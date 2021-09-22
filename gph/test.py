from gph.python import ripser_parallel
import numpy as np
import time


X = np.loadtxt('cloud_h10.txt', delimiter = ' ')

start = time.time()
lst = ripser_parallel(X, maxdim=3, metric='precomputed', collapse_edges=True)
#lst = ['we']
done = time.time()
elapsed = done - start

print ("Time elapse ", elapsed)

print(lst)

