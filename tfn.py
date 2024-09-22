#Testing for NEA's sake

from datasetpreparation import *
ds = prepareDataset()
print(ds.iloc[40:70])
atHashRemover(ds)
print(ds.iloc[40:70])


