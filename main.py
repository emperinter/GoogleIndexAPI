from google.oauth2 import service_account
from google.auth.transport.requests import Request
import requests as req
from bs4 import BeautifulSoup
import json

def index(url):
    SCOPES = ["https://www.googleapis.com/auth/indexing"]
    ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"

    # service_account_file.json is the private key that you created for your service account.
    JSON_KEY_FILE = "your-auth-key.json"

    credentials = service_account.Credentials.from_service_account_file(JSON_KEY_FILE, scopes=SCOPES)
    credentials.refresh(Request())

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {credentials.token}'
    }
    data = {
        "url": url,
        "type": "URL_UPDATED"
    }
    response = req.post(ENDPOINT, headers=headers, data=json.dumps(data))
    return response

all_link = []
origin_url = 'https://wordcloudmaster.com/post_tag-sitemap11.xml'
r = req.get(origin_url)
bs = BeautifulSoup(r.content, 'lxml')
hyperlink = bs.find_all(name='loc')
for h in hyperlink:
    hh = h.string
    all_link.append(hh)

all_link.reverse()

sent = []

with open("sent.txt", "r") as fo:
    print("file name: ", fo.name)
    for line in fo.readlines():
        line = line.strip()
        sent.append(line)
        print("url: %s" % (line))

for link in all_link:
    if link not in sent:
        print(link)
        res = index(link)
        if res.status_code == 200:
            with open("sent.txt", 'a+') as f:
                f.write(str(link) + '\n')
        else:
            print(res.text)
            break
    else:
        print(str(link) + 'has posted!')
        continue