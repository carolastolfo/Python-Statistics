from statistics import median
from fractions import Fraction
from itertools import product
import numpy as np
import csv
import pandas as pd

df_input = pd.read_csv('population_distribution.csv')

x = []
p = []

for index, row in df_input.iterrows():
    x.append(float(row['x']))
    p_string = row['p(x)']
    if p_string.__contains__('/'):
        p.append(Fraction(p_string))
    else:
        p.append(float(p_string))

f1 = open('all_possible_samples.csv', 'w', newline='')
f2 = open('sampling_distribution.csv', 'w', newline='')
writer1 = csv.writer(f1)
writer2 = csv.writer(f2)

n = int(input('Please enter the sample size (n): '))

header = []
for i in range(0, n):
    header.append('x{:d}'.format(i + 1))

mode = input('Sampling Distribution of which sample statistics (mean, median, or variance): ').lower()

if mode == 'mean':
    header.append('mean')
    header.append('p(mean)')
elif mode == 'median':
    header.append('median')
    header.append('p(median)')
elif mode == 'variance':
    header.append('variance')
    header.append('p(variance)')

writer1.writerow(header)
writer2.writerow(header[:-3:-1])

indices_list = list(x for x in product(range(0, len(x)), repeat=n))

sampling_distribution_x = []
sampling_distribution_prob = []
for indices in range(0, len(indices_list)):
    p_temp = 1
    sum = 0
    row = []
    for index in range(0, n):
        print('{:.2f}\t'.format(x[indices_list[indices][index]]), sep='', end='')
        row.append(x[indices_list[indices][index]])
        sum = sum + x[indices_list[indices][index]]
        p_temp = p_temp * p[indices_list[indices][index]]
    if mode == 'mean':
        target_value = sum / n
    elif mode == 'median':
        target_value = median(row)
    elif mode == 'variance':
        target_value = np.var(row, ddof=1)
    sampling_distribution_x.append(target_value)
    row.append(target_value)
    sampling_distribution_prob.append(p_temp)
    row.append(str(p_temp))
    writer1.writerow(row)
    print('{:.2f}\t'.format(target_value), sep='', end='')
    print(p_temp)
    print()

print('\n***************\n')

sampling_distribution_x_array = np.array(sampling_distribution_x)
sampling_distribution_prob_array = np.array(sampling_distribution_prob)
values = list(set(sampling_distribution_x))
values.sort()
expected_value = 0

for i in range(0, len(values)):
    row = []
    print('{:.2f}\t'.format(values[i]), sep='', end='')
    row.append(format(values[i]))
    p_temp = np.sum(sampling_distribution_prob_array[np.where(sampling_distribution_x_array == values[i])])
    print(p_temp)
    row.append(str(p_temp))
    writer2.writerow(row)
    expected_value = expected_value + values[i] * p_temp

print('\n***************\n')

print('E(', sep='', end='')
if mode == 'mean':
    print('mean', sep='', end='')
elif mode == 'median':
    print('m', sep='', end='')
elif mode == 'variance':
    print('variance', sep='', end='')

print(') =', expected_value)

f2.close()
print()
