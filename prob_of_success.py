import math
import pandas as pd
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution

class ProbSuccess(Distribution):
    """ ProbSuccess class is used for calculating and 
    visualizing a Binomial distribution.
    This class has methods and attributes to model the number of successes
    in a sample size n drawn with replacement from a population of size N. n
    could be anything such as number of experiments with one expreiment n = 1
     having a sequence of yes/1/success or no/0/failure. 
    
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring
        n (int) the total number of experiments/trial        
    """
    
    #       A binomial distribution is defined by two variables: 
    #           the probability of getting a positive outcome
    #           the number of trials
    
    #       If you know these two values, you can calculate the mean and the standard deviation
    #       
    #       For example, if you flip a fair coin 25 times, p = 0.5 and n = 25
    #       You can then calculate the mean and standard deviation with the following formula:
    #           mean = p * n
    #           standard deviation = sqrt(n * p * (1 - p))
    
    #       
    
    def __init__(self, prob=.5, size=20):
        Distribution.__init__(self, mu = 0, sigma = 1)
        self.p = prob
        self.n = size
        Distribution.read_data_file('numbers_binomial.txt')         
    
    def calculate_mean(self):
    
        """Function to calculate the mean from p and n
        
        Args: 
            None
        
        Returns: 
            float: mean of the data set
    
        """
                
        self.mean = self.n * self.p
        return self.mean



    def calculate_stdev(self):

        """Function to calculate the standard deviation from p and n.
        
        Args: 
            None
        
        Returns: 
            float: standard deviation of the data set
    
        """
        self.stdev = (self.n*self.p*(1-self.p))**0.5
        return self.stdev
        
        
        
    def replace_stats_with_data(self):
    
        """Function to calculate p and n from the data set
        
        Args: 
            None
        
        Returns: 
            float: the p value
            float: the n value
    
        """        
        
        self.n = len(self.data)
        k = []
        self.p = len([k.append(l) for l in self.data if l > 0])/self.n
        self.calculate_mean()
        self.calculate_stdev
        return self.n, self.p
        
    def plot_bar(self):
        """Function to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            None
        """
            
        # Using the matplotlib package to plot a bar chart of the data
        #       The x-axis should have the value zero or one
        #       The y-axis should have the count of results for each case
        #
        #       For example, say you have a coin where heads = 1 and tails = 0.
        #       If you flipped a coin 35 times, and the coin landed on
        #       heads 20 times and tails 15 times, the bar chart would have two bars:
        #       0 on the x-axis and 15 on the y-axis
        #       1 on the x-axis and 20 on the y-axis
        df = pd.DataFrame(pd.Series(self.data).value_counts())
        df.plot(kind = 'bar')
        plt.xlabel('Possibilities')
        plt.ylabel('Number of outcomes')
        plt.title('Bar chart of occurences')
        plt.show()      
        
    def pdf(self, k):
        """Probability density function calculator for the gaussian distribution.
        
        Args:
            k (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output, pdf_
        """
        
        # Here we calculate the probability density function for a binomial distribution
        #  For a binomial distribution with n trials and probability p, 
        #  the probability density function calculates the likelihood of getting
        #   k positive outcomes. 
        # 
        #   For example, if you flip a coin n = 60 times, with p = .5,
        #   what's the likelihood that the coin lands on heads 40 out of 60 times?
        def factor(b):
            ''' This calculates the factorial of any any number b
            factor(b) = b! = b*(b-1)*(b-2)*....*(b-(b-1))
            
            Args:
                b (int): any integer you want
            
            Returns:
                The factorial of the integer b. 
            '''
            result =  1
            for i in range(1, b+1):
                result = result*i
            return result
        
        nk = (self.n) - k
        return ((factor(self.n)/factor(k)*factor(nk))*(((self.p)**k)*(1-self.p)**nk))

    def plot_bar_pdf(self):

        """Function to plot the pdf of the binomial distribution
        
        Args:
            None
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """
    
        # Use a bar chart to plot the probability density function from
        # k = 0 to k = n
        
        #   uses the pdf() method defined above to calculate the
        #   density function for every value of k.
        x = []
        y = []
        for i in range(self.n+1):
            x.append(i)
            bh = self.pdf(i)
            y.append(bh)
        #fig, axes = plt.subplots(2,sharex=True)
        self.plot_bar()

        plt.plot(x, y)
        plt.title('Normal Distribution for \n Sample Mean and Sample Standard Deviation')
        plt.ylabel('Density')
        plt.xlabel('Number of successes')
        plt.show()

        return x, y
                
    def __add__(self, other):
        
        """Function to add together two Binomial distributions with equal p
        
        Args:
            other (Binomial): Binomial instance
            
        Returns:
            Binomial: Binomial distribution
            
        """
        
        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise
                
        result = ProbSuccess()
        result.mean = self.calculate_mean() + other.calculate_mean()
        result.stdev = math.sqrt(self.calculate_stdev() ** 2 + other.calculate_stdev() ** 2)
        return result
        
        
    def __repr__(self):
    
        """Function to output the characteristics of the PossSuccess (Binomial) instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the PossSuccess
        
        """
        
        return "mean {}, standard deviation {}, p {}, n {}".\
        format(self.mean, self.stdev, self.p, self.n)