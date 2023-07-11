import math
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

# fix and definetely use log plot later lmao
plt.xlabel('Seed value')
plt.ylabel('Maximum value')
plt.title('Hailstone maximums')
plt.figure(figsize=(5, 20))

maxlist = []

plotlist = []

isLog = 0


PLlength = len(plotlist)

def plot(n, color):
    Arr = [n]
    originalN = n
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = ((n * 3) + 1)
        Arr.append(n)

    x = originalN
    y = max(Arr)

    # for debug, remove later
    print(x, y)
    
    maxlist.append(y)

    plt.plot(x, y, '.', color=color)

def plotall():
    for k in range(PLlength):
        plot(plotlist[k], 'blue')

    # margins with this is more complicated
    # we calculate the margins as a percentage of the total range
    x_min = min(plotlist)
    x_max = max(plotlist)
    y_min = min(maxlist)
    y_max = max(maxlist)

    x_margin = 0.02 * (x_max - x_min)
    y_margin = 0.03 * (y_max - y_min)

    if isLog == 1:
        plt.yscale('log')
        plt.xlim(left=x_min - x_margin)
        plt.xlim(right=x_max + x_margin)
        plt.ylim(bottom=y_min - y_margin)
        # log margins bruh
        y_margin_log = (math.log10(y_max) - math.log10(y_min)) * 0.03
        if y_min == y_max:
            y_margin_log = 0.03
        plt.ylim(top=10 ** (math.log10(y_max) + y_margin_log))
    elif isLog == 2:
        plt.xscale('log')
        plt.yscale('log')
        # more log margins
        x_margin_log = (math.log10(x_max) - math.log10(x_min)) * 0.02
        plt.xlim(left=x_min - x_margin)
        plt.xlim(right=10 ** (math.log10(x_max) + x_margin_log))

        y_margin_log = (math.log10(y_max) - math.log10(y_min)) * 0.03
        if y_min == y_max:
            y_margin_log = 0.03
        plt.ylim(bottom=y_min - y_margin)
        plt.ylim(top=10 ** (math.log10(y_max) + y_margin_log))
    else:
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
 
plt.subplots_adjust(left=0.15, bottom=0.1)

plt.savefig("maxgraph.pdf", format='pdf')
