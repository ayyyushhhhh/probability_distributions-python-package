# TODO: import necessary libraries
from .Generaldistribution import Gaussian 
import math
from matplotlib import pyplot as plt
# TODO: make a Binomial class that inherits from the Distribution class. Use the specifications below.

class Binomial(Distribution):
    """ Binomial distribution class for calculating and 
    visualizing a Binomial distribution.

    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring
                
    """
 
    def __init__(self,n,p):
        Distribution.__init__(self, mu, sigma)
        self.n = n
        self.p = p
        

    def calculate_mean(self):
        """Function to calculate the mean from p and n
        
        Args: 
            None
        
        Returns: 
            float: mean of the data set
    
        """
        self.mean = self.n * self.p 
        return self.n * self.p 

    def calculate_stdev(self):

        """Function to calculate the standard deviation from p and n.
        
        Args: 
            None
        
        Returns: 
            float: standard deviation of the data set
    
        """
        self.stdev = math.sqrt(self.n * self.p * (1-self.p))
        return math.sqrt(self.n * self.p * (1-self.p))

    def replace_stats_with_data(self):
        """Function to calculate p and n from the data set. The function updates the p and n variables of the object.
        
        Args: 
            None
        
        Returns: 
            float: the p value
            float: the n value
    
        """
        self.n = len(self.data)
        self.p = 1.0 * sum(self.data) / len(self.data) 
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()
        return self.p , self.n
    
    # TODO: write a method plot_bar() that outputs a bar chart of the data set according to the following specifications.
        
    def plot_bar():
        """Function to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            None
        """
        plt.bar(x = ['0', '1'], height = [(1 - self.p) * self.n, self.p * self.n])
        plt.title('Bar Chart of Data')
        plt.xlabel('outcome')
        plt.ylabel('count')
        

    def pdf(self,r):
        """Probability density function calculator for the binomial distribution.
        
        Args:
            k (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """
        nCr = factorial(self.n)/(factorial(self.n - r) * factorial (r))

        return nCr * self.p**r * (1-self.p)**(self.n - r)

        

    # write a method to plot the probability density function of the binomial distribution
    def plot_bar_pdf(self):
        """Function to plot the pdf of the binomial distribution
        
        Args:
            None
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """
        x = []
        f_x = []
        for i in range(self.n+1):
            x.append(i)
            f_x.append(pdf(i))
        
        plt.bar(x, f_x)
        plt.title('Distribution of Outcomes')
        plt.ylabel('Probability')
        plt.xlabel('Outcome')

        plt.show()
        return x,f_x


                
    # write a method to output the sum of two binomial distributions. Assume both distributions have the same p value.
    def __add__(self,other):
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
        result = Binomial(self.n, self.p)
        result.n = self.n + other.n
        result.p = self.p 
        result.mean = self.mean
        result.stdev = self.stdev
        return result

                        
    def __repr__(self):
        """Function to output the characteristics of the Binomial instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Binomial object
        
        """
        return "mean {} , standard deviation {} , p {} n {}".format(self.mean,self.stdev,self.p,self.n)
       
