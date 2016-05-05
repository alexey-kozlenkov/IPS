__author__ = 'Alexey'
from matplotlib import pyplot as  plot


def plot_pair(x, y1, y2, filename, ylim, title=None, color1='skyblue', color2='green', label1='y1', label2='y2'):
    plot.plot(x, y1, color=color1, label=label1)
    plot.plot(x, y2, color=color2, label=label2)
    plot.ylim(-ylim, ylim)
    plot.title(title)
    plot.legend()
    plot.savefig('graphics/{}.png'.format(filename))
    plot.clf()
