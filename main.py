import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

plt.xlabel('Number of iterations')
plt.ylabel('Number value')
plt.title('Hailstone numbers comparison')

def get_cmap(n, name='hsv'):
    return plt.cm.get_cmap(name, n)

maxlist = [[], []]

plotlist = [
  163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 27
]

PLlength = len(plotlist)

def plot(n, color):
    count = 0
    Arr = [[0], [n]]
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = ((n * 3) + 1)
        count += 1
        Arr[0].insert(count, count)
        Arr[1].insert(count, n)

    x = Arr[0]
    y = Arr[1]

    plt.plot(x, y, ',-', linewidth=0.9, color=color)

    maxlist[0].append(max(x))
    maxlist[1].append(max(y))

def plotall(colorparse):
    cmap = get_cmap(colorparse + 1)
  
    for k in range(PLlength):
        plot(plotlist[k], cmap(k + 1))

    plt.xlim(left=-0.0053 * max(maxlist[0]))
    plt.xlim(right=1.01 * max(maxlist[0]))
    plt.ylim(bottom=-0.0053 * max(maxlist[1]))
    plt.ylim(top=1.02 * max(maxlist[1]))

plotall(PLlength)

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

plt.savefig('graph.png', dpi=dpi)