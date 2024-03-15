
# write a function that takes an integer n 
# and returns n samples from the Benford
# distribution.

from math import log10
from typing import List
from random import random

benford_distribution = [log10((k+1)/k) for k in range(1,10)]

# P(X <= t) c.d.f. of x

def sample_from_distribution(support: List[float], 
                             probabilities: List[float],
                             n : int) -> List[float]:
    
   
    if support == None:
        support = range(1, len(probabilities)+1)
    if len(support) != len(probabilities):
        raise ValueError("The support and the list of probabilities must have the same length")
    
    samples = []



    for _ in range(n):
            
        r = random()
        cummulative_sum = 0
        for i, prob in enumerate(probabilities):
            cummulative_sum += prob
            #######################
            if r < cummulative_sum:
                samples.append(i)
                break
    if n==1:
        return samples[0]
    else:
        return samples
            
# print(sample_from_distribution(probabilities=benford_distribution, n=10))


# We can use (at home) the Kolmogorev-Smirnov test.

class ProbabilityDistribution():
    def __init__(self, ) -> None:
        pass



class DiscreteProbabilityDistribution():
    def __init__(self, support: List[float], probabilities: List[float]):
        self.support = support
        self.probabilities = probabilities
        self.expectation = self.compute_moment(moment=1)
        self.variance = self.compute_moment(moment=2)- self.expectation
        self.standard_deviation = self.variance**(1/2)

    def compute_moment(self, moment: int):
        powers = [element**moment for element in self.support]
        ###
        return sum([prob*powers[i] for i, prob in enumerate(self.probabilities)])

benford = DiscreteProbabilityDistribution(support=range(1.10), probabilities=benford_distribution)

print(benford.variance)
print(benford.standard_deviation)