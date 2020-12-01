from requests import get
from datetime import datetime, timedelta

def get_repos():
    #Taking repos from today will return none
    int_yesterday = datetime.now() - timedelta(days=1)
    yesterday = int_yesterday.strftime('%Y-%m-%d')
    json_this = 'https://api.github.com/search/repositories?q=pushed:%3E' + yesterday + '+stars:%3C=1'
    response = get(json_this).json()
    global desc_list, name_list, default_branch_list, author_list, license_list
    pr_list = []
    desc_list = []
    name_list = []
    default_branch_list = []
    author_list = []
    license_list = []

    total_count = response['total_count'] + 1
    for i in range(0, total_count):
        try:
            if response['items'][i]['description'] == None or response['items'][i]['description'] == "None":
                booldescription = False
            else:
                booldescription = True

            #Logic to find the readme file
            #We don't use the github api here for rate limits
            READMEFileExists = True
            README_url = 'https://raw.githubusercontent.com/' + response['items'][i]['full_name'] + '/' + response['items'][i]['default_branch'] + '/README.md'
            README = get(README_url)
            if README.text == '404: Not Found':
                readme_url = 'https://raw.githubusercontent.com/' + response['items'][i]['full_name'] + '/' + response['items'][i]['default_branch'] + '/readme.md'
                readme = get(readme_url)
                if readme.text == "404: Not Found":
                    readmetxt_url = 'https://raw.githubusercontent.com/' + response['items'][i]['full_name'] + '/' + response['items'][i]['default_branch'] + '/readme.txt'
                    readmetxt = get(readmetxt_url)
                    if readmetxt.text == "404: Not Found":
                        ReadMemd_url = 'https://raw.githubusercontent.com/' + response['items'][i]['full_name'] + '/' + response['items'][i]['default_branch'] + '/ReadMe.md'
                        ReadMemd = get(ReadMemd_url)
                        if ReadMemd.text == "404: Not Found":
                            READMEFileExists = False
            
            #Store websites without readmes and with descriptions
            if booldescription and not READMEFileExists:
                pr_list.append(response['items'][i]['html_url'])
                pr_list.append(response['items'][i]['git_url'])
                desc_list.append(response['items'][i]['description'])
                name_list.append(response['items'][i]['name'])
                default_branch_list.append(response['items'][i]['default_branch'])
                author_list.append(response['items'][i]['owner']['login'])
            

        except:
            pass
    return pr_list
def return_descriptions():
    return desc_list
def return_names():
    return name_list
def return_branch_list():
    return default_branch_list
def return_authors():
    return author_list
print(get_repos())
