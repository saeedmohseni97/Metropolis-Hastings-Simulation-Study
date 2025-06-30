#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 15:31:26 2024

@author: saeedmohsenisehdeh
"""

import numpy as np
from scipy.stats import norm, t

def MH_n2t(num_iter, df, std):
    samples = np.zeros((num_iter + 1,1))
    z0 = 0
    for i in range(num_iter):
        u = np.random.uniform(0,1)
        v = np.random.normal(0, 1)
        
        target_ratio = t.pdf(v, df) / t.pdf(z0, df)
        proposal_ratio = norm.pdf(z0, loc=0, scale=std) / norm.pdf(v, loc=0, scale=std)
        rho = min(1, target_ratio * proposal_ratio)
        if (rho >= u):
            z0 = v
            samples[i+1, 0] = v
        else: 
            z0 = z0
            samples[i+1, 0] = z0
    return(samples)


def MH_t2n(num_iter, df, std):
    samples = np.zeros((num_iter + 1,1))
    z0 = 0
    for i in range(num_iter):
        u = np.random.uniform(0,1)
        v = np.random.standard_t(df,1)
        
        target_ratio = norm.pdf(v, loc=0, scale=std)/ norm.pdf(z0, loc=0, scale=std)
        proposal_ratio = t.pdf(z0, df) / t.pdf(v, df)
        
        rho = min(1, target_ratio * proposal_ratio)
        if (rho >= u):
            z0 = v
            samples[i+1, 0] = v
        else: 
            z0 = z0
            samples[i+1, 0] = z0
    return(samples) 

    
def MH_n2t_2(num_iter, df, std):
    samples = np.zeros((num_iter + 1,1))
    z0 = 0
    for i in range(num_iter):
        u = np.random.uniform(0,1)
        v = np.random.normal(z0, 1)
        
        target_ratio = t.pdf(v, df) / t.pdf(z0, df)
        #proposal_ratio = norm.pdf(z0, loc=z0, scale=std) / norm.pdf(v, loc=z0, scale=std)
        proposal_ratio = 1
        rho = min(1, target_ratio * proposal_ratio)
        
        if (rho >= u):
            z0 = v
            samples[i+1, 0] = v
        else: 
            z0 = z0
            samples[i+1, 0] = z0
    return(samples)