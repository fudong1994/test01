import requests


def director(token):
    url = "https://sit-icbs-ifs-api.fehorizon-ph.com/hlba/v1/0/company-attributes/getEmployeeInfo"

    header = {"Content-Type": "application/json",
              "Authorization": token}

    response = requests.get(url=url, headers=header)
    return response.json()
