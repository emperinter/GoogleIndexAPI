from oauth2client.service_account import ServiceAccountCredentials
import httplib2
import requests as req
from bs4 import BeautifulSoup

def index(url):
    SCOPES = [ "https://www.googleapis.com/auth/indexing" ]
    ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"

    # service_account_file.json is the private key that you created for your service account.
    JSON_KEY_FILE = "your-index-api.json"

    credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE, scopes=SCOPES)

    http = credentials.authorize(httplib2.Http())

    # Define contents here as a JSON string.
    # This example shows a simple update request.
    # Other types of requests are described in the next step.

    content = "{\"url\": \"%s\", \"type\": \"URL_UPDATED\"}" % url

    response, content = http.request(ENDPOINT, method="POST", body=content)
    return response

all_link = []
origin_rul = 'https://your-sitemap-url.xml'
r = req.get(origin_rul)
bs = BeautifulSoup(r.content, 'html.parser') #解析网页
hyperlink = bs.find_all(name = 'loc')  # 标签是否要附加信息，如要附加。去BeautifulSoup查看文档，我目前测试过attrs={'alt' : ''}
for h in hyperlink:
    hh = h.string
    all_link.append(hh)

all_link.reverse()

sent = []

# 打开文件
fo = open("sent.txt", "r")
print("文件名为: ", fo.name)

for line in fo.readlines():  # 依次读取每行
    line = line.strip()  # 去掉每行头尾空白
    sent.append(line)  # 将每行的内容添加到列表中
    print("读取的数据为: %s" % (line))

# 关闭文件
fo.close()

for link in all_link:
    if link not in sent:
        print(link)
        res = index(link)
        if res.get("status") == "200":
            with open("sent.txt", 'a+') as f:
                f.write(str(link) + '\n')  # 加\n换行显示
        else:
            print(res)
            break
    else:
        print(str(link) + '已经发送过了')
        continue