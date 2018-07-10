import json
import requests
from datetime import datetime

#f = open('github_file.txt')
#line = f.readline()

lines = []
with open('github_file.txt', 'r') as f:
    for lineItem in f:
        lines.append(lineItem.rstrip('\r\n'))

#mystring = mystring.replace('\n', ' ').replace('\r', '')
print("Array : %s" % lines)

i = 0
while i < len(lines):
    print("Repo Items : " + lines[i])
    git_api = "https://api.github.com/repos/" + lines[i]


    print('Git API: ' + git_api)
    repo_response = requests.get(git_api)
    commit_response = requests.get((git_api+'/commits').strip())

    print('Headers: %s' % repo_response.headers)
    print(commit_response.content)
    if lines[i] == '':
        print('Unable to connect to repository or Invalid repository')
    else:
        responseItem = json.loads(repo_response.content)
        print(responseItem)
        c_responseItem = json.loads(commit_response.content)
        convert_date = datetime.strptime(c_responseItem[0]['commit']['committer']['date'], '%Y-%m-%dT%H:%M:%SZ') \
            .strftime('%d-%b-%Y')

        print('Repository Name: %s' % responseItem['name'])
        print('Clone URL: %s' % responseItem['clone_url'])
        print('Latest Commit Date: %s' % convert_date)
        print('Name of the latest author: %s' % c_responseItem[0]['commit']['author']['name'])


    i += 1

f.close()
