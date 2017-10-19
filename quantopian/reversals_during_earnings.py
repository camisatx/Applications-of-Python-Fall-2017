""" Reversals during Earnings Announcements
https://www.quantopian.com/posts/quantpedia-trading-strategy-series-reversals-during-earnings-announcements

The strategy limits its universe to those stocks in the Q500US which are at or above the 95th percentile of average dollar volume among all equities on the platform. One day before each earnings announcement for each company, the algorithm determines the stock's 5-day returns quintile among all equities. Since reversal is expected, the algorithm goes short on the stock if it's in the highest quintile and long if it's in the lowest quintile. Positions are usually held for one day.

For non-premium subscribers, you're able to run the backtest until 2 years ago
    from today.
"""

import numpy as np
import pandas as pd

from quantopian.algorithm import attach_pipeline, pipeline_output
from quantopian.pipeline import Pipeline
from quantopian.pipeline.classifiers.morningstar import Sector
from quantopian.pipeline.data import morningstar as mstar
from quantopian.pipeline.data.builtin import USEquityPricing
from quantopian.pipeline.factors import AverageDollarVolume, Returns, CustomFactor
from quantopian.pipeline.factors.eventvestor import BusinessDaysUntilNextEarnings
from quantopian.pipeline.filters.morningstar import Q500US

def initialize(context):
    context.RETURNS_LOOKBACK = 5
    context.RETURNS_QUANTILES = 5
    context.DAYS_TO_HOLD = 1
    context.MAX_DAYS_TO_HOLD = 6
    context.MAX_IN_ONE = 1.0
    
    context.longs = [[]] * context.DAYS_TO_HOLD
    context.shorts = [[]] * context.DAYS_TO_HOLD
    
    attach_pipeline(make_pipeline(context), 'my_pipeline')
    
    schedule_function(rebalance, date_rules.every_day(), time_rules.market_open())
    schedule_function(record_vars, date_rules.every_day(), time_rules.market_close())
    
def make_pipeline(context):
    adv = AverageDollarVolume(
        window_length=30,
        mask=USEquityPricing.volume.latest > 0,
    )
    return Pipeline(
        columns={
            'returns_quantile': Returns(
                window_length=context.RETURNS_LOOKBACK,
                mask=adv.notnan()
            ).quantiles(context.RETURNS_QUANTILES),
        },
        screen=((BusinessDaysUntilNextEarnings().eq(1))
                & Q500US() & adv.percentile_between(95, 100))
    )

def before_trading_start(context, data):
    context.output = pipeline_output('my_pipeline')

    def update_record(record, new_item):
        record.insert(0, new_item)
        if len(record) > context.MAX_DAYS_TO_HOLD:
            del(record[-1])
        while len(record) > context.DAYS_TO_HOLD and len(record[-1]) == 0:
            del(record[-1])
        if sum(map(lambda l: 0 if len(l) == 0 else 1, record)) > context.DAYS_TO_HOLD:
            del(record[-1])
    
    update_record(context.longs, context.output.index[
        context.output['returns_quantile'] == 0
    ])
    update_record(context.shorts, context.output.index[
        context.output['returns_quantile'] ==
            context.RETURNS_QUANTILES - 1
    ])
        
def rebalance(context, data):
    # Convert the list of lists to a single list: [[1, 2], [3, 4]] -> [1, 2, 3, 4]
    long_list = [equity for sublist in context.longs for equity in sublist]
    short_list = [equity for sublist in context.shorts for equity in sublist]
    
    # For each long position, enter an order for the lower of the max in one variable
    #	or 50% * the number of positions
    for equity in long_list:
        if data.can_trade(equity):
            order_target_percent(equity, min(0.5 / len(long_list), context.MAX_IN_ONE))
    # for equity in short_list:
    #     if data.can_trade(equity):
    #         order_target_percent(equity, -min(0.5 / len(short_list), context.MAX_IN_ONE))
    
    # Exit any position current in the portfolio that isn't on our long or short list
    for position in context.portfolio.positions:
        if position not in long_list + short_list:
            order_target_percent(position, 0)
            
def record_vars(context, data):
    record(leverage=context.account.leverage)
