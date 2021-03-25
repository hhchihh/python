import requests
import json
import os
import random
import time

def download(illusts_url):
    time.sleep(random.randint(1, 5))
    response = requests.get(illusts_url, headers=header)
    illusts_text = json.loads(response.text)["body"]
    for img_original in illusts_text:
        link = img_original["urls"]["original"]
        sub = link.split(".")[-1]
        if sub in reserver:
            links = requests.get(link, headers=header)
            fn = dn + link.split("/")[-1]
            f = open(fn, "wb")
            f.write(links.content)
            f.close()
    print(link)


header = {
    "referer": "https://www.pixiv.net/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",
    "cookie": ""
}

user_id = 2539925
user_url = "https://www.pixiv.net/ajax/user/" + str(user_id)

illusts_id_list = []

dn = "pixiv/" + str(user_id) + "/"
if not os.path.exists(dn):
    os.makedirs(dn)

reserver = ["jpg", "jpeg", "png", "gif"]

img_id = "https://www.pixiv.net/ajax/user/" + str(user_id) + "/profile/all?lang=zh_tw"
response = requests.get(img_id, headers=header)
img_id_text = json.loads(response.text)["body"]["illusts"]
for illusts_id in img_id_text:
    illusts_id_list.append(illusts_id)

i = 0

while True:
    illusts_url = "https://www.pixiv.net/ajax/illust/" + illusts_id_list[i] + "/pages?lang=zh_tw"

    time.sleep(random.randint(1, 5))

    if illusts_id_list[-1] != illusts_id_list[i]:
        print(illusts_url)
        i = i + 1
    elif illusts_id_list[-1] == illusts_id_list[i]:
        download(illusts_url)
        print(illusts_url)
        break
    download(illusts_url)
    print("-" * 30)

