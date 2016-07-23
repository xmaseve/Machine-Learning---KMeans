# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 10:58:55 2016

@author: YI
"""

import numpy as np

def distEuc(x, y):
    return np.sqrt(sum(np.power(x-y,2)))
    
def ranCentroid(dataset, k):
    n = np.shape(dataset)[1]
    centroids = np.mat(np.zeros((k, n)))
    for i in range(n):
        minI = min(dataset[:, i])
        rangeI = float(max(np.mat(dataset)[:, i] - minI))
        centroids[:, i] = minI + rangeI * np.random.rand(k, 1)
    return centroids
        
def kMeans(dataset, k):
    m = np.shape(dataset)[0]
    clusterAssment = np.mat(np.zeros((m, 2)))
    centroids = ranCentroid(dataset, k)
    clusterChange = True
    while clusterChange:
        clusterChange = False
        for i in range(m):
            minDist = inf
            minIndex = -1
            for j in range(k):
                distIJ = distEuc(centroids[j, :], dataset[i, :])
                if distIJ < minDist:
                    minDist = distIJ
                    minIndex = j
            if clusterAssment[i,0] != minIndex:
                clusterChange = True
            clusterAssment[i, :] = minIndex, minDist**2
        print centroids
        for cent in range(k):
            for row in range(m):
                cluster = []
                if clusterAssment[row, :] == cent:
                    cluster.append([dataset[row, :]])
                centroids[cent, :] = np.mean(cluster, axis=0)
                del cluster
    return centroids, clusterAssment
                
                
                
                
                
                
                
                