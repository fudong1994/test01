import json
import re

import requests

url = "http://10.224.67.135:8080/febs/v1/0/chances/batch"  # 创建商机
header = {"Content-Type": "application/json",
          "Authorization": "fa46cf11-fd96-48c7-82b8-8d5ecc4446c6"}
data = [
    {
        "businessPartnerLov": {
            "bpName": "测试企业220617103649",
            "bpType": "TENANT",
            "bpCategory": "TENANT",
            "bpId": 9040352,
            "bpTypeMeaning": "主承租人",
            "ownerUserId": 22,
            "bpCategoryMeaning": "承租人",
            "bpCode": "BP202206170068",
            "bpClass": "ORG",
            "__dirty": False
        },
        "productTypeLov": {
            "productCode": "MICRO_LEASE_FIFTY",
            "productId": 10042,
            "productTypeName": "内贸直租",
            "productStatus": "ONLINE",
            "productNumber": "PD2020100101",
            "businessType": "LEASE_INTERNAL",
            "productName": "标品-直50",
            "__dirty": False
        },
        "chanceName": "测试企业220617103649(内贸直租)",
        "companyId": "80",
        "companyName": "远东宏信普惠融资租赁（天津）有限公司",
        "customerManager": "22",
        "regionalDirector": "21",
        "employeeName": "吕博文",
        "employeeIdOfManagerName": "李景俊",
        "employeeId": 22,
        "ownerUserId": 22,
        "unitName": "广州分公司广州(一区)",
        "unitId": 102,
        "employeeIdOfManager": 21,
        "businessPartnerCode": "BP202206170068",
        "businessPartnerName": "测试企业220617103649",
        "bpId": 9040352,
        "productId": 10042,
        "productName": "标品-直50",
        "productType": "MICRO_LEASE_FIFTY",
        "businessTypeMeaning": "内贸直租",
        "businessType": "LEASE_INTERNAL",
        "__id": 53664,
        "_status": "create"
    }
]

res = requests.post(url=url, data=json.dumps(data), headers=header)  # 第一个url指get方法的参数，第二个url指上一行我们定义的接口地址
print(res.text)

res1 = re.findall('"chanceId":([^"]+)', res.text)
res2 = res1[0]
print(res2)


