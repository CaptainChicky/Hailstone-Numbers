import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

import numpy as np
import os
import argparse

# Create a directory for saving figures if it doesn't exist
output_directory = 'generated'
os.makedirs(output_directory, exist_ok=True)

plotlist = []

path_lengths = []

# Create the argument parser
parser = argparse.ArgumentParser(description='Driver Program')

# Add an optional option for the plot argument
parser.add_argument('-p', '--plot', help='List of values for plotting', default='list(range(1, 1001))')

# Parse the command-line arguments
args = parser.parse_args()

# Parse the plot argument into a list
plotlist = eval(args.plot)


def get_path_length(n):
    count = 1
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1
        count += 1
    return count

for seed in plotlist:
    path_length = get_path_length(seed)
    path_lengths.append(path_length)

def get_cmap(n, name='hsv'):
    return plt.cm.get_cmap(name, n)

# Adjust the bin edges by adding an offset of 0.5
# the -2 and +2 is because the range function isn't inclusive so we have to grab the edges manually
bins = [edge + 0.5 for edge in range(min(path_lengths) - 2, max(path_lengths) + 2)]

# Create the invisible histogram
bin_heights, bin_edges, _ = plt.hist(path_lengths, bins=bins, alpha=0)

# Get the pixel size of each bin
fig = plt.gcf()
fig_size = fig.get_size_inches() * fig.dpi
bin_pixel_sizes = (fig_size[0] / len(bin_edges)) * 0.03  # 3% of the bin's pixel size
print("Edge size: " + str(bin_pixel_sizes))

plt.close()  # Close the previous figure

# Calculate the range of all the bins
bin_range = max(path_lengths) - min(path_lengths)

# Calculate the desired border width as 5% of the bin range
border_width = bin_range * 0.02

plt.xlim(left=min(path_lengths) - border_width)
plt.xlim(right=max(path_lengths) + border_width)

PLlength = len(plotlist)
cmap = get_cmap(PLlength + 1)

# Create a new figure with adjusted figsize
fig, ax = plt.subplots(figsize=(10, 5))

# Calculate the histogram values for each bin
hist, bin_edges = np.histogram(path_lengths, bins=bins)

# Assign a different color to each bin
for i in range(len(bins) - 1):
    color = cmap(i / (len(bins) - 1))  # Normalize bin index to range [0, 1]
    ax.bar(bin_edges[i], hist[i], width=bin_edges[i + 1] - bin_edges[i], color=color, edgecolor='black', linewidth=bin_pixel_sizes, alpha=0.7)

plt.xlabel('Path length')
plt.ylabel('Frequency')
plt.title('Hailstone Path Lengths')

txt = "Made by Chicky"
plt.figtext(0.075, 0.065, txt, wrap=True, horizontalalignment='center', fontsize=8, color="grey")

plt.tight_layout()

dpi = 500
plt.subplots_adjust(left=0.15, bottom=0.1)

# Save the figure in the specified directory
filename = os.path.join(output_directory, 'pathLen.png')
plt.savefig(filename, dpi=dpi)