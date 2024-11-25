import numpy as np
import matplotlib.pyplot as plt

# Generate a uniform distribution
np.random.seed(42)  # For reproducibility
population = np.random.uniform(0, 100, 10000)

# Plot the population distribution
plt.figure(figsize=(10, 5))
plt.hist(population, bins=50, color='skyblue', edgecolor='black', alpha=0.7)
plt.title("Population Distribution (Uniform)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# Central Limit Theorem Demonstration
sample_sizes = [5, 30, 50, 100]
means_list = []

for size in sample_sizes:
    sample_means = []
    for _ in range(1000):  # Take 1000 samples for each sample size
        sample = np.random.choice(population, size=size, replace=False)
        sample_means.append(np.mean(sample))
    means_list.append(sample_means)

# Plot sample means distributions
plt.figure(figsize=(10, 7))
for i, sample_means in enumerate(means_list):
    plt.hist(sample_means, bins=30, alpha=0.7, label=f"Sample size = {sample_sizes[i]}")

plt.title("Sample Mean Distributions (Central Limit Theorem)")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.legend()
plt.show()
