import math
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

import matplotlib as mpl 
mpl.use('Agg')
import matplotlib.pyplot as plt 
plt.figure(figsize=(10, 5))

import numpy as np
from sklearn.linear_model import LinearRegression

import os
import argparse

# Create a directory for saving figures if it doesn't exist
output_directory = 'generated'
os.makedirs(output_directory, exist_ok=True)

# make sure variable is just an integer
n = 1

plt.xlabel('Number of iterations')
plt.ylabel('Number value')
plt.title('Hailstone numbers: number %i' % n)

def get_cmap(n, name='hsv'):
    '''Returns a function that maps each index in 0, 1, ..., n-1 to a distinct 
    RGB color; the keyword argument name must be a standard mpl colormap name.'''
    return plt.cm.get_cmap(name, n)


isLog = 0
height = 0

# Create the argument parser
parser = argparse.ArgumentParser(description='Driver Program')

# Add an optional option for the plot argument
parser.add_argument('-p', '--plot', help='List of values for plotting', default='list(range(1, 101))')
parser.add_argument('-l', '--log', help='Log axis scaling, 0 for non, 1 for y axis, 2 for both', default=0, type=int)
parser.add_argument('-ht', '--height', help='Specify the height of a graph', default=0, type=int)

# Parse the command-line arguments
args = parser.parse_args()

# Parse the plot argument into a list
n = eval(args.plot)
isLog = args.log
height = args.height

# conut starts at 0 because the seed is not an iteration
count = 0
Arr = [[0],[n]]

# for border of x axis
if isLog == 2:
    count = 1
    Arr = [[1], [n]]

print("Begin sequence: ")

while n > 1:
    print(n)
    if n % 2 == 0:
        n = n / 2
    else:
        n = ((n * 3) + 1)
    count += 1
    Arr[0].insert(count,count)
    Arr[1].insert(count,n)

print(n)

x = Arr[0]
y = Arr[1]

# only for isLog == 3
log_arr = np.log(Arr[1])

if isLog == 3:
    # Perform linear regression
    X = np.arange(len(log_arr)).reshape(-1, 1)
    regressor = LinearRegression()
    regressor.fit(X, log_arr)

    # Get the slope of the linear regression
    slope = regressor.coef_[0]
    print("Linear Regression Slope: %f" % slope)

    # Create a new dataset by subtracting the slope of the linear regression
    noLog_dataset = log_arr - slope * X.flatten()

if isLog == 3:
    plt.plot(x, noLog_dataset, 'k,-', linewidth=0.9)
else: 
    plt.plot(x, y, 'k,-', linewidth=0.9)

cmap = get_cmap(len(x))

for k in range(count + 1):
    if isLog == 2:
        plt.plot(x[k-1],y[k-1],color=cmap(k), marker='.', markersize=1.9)
    elif isLog == 3:
        plt.plot(x[k],noLog_dataset[k],color=cmap(k), marker='.', markersize=1.9)
    else:
        plt.plot(x[k],y[k],color=cmap(k), marker='.', markersize=1.9)

x_min = min(x)
x_max = max(x)
y_min = min(y)
y_max = max(y)

if isLog == 3:
    log_min = min(noLog_dataset)
    log_max = max(noLog_dataset)


if isLog == 1:
    plt.yscale('log')
    plt.xlim(left=-0.0053 * max(x))
    plt.xlim(right= 1.01 * max(x))
    plt.ylim(bottom=1-0.0075 * max(y))
    # log margins
    y_margin_log = (math.log10(y_max) - math.log10(y_min)) * 0.03
    plt.ylim(top=10 ** (math.log10(y_max) + y_margin_log))
elif isLog == 2:
    plt.yscale('log')
    plt.xscale('log')
    # more log margins
    x_margin_log = (math.log10(x_max) - math.log10(x_min)) * 0.02
    plt.xlim(left=-0.0053 * max(x))
    plt.xlim(right=10 ** (math.log10(x_max) + x_margin_log))

    y_margin_log = (math.log10(y_max) - math.log10(y_min)) * 0.03
    plt.ylim(bottom=1-0.0075 * max(y))
    plt.ylim(top=10 ** (math.log10(y_max) + y_margin_log))
elif isLog == 3:
    plt.xlim(left=-0.0053 * max(x))
    plt.xlim(right= 1.01 * max(x))
    plt.ylim(bottom=0.98 * log_min - 1)
    plt.ylim(top=1.02 * log_max)
else:
    plt.xlim(left=-0.0053 * max(x))
    plt.xlim(right= 1.01 * max(x))
    if height != 0:
        plt.ylim(top=height)
        plt.ylim(bottom=1-0.0075 * height)
    else:
        plt.ylim(bottom=1-0.0075 * max(y))
        plt.ylim(top=1.02 * max(y))

txt="Made by Chicky"
#first num is percent on x axis, second is y
plt.figtext(0.075, 0.065, txt, wrap=True, horizontalalignment='center', fontsize=8, color="grey")

plt.tight_layout()

dpi = 500
plt.subplots_adjust(left=0.15, bottom=0.1)


# Save the figure in the specified directory
filename = os.path.join(output_directory, 'graph-single.png')
plt.savefig(filename, dpi=dpi)