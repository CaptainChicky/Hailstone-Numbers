import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

# fix and definetely use log plot later lmao
plt.xlabel('Seed value')
plt.ylabel('Maximum value')
plt.title('Hailstone maximums')
plt.figure(figsize=(6, 600))

maxlist = []

plotlist = []

i=1

while i <= 10000:
    plotlist.append(i)
    i += 1

PLlength = len(plotlist)

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

    print(x, y)
    
    maxlist.append(y)

    plt.plot(x, y, '.', color=color)

def plotall():
    color = "blue"
    tmp = []
    for k in range(PLlength):
        if isPrime(plotlist[k]):
            tmp.append(plotlist[k])
        else:
            plot(plotlist[k], color)
    
    for j in range(len(tmp)):
        plot(tmp[j], "red")

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
    plt.ylim(bottom=0)
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

plt.savefig('maxgraph.pdf', format='pdf')
