import numpy as np
import matplotlib.pyplot as pl
#loading data
data_tr=np.loadtxt("data_tr.txt", dtype=str, delimiter='\t')
#see how is made the array
data_tr.shape
data_tr[:5,5]
#remove column and row names and convert into float
x_tr=data_tr[1:,1].astype(np.float)
#check if it worked
x_tr.shape
#load training set label
y_tr = np.loadtxt("classes_tr,txt", dtype=np.int)
y_tr[:10]
feat_tr = data_tr[0,1:]
samp_tr= data_tr[1:,0]
data_ts = np.loadtxt("data_ts


from sklearn.decomposition import PCA
#create object
pca=PCA(n_components=2)
z_tr = pca.fit_trnsform(x_tr)

z_ts = pca.transform(x.ts)

import


































































