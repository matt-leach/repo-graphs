import requests
import secret


GITHUB_API = 'https://api.github.com'


class Commit(object):

    def __init__(self, data):
        # data is the json from accessing the github api
        self.date = data['commit']['author']['date']

        files = data['files']
        exts = {}
        for f in files:
            net_loc = f['additions'] - f['deletions']
            ext = f['filename'].split('.')[-1]
            if ext in exts.keys():
                exts[ext] = net_loc
            else:
                exts[ext] += net_loc

        self.loc = exts


class GithubAPI(object):
    access_token = secret.TOKEN
    base_url = 'https://api.github.com'

    @classmethod
    def get(self, url):
        r = requests.get(self.base_url + url + '?access_token={}'.format(self.access_token))
        return r


def get_commit_shas(username, repo):
    r = GithubAPI.get('/repos/{}/{}/commits'.format(username, repo))
    commits = r.json()
    print commits
    return [c['sha'] for c in commits]


def get_commit(username, repo, sha):
    r = GithubAPI.get('/repos/{}/{}/commits/{}'.format(username, repo, sha))
    commit = r.json()
    return commit


def print_commits_data(username, repo):
    commits = get_commit_shas(username, repo)
    for sha in commits:
        c = Commit(get_commit(username, repo, sha))
        print c.date, c.net_loc
