"""Length histogram driver.
Versions: reg, prime, rainbow
"""

import sys
import os
import argparse

import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from utils import is_prime, get_cmap, setup_output, save_figure

import matplotlib.pyplot as plt


output_dir = setup_output()

parser = argparse.ArgumentParser(description="Length Histogram Driver")
parser.add_argument(
    "-v", "--version", required=True, choices=["reg", "prime", "rainbow"]
)
parser.add_argument("-p", "--plot", default="list(range(1, 1001))")
args = parser.parse_args()

version = args.version
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


path_lengths = []
prime_path_lengths = []

for seed in plotlist:
    path_length = get_path_length(seed)
    path_lengths.append(path_length)
    if version == "prime" and is_prime(seed):
        prime_path_lengths.append(path_length)

# Adjust the bin edges by adding an offset of 0.5
# the -2 and +2 is because the range function isn't inclusive so we have to grab the edges manually
bins = [edge + 0.5 for edge in range(min(path_lengths) - 2, max(path_lengths) + 2)]

# Create the invisible histogram to get bin pixel sizes
bin_heights, bin_edges, _ = plt.hist(path_lengths, bins=bins, alpha=0)

# Get the pixel size of each bin
fig = plt.gcf()
fig_size = fig.get_size_inches() * fig.dpi
bin_pixel_sizes = (fig_size[0] / len(bin_edges)) * 0.03  # 3% of the bin's pixel size
print("Edge size: " + str(bin_pixel_sizes))

plt.close()  # Close the previous figure

# Calculate border width
bin_range = max(path_lengths) - min(path_lengths)
border_width = bin_range * 0.02

if version == "rainbow":
    PLlength = len(plotlist)
    cmap = get_cmap(PLlength + 1)

    fig, ax = plt.subplots(figsize=(10, 5))

    plt.xlim(left=min(path_lengths) - border_width)
    plt.xlim(right=max(path_lengths) + border_width)

    # Calculate the histogram values for each bin
    hist, bin_edges = np.histogram(path_lengths, bins=bins)

    # Assign a different color to each bin
    for i in range(len(bins) - 1):
        color = cmap(i / (len(bins) - 1))  # Normalize bin index to range [0, 1]
        ax.bar(
            bin_edges[i],
            hist[i],
            width=bin_edges[i + 1] - bin_edges[i],
            color=color,
            edgecolor="black",
            linewidth=bin_pixel_sizes,
            alpha=0.7,
        )
else:
    plt.figure(figsize=(10, 5))

    plt.xlim(left=min(path_lengths) - border_width)
    plt.xlim(right=max(path_lengths) + border_width)

    # create the actual histogram
    plt.hist(
        path_lengths,
        bins=bins,
        color="blue",
        edgecolor="black",
        linewidth=bin_pixel_sizes,
        alpha=0.7,
    )

    if version == "prime":
        plt.hist(
            prime_path_lengths,
            bins=bins,
            color="red",
            edgecolor="black",
            linewidth=bin_pixel_sizes,
            alpha=0.7,
        )

plt.xlabel("Path length")
plt.ylabel("Frequency")
plt.title("Hailstone Path Lengths")

save_figure(os.path.join(output_dir, "pathLen.png"))
