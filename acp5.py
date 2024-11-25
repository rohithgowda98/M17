import scipy.stats as stats

# expected value = 10
# probability of observing 12 or more
prob1 = 1 - stats.poisson.cdf(11, 10)
print("Probability of observing 12 or more rainy days is :", prob1)

# expected value = 10
# probability of observing between 12 and 18
prob2 = stats.poisson.cdf(18, 10) - stats.poisson.cdf(11, 10)
print("Probability of observing between 12 to 18 rainy days is :", prob2)

