from api import get_commit_shas, get_commit, Commit
from matplotlib import pyplot as plt
import numpy as np


def plot(username, repo):
    commits = get_commit_shas(username, repo)
    py = []
    html = []
    x = []

    # Hard coding for now
    py_loc = 0
    html_loc = 0

    count = 0
    for sha in commits:
        count += 1
        c = Commit(get_commit(username, repo, sha))
        x.append(count)
        py_loc += c.loc.get('py', 0)
        html_loc += c.loc.get('html', 0)
        html.append(html_loc)
        py.append(py_loc)

    y = np.row_stack((py, html))
    y_stack = np.cumsum(y, axis=0)
    fig = plt.figure()
    ax1 = fig.add_subplot(111)

    ax1.fill_between(x, 0, y_stack[0, :], facecolor='#ababab')
    ax1.fill_between(x, y_stack[0, :], y_stack[1, :], facecolor='#12efef')

    plt.show()


if __name__ == '__main__':
    import sys
    plot(sys.argv[1], sys.argv[2])
