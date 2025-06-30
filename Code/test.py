#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 15:28:33 2024

@author: saeedmohsenisehdeh
"""

## Importing required packages and methods
import sys
sys.path.append('Functions')
import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, t

def metropolis_hastings(num_samples, initial_value, proposal_std, df):
    samples = [initial_value]
    current_value = initial_value
    
    for _ in range(num_samples):
        # Generate a candidate sample from the proposal distribution
        candidate_value =  np.random.normal(0, proposal_std)
        
        # Calculate the ratio of the target distribution (t-distribution) and the proposal distribution (normal)
        target_ratio = t.pdf(candidate_value, df) / t.pdf(current_value, df)
        proposal_ratio = norm.pdf(candidate_value, loc=0, scale=proposal_std) / norm.pdf(current_value, loc=0, scale=proposal_std)
        
        # Calculate acceptance probability
        acceptance_prob = min(1, target_ratio / proposal_ratio)
        
        # Accept or reject the candidate sample
        if np.random.rand() < acceptance_prob:
            current_value = candidate_value
        
        samples.append(current_value)
    
    return np.array(samples)

# Parameters
num_samples = 10000
initial_value = 0  # Initial value for the Markov chain
proposal_std = 1   # Standard deviation for the proposal distribution (normal)
df = 5             # Degrees of freedom for the t-distribution

# Generate samples using Metropolis-Hastings algorithm
samples = metropolis_hastings(num_samples, initial_value, proposal_std, df)

# Plot the histogram of generated samples
plt.figure(figsize=(8, 6))
plt.hist(samples, bins=50, density=True, color='blue', alpha=0.6)

# Plot the true density of the t-distribution for comparison
x = np.linspace(t.ppf(0.001, df), t.ppf(0.999, df), 1000)
plt.plot(x, t.pdf(x, df), 'r-', lw=2, label='True t-distribution PDF')

plt.title('Metropolis-Hastings Samples vs. True t-distribution')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()



sorted_data = np.sort(samples)
sorted_data = np.quantile(samples, np.linspace(0, 1, len(samples)))
norm_quantiles = t.ppf(np.linspace(0, 1, len(samples)), df)

# Step 3: Plot QQ Plot
plt.figure(figsize=(8, 6))
plt.scatter(norm_quantiles, sorted_data, color='blue', alpha=0.6)
plt.plot(np.linspace(-20, 20, len(samples)), np.linspace(-20, 20, len(samples)))
plt.title('QQ Plot')
plt.xlabel('Theoretical Quantiles')
plt.ylabel('Sample Quantiles')
plt.grid(True)
plt.show()
