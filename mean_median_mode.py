import pandas as pd
import numpy as np
from scipy import stats

data = np.array(pd.read_csv('data.csv', header=None)).flatten()
mean_ = np.mean(data)
median_ = np.median(data)
mode_ = stats.mode(data, keepdims=True)

print('mean =', mean_)
print('median =', median_)
print('mode =', mode_[0], 'with frequency of', mode_[1])

print('\n>>> END <<<')
