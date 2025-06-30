#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 21:27:06 2024

@author: saeedmohsenisehdeh
"""

#%% Adding the path to function files:
import sys
sys.path.append('Functions')

import numpy as np
import pickle
import matplotlib.pyplot as plt
from scipy.stats import norm, t
#%% parameters:
num_iter = [10, 100, 1000, 10000]
df = [2, 5, 10, 20]
#%% Loading the Results:
Variables = [0,0,0]
Names = ["MH_n2t", "MH_n2t_2", "MH_t2n"] 

for count in range(len(Names)):
    with open(f'../Results/{Names[count]}_samples.pkl', 'rb') as f:
        Variables[count] = pickle.load(f)
MH_n2t, MH_n2t_2, MH_t2n = Variables[0],Variables[1],Variables[2]
#%% Plotting:

# Creating all histograms:
fig_size = 16
sub_title_margin = 2
for k in range(len(Names)):     

    if k ==2:
        fig, axs = plt.subplots(4, 4, figsize=(fig_size, fig_size))
        fig.suptitle('Histogram of Data (From t-distribution to Normal)', fontsize=16)      
        for i in range(4):
            for j in range(4):
                ax = axs[i,j]
                ax.hist(Variables[k][i][j], bins=30, color='blue', edgecolor='black', density = True)
                x = np.linspace(norm.ppf(0.001), norm.ppf(0.999), 1000)
                ax.plot(x, norm.pdf(x), 'r--', lw=2, label='True Normal PDF')
                ax.set_title(fr'$N = {num_iter[j]}, \nu = {df[i]}$')
                ax.set_xlabel('Value')
                ax.set_ylabel('Probability')
                ax.grid(True)
                ax.legend()
            plt.tight_layout() 
            plt.savefig(f'../Figures/Histogram_{Names[k]}.pdf')
            print("Histogram Figures saved as PDFs.")      
    elif k == 1:
        fig, axs = plt.subplots(4, 4, figsize=(fig_size, fig_size))
        plt.subplots_adjust(top=sub_title_margin)
        fig.suptitle('Histogram of Data (From  Normal to t-distribution, conditional proposal)', fontsize=16)
        for i in range(4):
            for j in range(4):
                ax = axs[i,j]
                ax.hist(Variables[k][i][j], bins=30, color='blue', edgecolor='black', density = True)
                x = np.linspace(t.ppf(0.001, df[i]), t.ppf(0.999, df[i]), 1000)
                ax.plot(x, t.pdf(x, df[i]), 'r--', lw=2, label='True t-distribution PDF')
                ax.set_title(fr'$N = {num_iter[j]}, \nu = {df[i]}$')
                ax.set_xlabel('Value')
                ax.set_ylabel('Probability')
                ax.grid(True)
                ax.legend()
            plt.tight_layout() 
            plt.savefig(f'../Figures/Histogram_{Names[k]}.pdf')
            print("Histogram Figures saved as PDFs.")
    else:
        fig, axs = plt.subplots(4, 4, figsize=(fig_size, fig_size))
        plt.subplots_adjust(top=sub_title_margin)
        fig.suptitle('Histogram of Data (From  Normal to t-distribution, unconditional proposal)', fontsize=16)
        for i in range(4):
            for j in range(4):
                ax = axs[i,j]
                ax.hist(Variables[k][i][j], bins=30, color='blue', edgecolor='black', density = True)
                x = np.linspace(t.ppf(0.001, df[i]), t.ppf(0.999, df[i]), 1000)
                ax.plot(x, t.pdf(x, df[i]), 'r--', lw=2, label='True t-distribution PDF')
                ax.set_title(fr'$N = {num_iter[j]}, \nu = {df[i]}$')
                ax.set_xlabel('Value')
                ax.set_ylabel('Probability')
                ax.grid(True)
                ax.legend()
            plt.tight_layout() 
            plt.savefig(f'../Figures/Histogram_{Names[k]}.pdf')
            print("Histogram Figures saved as PDFs.")
plt.show()


# Creating all the QQPlots
fig_size = 16
sub_title_margin = 1
for k in range(len(Names)):  
    if k ==2:
        fig, axs = plt.subplots(4, 4, figsize=(fig_size, fig_size))
        plt.subplots_adjust(top=sub_title_margin)
        fig.suptitle('QQ Plots (From t-distribution to Normal)', fontsize=16)
        for i in range(4):
            for j in range(4):
                ax = axs[i,j]
                dist_quantile = norm.ppf(np.linspace(0, 1, len(Variables[k][i][j])))
                sample_quantile = np.quantile(np.sort(Variables[k][i][j]), np.linspace(0, 1, len(Variables[k][i][j])))
                ax.scatter(dist_quantile, sample_quantile, color='blue', alpha=0.6)
                ax.plot(np.linspace(-10, 10, len(Variables[k][i][j])), np.linspace(-10, 10, len(Variables[k][i][j])),'r-', lw=2)
                
                ax.set_title(fr'$N = {num_iter[j]}, \nu = {df[i]}$')
                ax.set_xlabel('True Distribution Quantile')
                ax.set_ylabel('Sample Distribution Quantile')
                ax.grid(True)
                ax.legend()
            plt.tight_layout() 
            plt.savefig(f'../Figures/QQPlot_{Names[k]}.pdf')
            print("Histogram Figures saved as PDFs.")
    elif k ==1:
        fig, axs = plt.subplots(4, 4, figsize=(fig_size, fig_size))
        plt.subplots_adjust(top=sub_title_margin)
        fig.suptitle('QQ Plots (From  Normal to t-distribution, conditional proposal))', fontsize=16)
        for i in range(4):
            for j in range(4):
                ax = axs[i,j]
                dist_quantile = t.ppf(np.linspace(0, 1, len(Variables[k][i][j])),df[i])
                sample_quantile = np.quantile(np.sort(Variables[k][i][j]), np.linspace(0, 1, len(Variables[k][i][j])))
                ax.scatter(dist_quantile, sample_quantile, color='blue', alpha=0.6)
                ax.plot(np.linspace(-10, 10, len(Variables[k][i][j])), np.linspace(-10, 10, len(Variables[k][i][j])),'r-', lw=2)
                
                ax.set_title(fr'$N = {num_iter[j]}, \nu = {df[i]}$')
                ax.set_xlabel('True Distribution Quantile')
                ax.set_ylabel('Sample Distribution Quantile')
                ax.grid(True)
                ax.legend()
            plt.tight_layout() 
            plt.savefig(f'../Figures/QQPlot_{Names[k]}.pdf')
            print("Histogram Figures saved as PDFs.")
    else:
        fig, axs = plt.subplots(4, 4, figsize=(fig_size, fig_size))
        plt.subplots_adjust(top=sub_title_margin)
        fig.suptitle('QQ Plots (From  Normal to t-distribution, unconditional proposal))', fontsize=16)
        for i in range(4):
            for j in range(4):
                ax = axs[i,j]
                dist_quantile = t.ppf(np.linspace(0, 1, len(Variables[k][i][j])),df[i])
                sample_quantile = np.quantile(np.sort(Variables[k][i][j]), np.linspace(0, 1, len(Variables[k][i][j])))
                ax.scatter(dist_quantile, sample_quantile, color='blue', alpha=0.6)
                ax.plot(np.linspace(-10, 10, len(Variables[k][i][j])), np.linspace(-10, 10, len(Variables[k][i][j])),'r-', lw=2)
                
                ax.set_title(fr'$N = {num_iter[j]}, \nu = {df[i]}$')
                ax.set_xlabel('True Distribution Quantile')
                ax.set_ylabel('Sample Distribution Quantile')
                ax.grid(True)
                ax.legend()
            plt.tight_layout() 
            plt.savefig(f'../Figures/QQPlot_{Names[k]}.pdf')
            print("Histogram Figures saved as PDFs.")
plt.show()




