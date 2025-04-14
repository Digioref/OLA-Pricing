# Abstract base class for environment
# This class defines the interface for all environments with the following methods:
# get_reward: returns the reward for the given arm
class Environment:
    def __init__(self):
        pass
    
    def get_reward(self, arm):
        raise NotImplementedError("This method should be overridden by subclasses")