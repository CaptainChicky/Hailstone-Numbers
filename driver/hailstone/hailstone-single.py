import matplotlib as mpl 
mpl.use('Agg')
import matplotlib.pyplot as plt 
n = 97
plt.xlabel('Number of iterations')
plt.ylabel('Number value')
plt.title('Hailstone numbers: number %i' % n)

def get_cmap(n, name='hsv'):
    '''Returns a function that maps each index in 0, 1, ..., n-1 to a distinct 
    RGB color; the keyword argument name must be a standard mpl colormap name.'''
    return plt.cm.get_cmap(name, n)

# conut starts at 0 because the seed is not an iteration
count = 0
Arr = [[0],[n]]

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
plt.plot(x, y, 'k,-', linewidth=0.9)

cmap = get_cmap(len(x))

for k in range(count + 1):
  plt.plot(x[k],y[k],color=cmap(k), marker='.', markersize=1.9)

plt.xlim(left=-0.0053 * max(x))
plt.xlim(right= 1.01 * max(x))
plt.ylim(bottom=1-0.0075 * max(y))
plt.ylim(top=1.02 * max(y))

txt="Made by Chicky"
#first num is percent on x axis, second is y
plt.figtext(0.05, 0.03, txt, wrap=True, horizontalalignment='center', fontsize=8, color="grey")

plt.tight_layout()

dpi = 500
plt.subplots_adjust(left=0.15, bottom=0.1)

plt.savefig('graph-single.png', dpi=dpi)