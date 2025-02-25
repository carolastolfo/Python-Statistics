import pandas as pd
import numpy as np
from scipy import stats

data = np.array(pd.read_csv('data.csv', header=None)).flatten()
range_ = np.max(data) - np.min(data)
var_ = np.var(data, ddof=1)
std_dev_ = np.std(data, ddof=1)

print('range =', range_)
print('var =', var_)
print('std dev =', std_dev_)

print('\n>>> END <<<')
