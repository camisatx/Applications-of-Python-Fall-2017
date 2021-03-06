# Applications of Python
### Fall 2017

This is the course content for the Fall 2017 Applications of Python class. The main projects will focus on finance and data science.

## Contents

- [Class 1](#class-1)
- [Class 2](#class-2)
- [Class 3](#class-3)
- [Class 4](#class-4)
- [Class 5](#class-5)
- [Class 6](#class-6)

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

## Class 4

[Presentation](https://docs.google.com/presentation/d/14K3PvUVDn_trTFC1Lb-CXPYDrsEXY08Ha279SFeZjso/edit?usp=sharing)

Class 4 covers building a simple Python program to check if a file has profanity in it.

We will code this example in the Spyder IDE (installed with Anaconda). The program will load a text file from the disk, and use an internet based API.

View the final script [here](./profanity_screen/profanity_screen.py), and a movie quote text file [here](./profanity_screen/movie_quotes_1.txt).

The code structure is covered in more detail in the Udacity [*Programming Foundations with Python*](https://www.udacity.com/course/programming-foundations-with-python--ud036) course.

## Class 5

[Presentation](https://docs.google.com/presentation/d/1OchbLbBuGsa2w33qtsuhHCkm782Exaau9aRyk41kqjM/edit?usp=sharing)

Class 5 introduces AI and machine learning. This is a very wide and deep field within computer science, so we only touch the surface.

We'll explore a simple example of classifying digit images using scikit learn.

View the Jupyter Notebook [here](./machine_learning/plot_digits_classification.ipynb).

If you'd like to learn more about machine learning, check out this multi-part series: [Machine Learning for Humans](https://medium.com/machine-learning-for-humans/why-machine-learning-matters-6164faf1df12)

## Class 6

[Presentation](https://docs.google.com/presentation/d/1md0fOp9EMEzXljNsXx5FalJoEfCGgtqil7JEHGNRrPs/edit?usp=sharing)

Class 6 investigates unsupervised machine learning, focusing specifically on clustering.

We look at K-Means clustering, and how we can use it to build a model to cluster the Iris dataset.

View the Jupyter Notebook [here](./iris/plot_cluster_iris.ipynb).
