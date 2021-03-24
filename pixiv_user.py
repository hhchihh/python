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
    "cookie": "__cfduid=d0046ea83fa445e48524a419c650f6d911611986212; first_visit_datetime_pc=2021-01-30+14%3A56%3A53; yuid_b=OJA5mEQ; p_ab_id=7; p_ab_id_2=6; p_ab_d_id=1624885670; device_token=5cedf9212a360913fec79c74f2b95608; c_type=29; a_type=0; b_type=1; login_ever=yes; PHPSESSID=13475253_CwXXoBRxsWJLeFvQOkW8kIZ6XsKYiLNr; privacy_policy_agreement=0; __cf_bm=4f2f3c3223512762ca61a5de98090642db93be14-1614252284-1800-AbCuoDno/oaZLTSEvEP4Kh68G2WxHKyAZcyF6ytHjUwwDibug5ROS6oEQg4ZyOIPZ5cDnVLpJbRf1oGGf8v6Qc48icWyIS5eTzQw1yS/4Aa6; tag_view_ranking=0xsDLqCEW6~g-aCwpfKBO~yPNaP3JSNF~kGYw4gQ11Z~4ZEPYJhfGu~RTJMXD26Ak~KN7uxuR89w~BU9SQkS-zU~NpsIVvS-GF~sLQ8trav9X~ZEVqmDpghJ~QaiOjmwQnI~_bpS_tf07g~eMVo52EJIw~ZTBAtZUDtQ~pPd467eyWs~i83OPEGrYw~azESOjmQSV~Lt-oEicbBr~RcahSSzeRf~sQC4pGQx9E~jfnUZgnpFl~3gc3uGrU1V~gpglyfLkWs~XcIpinmcSt~GNcgbuT3T-~AkdtNEMh8i~NlYn1jwtuG~ldWX9tpU0G~WnuJ28BliV~yRltuBngJJ~Yl_HsRLqlh~THI8rtfzKo~n_QeEntwnh~HY55MqmzzQ~14-vQ9R9t1~jk9IzfjZ6n~0PxqSkQsXK~pZiEPnRTum~uFigYBR0MO~JXj60bPp4r~ZtdTKsZ90-~9V46Zz_N_N~iu2YDB5Fqp~HBuswNf19E~K6JjooB-Ba~uGW7Tzhi1A~Y9RmscwNAS~5oPIfUbtd6~KOnmT1ndWG~y3NlVImyly~cbmDKjZf9z~Bd2L9ZBE8q~_pwIgrV8TB~Te-Gu2wMLd~4QveACRzn3~-Mi31N3WSk~pnCQRVigpy~ZZltVrbyeV~BLo4YIul9L~VeNYv5seZ_~FfFuZRxXNV~vnydhfA2BB~rsb55I7upx~Ib0YGS-7FI~UOfaO1Dqq-~C1zxl77dvd~bT9-tCh-Tu~aMSPvw-ONW~Sjwi7bh6-s~lrW2UGRlTF~O2tFVkTz_9~7d8LZB8dpY~TBLP3caQ0S~NpVw-NEOOh~W4_X_Af3yY~4vfV_M7vzB~z3I4S1dEHE~vYBPiUXRIF~vSWEvTeZc6~1mnqYqUwL7~UFyUgz2n2m~4LfBhWYcxv~FX4bTIsxzb~3gjIvNWGCE~skx_-I2o4Y~9Nx-lbSnZF~AI_aJCDFn0~cPZorjmaDw~-MuiEJf_Sr~QdBk9VtgiK~FqVQndhufZ~4Q1GaIiU6i~iFoujbj8RG~yS9cDC8XJc~JN-XguT8PU~1P--lTQMwI~engSCj5XFq~YKP81wwPPT~a6S8tZ2AyZ"}

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

