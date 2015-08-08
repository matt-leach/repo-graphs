from api import get_commit_shas, get_commit, Commit
from matplotlib import pyplot as plt


def plot(username, repo):
    commits = get_commit_shas(username, repo)
    y = []
    x = []
    total_loc = 0
    count = 0
    for sha in commits:
        count += 1
        c = Commit(get_commit(username, repo, sha))
        total_loc += c.net_loc
        x.append(count)
        y.append(total_loc)

    plt.plot(x, y)
    plt.show()
