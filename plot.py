from api import get_commit_shas, get_commit, Commit
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from collections import Counter

# Thanks http://rforwork.info/2012/05/18/bar-graph-colours-that-work-well/
COLORS = ['#727272', '#f1595f', '#79c36a', '#599ad3', '#f9a65a', '#9e66ab', '#cd7058', '#d77fb3']


def plot(username, repo):
    commits = get_commit_shas(username, repo)
    loc_count = Counter()
    ys = {}
    x = []

    count = 0
    for sha in commits:
        count += 1
        c = Commit(get_commit(username, repo, sha))
        x.append(count)

        # for each extension in the commit, add it to loc_count
        for ext, val in c.loc.items():
            loc_count[ext] += val
            if ext not in ys:
                ys[ext] = [0] * (count - 1)  # Fill with 0s

        # For each extension we've seen append the current value to ys
        for ext, val in loc_count.items():
            ys[ext].append(val)

    # stack ys appropriately
    y = np.row_stack(ys.values())
    y_stack = np.cumsum(y, axis=0)
    fig = plt.figure()
    ax1 = fig.add_subplot(111)

    legend_patches = []
    for val, ext in enumerate(ys.keys()):
        color = COLORS[val % len(COLORS)]
        if val == 0:
            ax1.fill_between(x, 0, y_stack[0, :], facecolor=color)
        ax1.fill_between(x, y_stack[val-1, :], y_stack[val, :], facecolor=color)

        legend_patches.append(mpatches.Patch(color=color, label=ext))

    plt.legend(handles=legend_patches)

    plt.show()


if __name__ == '__main__':
    import sys
    plot(sys.argv[1], sys.argv[2])
