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
  2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 
  31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 
  61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 
  91, 92, 93, 94, 95, 96, 97, 98, 99, 100
]

PLlength = len(plotlist)

def plot(n, color):
    # count starts at 0 because the beginning number is not an iteration
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
    plt.ylim(bottom=1-0.0075 * max(maxlist[1]))
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