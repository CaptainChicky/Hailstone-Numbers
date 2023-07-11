import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import os
# make choice to prioritize primes or not

# Create a directory for saving figures if it doesn't exist
output_directory = 'generated'
os.makedirs(output_directory, exist_ok=True)

plt.xlabel('Seed number')
plt.ylabel('Number of iterations')
plt.title('Hailstone path length')

def isPrime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
    

maxlist = []

plotlist = list(range(1, 1001))


PLlength = len(plotlist)

def PlotSeed(n, color):
    # count starts at 1 because the seed is part of the sequence
    count = 1
    originalN = n
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = ((n * 3) + 1)
        count += 1

    maxlist.append(count)
    plt.plot(originalN, count, '.', color=color)

def plotall():
    color = "blue"
    tmp = []
    for k in range(PLlength):
        if isPrime(plotlist[k]):
            tmp.append(plotlist[k])
        else:
            PlotSeed(plotlist[k], color)
    
    for j in range(len(tmp)):
        PlotSeed(tmp[j], "red")

    # margins with this is more complicated
    # we calculate the margins as a percentage of the total range
    x_min = min(plotlist)
    x_max = max(plotlist)
    y_min = min(maxlist)
    y_max = max(maxlist)

    x_margin = 0.02 * (x_max - x_min)
    y_margin = 0.03 * (y_max - y_min)

    plt.xlim(left=x_min - x_margin)
    plt.xlim(right=x_max + x_margin)
    plt.ylim(bottom=y_min - y_margin)
    plt.ylim(top=y_max + y_margin)

            
        

plotall()

txt = "Made by Chicky"
#first num is percent on x axis, second is y
plt.figtext(0.05,
            0.03,
            txt,
            wrap=True,
            horizontalalignment='center',
            fontsize=8,
            color="grey")

plt.tight_layout()

dpi = 500
plt.subplots_adjust(left=0.15, bottom=0.1)

# Save the figure in the specified directory
filename = os.path.join(output_directory, 'seedLen.png')
plt.savefig(filename, dpi=dpi)