from abc import ABC, abstractmethod

class interface_sample(ABC):
    # If the sample_method() is passed onto another class, then
    # it must be implemented
    @abstractmethod
    def sample_method(self,variable_1,variable_2):
        pass

class implementation(interface_sample):
    def __init_(self):
        pass

    def sample_method(self):
        pass

# Error example:
# TypeError: Can't instantiate abstract class implementation with abstract
# methods sample_method
imp = implementation()
