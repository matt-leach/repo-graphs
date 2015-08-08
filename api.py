import requests


GITHUB_API = 'https://api.github.com'


class Commit(object):

    def __init__(self, data):
        # data is the json from accessing the github api
        self.date = data['commit']['author']['date']
        self.net_loc = sum(f['additions'] - f['deletions'] for f in data['files'])


def get_commit_shas(username, repo):
    r = requests.get(GITHUB_API + '/repos/{}/{}/commits'.format(username, repo))
    commits = r.json()
    return [c['sha'] for c in commits]


def get_commit(username, repo, sha):
    r = requests.get(GITHUB_API + '/repos/{}/{}/commits/{}'.format(username, repo, sha))
    commit = r.json()
    return commit


def print_commits_data(username, repo):
    commits = get_commit_shas(username, repo)
    for sha in commits:
        c = Commit(get_commit(username, repo, sha))
        print c.date, c.net_loc
