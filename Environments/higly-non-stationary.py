# Class for a higly non stationary environment, like the stochastic one but with the distribution changing at each round
import numpy as np
import random
from Environments.environment import Environment

class HighlyNonStationaryEnvironment(Environment):
    def __init__(self, num_products = 1):
        """
        Initialize the stochastic environment with a given number of products and distribution type.
        :param num_products: Number of products (arms) in the environment
        :param distribution: Type of distribution to use for rewards (e.g., "Gaussian", "Bernoulli")
        :param distribution_params: Parameters for the distribution (e.g., mean and std for Gaussian)
        """
        super().__init__()
        self.num_products = num_products
        self.distributions_methods = [self._gaussian_distribution, self._bernoulli_distribution]
    
    def _gaussian_distribution(self):
        """
        Initialize a Gaussian distribution with random mean and standard deviation.
        :return: A function that returns a random value from the Gaussian distribution
        """
        mean = random.uniform(0, 10)
        std = random.uniform(0, 5)
        
        def sample():
            return np.random.normal(mean, std)
        
        return sample

    def _bernoulli_distribution(self):
        """
        Initialize a Bernoulli distribution with a random probability of success.
        :return: A function that returns a random value from the Bernoulli distribution
        """
        p = random.uniform(0, 1)
        
        def sample():
            return np.random.binomial(1, p)
        
        return sample

    def get_reward(self, arm):
        """
        Get the reward for the given arm (product).
        :param arm: The arm list of selling prices for each product
        :return: The reward for the given arm, 0 if the price is higher than the value sampled from the distribution, 1 otherwise
        """
        # Sample values from the distributions for each product
        values = []
        for i in range(self.num_products):
            # Randomly select a distribution initialization method
            distribution_method = random.choice(self.distributions_methods)
            # Sample a value from the selected distribution
            values.append(distribution_method())

        # Return 1 if the arm price is less than the sampled value, else 0
        return [1 if arm[i] < values[i] else 0 for i in range(self.num_products)]