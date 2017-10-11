def initialize(context):
    
    # Use AAPL for this strategy
    context.stock = sid(24)
    
    # Perform the SMA crossover every day 1 hour after market open
    schedule_function(sma_crossover,
                      date_rules.every_day(),
                      time_rules.market_open(hours=1))


def sma_crossover(context, data):
    
    hist = data.history(context.stock, 'price', 50, '1d')
    
    # Calculate the 20 and 50 simple moving averages
    sma_20 = hist[-20:].mean()
    sma_50 = hist.mean()
    
    # Request to get the open orders
    open_orders = get_open_orders()
    
    # Only perform crossover check if there are no current oders for this stock
    if context.stock not in open_orders:
        if sma_20 > sma_50:
            # Set the target order for 100% (long) of our portfolio in AAPL
            order_target_percent(context.stock, 1.0)
            log.info('Buying %s' % context.stock.symbol)
        else:
            # Set the target order for -100% (short) or our portfolio in AAPL
            order_target_percent(context.stock, -1.0)
            log.info('Selling %s' % context.stock.symbol)
