# encoding: utf-8
__author__ = 'zhanghe'

import numpy as np
import matplotlib.pyplot as plt

N = 5
menMeans = (20, 35, 30, 35, 27)
# menStd = (2, 3, 4, 1, 2)
menStd = (1, 1, 1, 1, 1)

ind = np.arange(N)  # the x locations for the groups
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rect_1 = ax.bar(ind, menMeans, width, color='r', yerr=menStd)

womenMeans = (25, 32, 34, 20, 25)
# womenStd = (3, 5, 2, 3, 3)
womenStd = (1, 1, 1, 1, 1)
rect_2 = ax.bar(ind + width, womenMeans, width, color='y', yerr=womenStd)

# add some
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(ind + width)
ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))

ax.legend((rect_1[0], rect_2[0]), ('Men', 'Women'))


def auto_label(rect_bar):
    # attach some text labels
    for rect in rect_bar:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height, '%d' % int(height),
                ha='center', va='bottom')


auto_label(rect_1)
auto_label(rect_2)

plt.show()