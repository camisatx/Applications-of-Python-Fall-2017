# Applications of Python
### Fall 2017

This is the course content for the Fall 2017 Applications of Python class. The main projects will focus on finance and data science.

## Class 1

[Presentation](https://docs.google.com/presentation/d/1HLHjUlhV3QzeNNu6LckHgx63TIdyeWzPgg-KPo0x0IA/edit?usp=sharing)

Class 1 discusses the main applications for python, and introduces [Quantopian](https://www.quantopian.com) along with a [basic simple moving average strategy](./quantopian/sma_basic.py).

To run the SMA crossover strategy, go to [quantopian.com](https://www.quantopian.com) (create an account if you want to save your strategies), select **Algorithms** from the **Research** tab, and click **New Algorithm**. Type in a name for this new algorithm (such as *SMA Crossover*), click **Create Algorithm**, then copy and paste the code in [**this**](./quantopian/sma_basic.py) file over the existing code in the left window (completely deleting the code that appears there). Now you can click **Build Algorithm** above the code, and this strategy will be backtested.

For practice, try to make this strategy profitable over different time periods and with different tickers!

If you need help with the Quantopian API, check out their extensive [documentation](https://www.quantopian.com/help).

To learn more about how Quantopian works, view their [tutorials](https://www.quantopian.com/tutorials) and [lecturers](https://www.quantopian.com/lectures).

You can find strategies from other Quantopian members in the [forum](https://www.quantopian.com/posts). This is a great place to learn how others use Quantopian, along with learning more about strategies.

## Class 2

[Presentation](https://docs.google.com/presentation/d/1XBmdWTQ_t-GdZBNz1mOL7fh0jZv8-LS1xfEjs10JZIQ/edit?usp=sharing)

Class 2 explore [Quantopian](https://www.quantopian.com) more. We look at a more advanced strategy that utilizes the Pipeline for restricting the stocks it considers. We also explore the research notebook system of Quantopian.

We focus on the [Reversals During Earning Announcements](./quantopian/reversales/during/earnings/reversals_during_earnings.py), which suggests that the uncertainty regarding anticipated information events elicits predictable increases in expected returns to liquidity provision.

To learn more about how the Quantopian Pipeline works, check out this [tutorial](https://www.quantopian.com/tutorials/pipeline#lesson1).

## Class 3

[Presentation](https://docs.google.com/presentation/d/1v6GHA0OaDzje116zdP8o-ScQsA-esWAYuOmhA7dxy68/edit?usp=sharing)

Class 3 covers the development environment, and a quick intro to web apps.

We discuss what dev environments are, and how [Anaconda](https://www.anaconda.com/download) can be used to fulfill our needs. Also, we look into web apps, including the MVC architecture and a quick Flask example.

Be sure to read through some Flask tutorials on the internet.
