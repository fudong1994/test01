import requests
import re


def get_token(username, password):
    url = "https://sit-icbs-ifs-api.fehorizon-ph.com/oauth/login"

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    datas = {
        "username": username,
        "password": password
    }
    s = requests.session()
    s.post(url=url, headers=headers, data=datas, allow_redirects=False)
    # res = response.headers
    #
    # url2 = res['Location']
    # print(url2)
    url2 = "https://sit-icbs-ifs-api.fehorizon-ph.com/oauth/oauth/authorize?response_type=token&client_id=hzero-front-sit1&redirect_uri=http%3A%2F%2F10.224.67.135%2Fhlpj%2Fprj001%2Fquery"
    response2 = s.get(url=url2, allow_redirects=False)
    res2 = response2.headers
    url3 = res2['Location']
    # print(url3)

    res1 = re.findall(r"access_token=(.*?)&", url3)
    token = "bearer " + ''.join(res1)
    # print(token)
    return token


if __name__ == '__main__':
    token = get_token("longboguang", 123456)
    print(token)
