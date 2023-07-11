import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

plt.xlabel('Path length')
plt.ylabel('Frequency')
plt.title('Hailstone Path Lengths')

plotlist = list(range(1, 1001))

path_lengths = []

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

# Adjust the bin edges by adding an offset of 0.5
# the -2 and +2 is because the range function isn't inclusive so we have to grab the edges manually
bins = [edge + 0.5 for edge in range(min(path_lengths) - 2, max(path_lengths) + 2)]

# Create the invisible histogram
bin_heights, bin_edges, _ = plt.hist(path_lengths, bins=bins, alpha=0)

# Get the pixel size of each bin
fig = plt.gcf()
fig_size = fig.get_size_inches() * fig.dpi
bin_pixel_sizes = (fig_size[0] / len(bin_edges)) * 0.03  # 3% of the bin's pixel size
print(bin_pixel_sizes)

plt.close()  # Close the previous figure


# Calculate the range of all the bins
bin_range = max(path_lengths) - min(path_lengths)

# Calculate the desired border width as 5% of the bin range
border_width = bin_range * 0.02

plt.xlim(left=min(path_lengths) - border_width)
plt.xlim(right=max(path_lengths) + border_width)


# create the actual histogram
plt.hist(path_lengths, bins=bins, color='blue', edgecolor='black', linewidth=bin_pixel_sizes, alpha=0.7)


txt = "Made by Chicky"
plt.figtext(0.05, 0.03, txt, wrap=True, horizontalalignment='center', fontsize=8, color="grey")

plt.tight_layout()

dpi = 500
plt.subplots_adjust(left=0.15, bottom=0.1)

plt.savefig('pathLengthHistogram.png', dpi=dpi)