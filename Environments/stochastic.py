# Class for stochastic environments
import numpy as np
from Environments.environment import Environment


class StochasticEnv(Environment):
    def __init__(self, num_products = 1, distribution = "Gaussian", distribution_params = None):
        """
        Initialize the stochastic environment with a given number of products and distribution type.
        :param num_products: Number of products (arms) in the environment
        :param distribution: Type of distribution to use for rewards (e.g., "Gaussian", "Bernoulli")
        :param distribution_params: Parameters for the distribution (e.g., mean and std for Gaussian)
        """
        super().__init__()
        self.num_products = num_products
        # Initialize one distribution for each product
        if distribution == "Gaussian":
            self.distributions = [self._init_gaussian_distribution(distribution_params) for _ in range(num_products)]
        elif distribution == "Bernoulli":
            self.distributions = [self._init_bernoulli_distribution(distribution_params) for _ in range(num_products)]
        else:
            raise ValueError("Unsupported distribution type. Use 'Gaussian' or 'Bernoulli'.")
    
    def _init_gaussian_distribution(self, params):
        """
        Initialize a Gaussian distribution with the given parameters.
        :param params: Parameters for the Gaussian distribution (mean and std)
        :return: A callable that returns a reward from the Gaussian distribution
        """
        # Check if the parameters are valid
        if len(params) != 2:
            raise ValueError("Gaussian distribution requires two parameters: mean and standard deviation.")
        
        mean, std = params
        if std <= 0:
            raise ValueError("Standard deviation must be positive.")
        
        # Create a Gaussian distribution with the given mean and std
        return lambda: np.random.normal(mean, std)

    def _init_bernoulli_distribution(self, params):
        """
        Initialize a Bernoulli distribution with the given parameters.
        :param params: Parameters for the Bernoulli distribution (probability of success)
        :return: A callable that returns a reward from the Bernoulli distribution
        """
        # Check if the parameter is valid
        if len(params) != 1 or params[0] < 0 or params[0] > 1:
            raise ValueError("Bernoulli distribution requires one parameter: probability of success (between 0 and 1).")
    
        p = params[0]
        
        # Create a Bernoulli distribution with the given probability
        return lambda: np.random.binomial(1, p)

    def get_reward(self, arm):
        """
        Get the reward for the given arm (product).
        :param arm: The arm list of selling prices for each product
        :return: The reward for the given arm, 0 if the price is higher than the value sampled from the distribution, 1 otherwise
        """
        # Sample values from the distributions for each product
        values = [distribution() for distribution in self.distributions]

        # Return 1 if the arm price is less than the sampled value, else 0
        return [1 if arm[i] < values[i] else 0 for i in range(self.num_products)]