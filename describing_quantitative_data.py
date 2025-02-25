import matplotlib.pyplot as plt
import numpy as np

min_ = 0  # TO DO
max_ = 6  # TO DO
bin_size_ = 1.0  # TO DO
frequencies = [0.0625, 0.125, 0.1875, 0.25, 0.1875, 0.125, 0.0625]  # TO DO

range_ = list(np.arange(min_, max_, bin_size_))
range_.append(max_)
bins_ = list(np.arange(min_ + bin_size_ / 2, max_ - bin_size_ / 2, bin_size_))
bins_.append(max_ - bin_size_ / 2)

histogram = plt.figure('Histogram')
plt.bar(bins_, frequencies, width=bin_size_, edgecolor='black')
plt.xticks(range_)
plt.title('Histogram')
histogram.savefig('histogram.png', format='png', dpi=1200)

plt.show()

print('\n>>> END <<<')
