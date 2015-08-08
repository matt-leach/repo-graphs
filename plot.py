from api import get_commit_shas, get_commit, Commit
from bokeh.plotting import figure, output_file, show


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

    output_file('chart.html', title='Basic Repository LOC trend')

    p = figure(x_axis_label='commit count', y_axis_label='LOC')
    p.line(x, y)
    show(p)
