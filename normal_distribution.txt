import matplotlib.pyplot as plt
import numpy as np
import scipy
import scipy.stats as stats

mu = float(input('Please enter mean: '))
sigma = float(input('Please enter standard deviation: '))
mode = input('Please enter mode (lower-tail, upper-tail, both-tails, or interval): ')

x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)

ax = plt.gca()
ax.axes.xaxis.set_visible(False)

plt.ylim(bottom=0, top=1.1 * stats.norm.pdf(mu, mu, sigma))
ax.axes.yaxis.set_visible(False)

plt.plot(x, stats.norm.pdf(x, mu, sigma))
plt.vlines(x=mu - 3 * sigma, ymin=0, ymax=stats.norm.pdf(mu - 3 * sigma, mu, sigma), linestyles='dashed',
           colors='black')
plt.vlines(x=mu - 2 * sigma, ymin=0, ymax=stats.norm.pdf(mu - 2 * sigma, mu, sigma), linestyles='dashed',
           colors='black')
plt.vlines(x=mu - 1 * sigma, ymin=0, ymax=stats.norm.pdf(mu - 1 * sigma, mu, sigma), linestyles='dashed',
           colors='black')
plt.vlines(x=mu, label='mu', ymin=0, ymax=stats.norm.pdf(mu, mu, sigma), linestyles='dashed', colors='black')
plt.text(mu, -stats.norm.pdf(mu, mu, sigma) * 0.05, s='\u03BC={:.2f}'.format(mu), ha='center')
plt.vlines(x=mu + 1 * sigma, ymin=0, ymax=stats.norm.pdf(mu + 1 * sigma, mu, sigma), linestyles='dashed',
           colors='black')
plt.vlines(x=mu + 2 * sigma, ymin=0, ymax=stats.norm.pdf(mu + 2 * sigma, mu, sigma), linestyles='dashed',
           colors='black')
plt.vlines(x=mu + 3 * sigma, ymin=0, ymax=stats.norm.pdf(mu + 3 * sigma, mu, sigma), linestyles='dashed',
           colors='black')

b1 = mu - 3 * sigma
b2 = mu + 3 * sigma
if mode == 'lower-tail':
    b2 = float(input('Please enter the boundary value: '))
    plt.vlines(x=b2, ymin=0, ymax=stats.norm.pdf(b2, mu, sigma), linestyles='solid',
               colors='black')
    plt.text(b2, -stats.norm.pdf(mu, mu, sigma) * 0.05, b2, ha='center')
    region = np.linspace(b1, b2, 100)
    plt.fill_between(region, stats.norm.pdf(region, mu, sigma), color='pink')
    cdf = scipy.stats.norm.cdf(b2, mu, sigma)
    print('P(x < ', b2, ') = ', cdf, ' = ', cdf * 100, '%', sep='')
elif mode == 'upper-tail':
    b1 = float(input('Please enter the boundary value: '))
    plt.vlines(x=b1, ymin=0, ymax=stats.norm.pdf(b1, mu, sigma), linestyles='solid',
               colors='black')
    plt.text(b1, -stats.norm.pdf(mu, mu, sigma) * 0.05, b1, ha='center')
    region = np.linspace(b1, b2, 100)
    plt.fill_between(region, stats.norm.pdf(region, mu, sigma), color='pink')
    cdf = 1 - scipy.stats.norm.cdf(b1, mu, sigma)
    print('P(', b1, ' < x', ') = ', cdf, ' = ', cdf * 100, '%', sep='')
elif mode == 'both-tails':
    b1 = float(input('Please enter the lower boundary value: '))
    b2 = float(input('Please enter the upper boundary value: '))
    plt.vlines(x=b1, ymin=0, ymax=stats.norm.pdf(b1, mu, sigma), linestyles='solid',
               colors='black')
    plt.vlines(x=b2, ymin=0, ymax=stats.norm.pdf(b2, mu, sigma), linestyles='solid',
               colors='black')
    plt.text(b1, -stats.norm.pdf(mu, mu, sigma) * 0.05, b1, ha='center')
    plt.text(b2, -stats.norm.pdf(mu, mu, sigma) * 0.05, b2, ha='center')
    region = np.linspace(mu - 3 * sigma, b1, 100)
    plt.fill_between(region, stats.norm.pdf(region, mu, sigma), color='pink')
    region = np.linspace(b2, mu + 3 * sigma, 100)
    plt.fill_between(region, stats.norm.pdf(region, mu, sigma), color='pink')
    cdf = scipy.stats.norm.cdf(b1, mu, sigma) + 1 - scipy.stats.norm.cdf(b2, mu, sigma)
    print('P(x < ', b1, ' or ', b2, ' < x) = ', cdf, ' = ', cdf * 100, '%', sep='')
elif mode == 'interval':
    b1 = float(input('Please enter the lower boundary value: '))
    b2 = float(input('Please enter the upper boundary value: '))
    plt.vlines(x=b1, ymin=0, ymax=stats.norm.pdf(b1, mu, sigma), linestyles='solid',
               colors='black')
    plt.vlines(x=b2, ymin=0, ymax=stats.norm.pdf(b2, mu, sigma), linestyles='solid',
               colors='black')
    plt.text(b1, -stats.norm.pdf(mu, mu, sigma) * 0.05, b1, ha='center')
    plt.text(b2, -stats.norm.pdf(mu, mu, sigma) * 0.05, b2, ha='center')
    region = np.linspace(b1, b2, 100)
    plt.fill_between(region, stats.norm.pdf(region, mu, sigma), color='pink')
    cdf = scipy.stats.norm.cdf(b2, mu, sigma) - scipy.stats.norm.cdf(b1, mu, sigma)
    print('P(', b1, ' < x < ', b2, ') = ', cdf, ' = ', cdf * 100, '%', sep='')
else:
    print(mode, 'is an incorrect mode. It must be lower-tail, upper-tail, both-tails, or interval.')
    exit(0)

plt.savefig('normal_distribution_sketch.png', format='png', dpi=1200)

plt.show()
