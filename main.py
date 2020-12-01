from utils import get_repos
from sys import exit
from subprocess import Popen

git_list = []
new_git_urls = []
new_html_urls = []
forked_url_list = []

html_urls = get_repos.get_repos()
if not html_urls:
    exit("Debugging")

for each_url in html_urls:
    if 'git://' in each_url:
        git_list.append(each_url)
        continue
    new_html_urls.append(each_url)

for each_git_url in git_list:
    remove_git = each_git_url.replace('git://', 'https://')
    new_git_urls.append(remove_git)

descriptions = get_repos.return_descriptions()
names = get_repos.return_names()
branches = get_repos.return_branch_list()
authors = get_repos.return_authors()

item_index = 0
for item in new_git_urls:
    replace_this = "/" + names[item_index] + "/"
    forked_url = item.replace(replace_this, 'mehtaarn000-readmebot')
    forked_url_list.append(forked_url)

index = 0
for i in names:
    Popen("sh submit_prs.sh {} {} {} {} {} {}".format(new_git_urls[0], forked_url_list[0], i, descriptions[0], branches[0], authors[0]))
    index += 1