> 最近搞了一站点提交给sitemap给search console，结果一直显示**无法读取此站点地图**，sitemap多次核查是没有问题的，百度和bing等等收录正常，自己写了一个simemap生成器仍是如此。后来发现Google也是只是API提交的就尝试搞了一下。

- [参考: https://developers.google.com/search/apis/indexing-api/v3/quickstart?hl=zh-cn](https://developers.google.com/search/apis/indexing-api/v3/quickstart?hl=zh-cn)

- 注册感觉没啥可说的按上面教程来就行，注意给授权就行。

- requirements.txt

```txt
beautifulsoup4==4.11.1
bs4==0.0.1
cachetools==5.2.0
certifi==2022.6.15
charset-normalizer==2.1.0
google-api-core==2.8.2
google-api-python-client==2.55.0
google-auth-httplib2==0.1.0
google-auth==2.9.1
googleapis-common-protos==1.56.4
httplib2==0.20.4
idna==3.3
oauth2client==4.1.3
pip==21.3.1
protobuf==4.21.4
pyasn1-modules==0.2.8
pyasn1==0.4.8
pyparsing==3.0.9
requests==2.28.1
rsa==4.9
setuptools==60.2.0
six==1.16.0
soupsieve==2.3.2.post1
uritemplate==4.1.1
urllib3==1.26.11
wheel==0.37.1
```

- 按照requirements.txt安装

```shell
pip install -r requirements.txt
```

- 注意配置修改代码与自己相关的json验证文件和网站地图文件的路径

- 运行

```shell
python3 main.py
```