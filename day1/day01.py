import requests
from day1.day07 import get_token
from api.now_time import get_time, get_time2
from api.regional_director import director
from day1.day06 import get_project

# 登录获取token
token = get_token("lvbowen01", 123456)
# ===============================创建客户==================================
url = "http://10.224.67.135:8080/febs/v1/bp-masters/0"  # 创建客户
header = {"Content-Type": "application/json",
          "Authorization": token}
data = {
    "registerCapitalCur": "CNY",
    "legalPersonIdType": "0",
    "actualControllerType": "NP",
    "abroadFlag": "0",
    "enterpriseProperty": "Non_State_holding_enterprises",
    "stockFlag": "0",
    "publicInstitutionFlag": "0",
    "actualControllerIdType": "0",
    "idType": "UNIFIED_SOCIAL_CREDIT_CODE",
    "parentCompany": "0",
    "invoiceTitle": "测试企业",
    "bpName": "测试企业" + get_time(),
    "taxpayerIdentifyCode": "92330282MA2GRTGM34",
    "bpClass": "ORG",
    "registeredDate": "2019-06-17 00:00:00",
    "registeredCapital": 0,
    "licenseTermsIfLong": 0,
    "legalPerson": "刘松",
    "enabledFlag": 0,
    "organizationCode": "MA2GRTGM-3",
    "certificateProvinceLov": {
        "regionCode": "440000",
        "regionId": 1925,
        "regionName": "广东省",
        "__dirty": False
    },
    "certificateCityLov": {
        "regionCode": "440100",
        "regionId": 1926,
        "regionName": "广州市",
        "__dirty": False
    },
    "certificateDistrictLov": {
        "regionCode": "440104",
        "regionId": 1928,
        "regionName": "越秀区",
        "__dirty": False
    },
    "certificateAddress": "阿萨大厦发飞洒",
    "nationalStandardIndustryLov": {
        "industryId": 524,
        "firstInduCode": "A",
        "secondInduCode": "01",
        "thirdInduCode": "011",
        "firstDesc": "农、林、牧、渔业",
        "nationalStandardIndustry": "稻谷种植",
        "secondDesc": "农业",
        "thirdDesc": "谷物种植",
        "fourthInduCode": "0111",
        "__dirty": False
    },
    "certificateScope": "食品经营：餐饮服务、食品销售及网上销售以及其他按法律、法规、国务院决定等规定未禁止或无需经营许可的项目和未列入地方产业发展负面清单的项目。（依法须经批准的项目，经相关部门批准后方可开展经营活动）",
    "idCardNo": "92330282MA2GRTGM34",
    "registeredProvinceLov": {
        "regionCode": "140000",
        "regionId": 217,
        "regionName": "山西省",
        "__dirty": False
    },
    "registeredCityLov": {
        "regionCode": "140300",
        "regionId": 240,
        "regionName": "阳泉市",
        "__dirty": False
    },
    "registeredPlace": "阿萨大厦发飞洒的",
    "subIndustry": "餐饮业",
    "insuredCount": "0",
    "survivalStatus": "NORMAL",
    "econKind": 70,
    "bpCategory": "TENANT",
    "bpType": "TENANT",
    "certificateProvinceId": 1925,
    "provinceMeaning": "广东省",
    "certificateCityId": 1926,
    "cityMeaning": "广州市",
    "certificateDistrictId": 1928,
    "districtMeaning": "越秀区",
    "nationalStandardInduId": 524,
    "nationalStandardIndustry": "稻谷种植",
    "registeredProvinceId": 217,
    "registeredCityId": 240,
    "registeredProvinceMeaning": "山西省",
    "registeredCityMeaning": "阳泉市",
    "bp001f1_nBasic_gAddress_table_hlcmBpMaster_hlcmBpMasterAddress_ds": [],
    "bp001f1_nBasic_gRole_table_hlcmBpMaster_hlcmBpMasterRole_ds": [
        {
            "bpCategory": "TENANT",
            "bpType": "TENANT",
            "primaryFlag": 1,
            "enabledFlag": 1,
            "bpCategoryMeaning": "承租人",
            "bpCreateWay": 2,
            "survivalStatus": "NORMAL",
            "bpCategoryLov": {
                "description": "承租人",
                "bpCategory": "TENANT"
            }
        }
    ],
    "bp001f1_nBasic_gContact_table_hlcmBpMaster_hlcmBpMasterContactInfo_ds": [
        {
            "enabledFlag": 1,
            "bpId": "-1",
            "emergencyContact": 1,
            "contactPerson": "吴彦祖",
            "position": "CONTACT_PERSON",
            "cellPhone": "15821898392"
        }
    ],
    "bp001f1_nBasic_gAccount_table_hlcmBpMaster_hlcmBpMasterBankAccount_ds": [],
    "bp001f1_nBasic_gShareholder_table_hlcmBpMaster_hlcmBpShareholderInfo_ds": [],
    "bp001f1_nBasic_gStaff_table_hlcmBpMaster_hlcmBpMainStaffInfo_ds": [],
    "bp001f1_nBasic_gDirector_table_hlcmBpMaster_hlcmBpDirectorInfo_ds": [],
    "bp001f1_nBasic_gPartnership_table_hlcmBpMaster_hlcmBpPartnership_ds": [],
    "bp001f1_nBasic_gRelatedCom_table_hlcmBpMaster_hlcmBpAffiEnterprises_ds": [],
    "bp001f1_nRisk_gLawsuitRecord_table_hlcmBpMaster_hlcmBpLawsuitRecord_ds": [],
    "bp001f1_nRisk_gCreditEvent_table_hlcmBpMaster_hlcmBpCreditEvent_ds": [],
    "bp001f1_nStaffInfo_gAssist_table_hlcmBpMaster_hlcmBpMasterAuthority_ds": [],
    "bp001f1_nStaffInfo_gChief_table_hlcmBpMaster_hlcmBpMasterAuthority_ds": [],
    "bp001f1_nAttachment_gAttachment_table_hlcmBpMaster_hlcmBpAttachment_ds": [],
    "addressesList": [],
    "roleList": [
        {
            "bpCategory": "TENANT",
            "bpType": "TENANT",
            "primaryFlag": 1,
            "enabledFlag": 1,
            "bpCategoryMeaning": "承租人",
            "bpCreateWay": 2,
            "survivalStatus": "NORMAL",
            "bpCategoryLov": {
                "description": "承租人",
                "bpCategory": "TENANT"
            }
        }
    ],
    "contactInfoList": [
        {
            "enabledFlag": 1,
            "bpId": "-1",
            "emergencyContact": 1,
            "contactPerson": "吴彦祖",
            "position": "CONTACT_PERSON",
            "cellPhone": "15821898392"
        }
    ],
    "bankAccountList": [],
    "shareholderInformationList": [],
    "affiEnterprisesList": [],
    "lawsuitRecordList": [],
    "creditEventList": [],
    "attachmentList": []
}
res = requests.post(url=url, json=data, headers=header)  # 第一个url指get方法的参数，第二个url指上一行我们定义的接口地址
res1 = res.json()
# print(res1)

bpid = res1['bpId']
bpCode = res1['bpCode']
bpname = res1['bpName']
ownerUserId = res1['ownerUserId']
ownerEmployeeId = res1['ownerEmployeeId']
ownerUserName = res1['ownerUserName']

# 获取区域信息
dir = director(token)
# print(director)
unitCompanyName = dir['unitCompanyName']
employeeIdOfManager = dir['employeeIdOfManager']
unitId = dir['unitId']
userIdOfManager = dir['userIdOfManager']
employeeIdOfManagerName = dir['employeeIdOfManagerName']
unitName = dir['unitName']
unitCompanyId = dir['unitCompanyId']

# ========================创建商机==============================
url1 = "http://10.224.67.135:8080/febs/v1/0/chances/batch"  # 创建商机
header1 = {"Content-Type": "application/json",
           "Authorization": token}
data1 = [
    {
        "businessPartnerLov": {
            "bpName": bpname,
            "bpType": "TENANT",
            "bpCategory": "TENANT",
            "bpId": bpid,
            "bpTypeMeaning": "主承租人",
            "ownerUserId": ownerUserId,
            "bpCategoryMeaning": "承租人",
            "bpCode": bpCode,
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
        "chanceName": bpname + "(内贸直租)",
        "companyId": unitCompanyId,
        "companyName": unitCompanyName,
        "customerManager": ownerUserId,
        "regionalDirector": userIdOfManager,
        "employeeName": ownerUserName,
        "employeeIdOfManagerName": employeeIdOfManagerName,
        "employeeId": ownerEmployeeId,
        "ownerUserId": ownerUserId,
        "unitName": unitName,
        "unitId": unitId,
        "employeeIdOfManager": employeeIdOfManager,
        "businessPartnerCode": bpCode,
        "businessPartnerName": bpname,
        "bpId": bpid,
        "productId": 10042,
        "productName": "标品-直50",
        "productType": "MICRO_LEASE_FIFTY",
        "businessTypeMeaning": "内贸直租",
        "businessType": "LEASE_INTERNAL",
        "__id": 53664,
        "_status": "create"
    }
]
res2 = requests.post(url=url1, json=data1, headers=header1)
res2 = res2.json()
get_data = res2[0]

_token = get_data['_token']
chanceId = get_data['chanceId']
chanceNumber = get_data['chanceNumber']
chanceName = get_data['chanceName']
businessPartnerCode = get_data['businessPartnerCode']
businessPartnerName = get_data['businessPartnerName']

# =======================导入授信===================================
url2 = "https://sit-icbs-ifs-api.fehorizon-ph.com/febs/v1/0/chances/importToCredit"  # 导入授信
header2 = {"Content-Type": "application/json",
           "Authorization": token}
data2 = {
    "creationDate": get_time2() + " 00:00:00",
    "createdBy": ownerUserId,
    "lastUpdateDate": get_time2() + " 00:00:00",
    "lastUpdatedBy": ownerUserId,
    "objectVersionNumber": 1,
    "_token": _token,
    "chanceId": chanceId,
    "chanceNumber": chanceNumber,
    "businessType": "LEASE_INTERNAL",
    "chanceStatus": "NEW",
    "companyId": "80",
    "ownerUserId": ownerUserId,
    "employeeId": ownerEmployeeId,
    "unitId": unitId,
    "employeeIdOfManager": employeeIdOfManager,
    "bpId": bpid,
    "chanceName": chanceName,
    "businessPartnerCode": businessPartnerCode,
    "businessPartnerName": businessPartnerName,
    "productType": "MICRO_LEASE_FIFTY",
    "customerManager": ownerUserId,
    "productName": "标品-直50",
    "productId": 10042,
    "regionalDirector": userIdOfManager,
    "businessTypeMeaning": "内贸直租",
    "customerManagerName": ownerUserName,
    "regionalDirectorName": employeeIdOfManagerName,
    "productTypeLov": {
        "productName": "标品-直50",
        "productId": 10042,
        "productCode": "MICRO_LEASE_FIFTY",
        "productTypeName": "内贸直租",
        "businessType": "LEASE_INTERNAL"
    },
    "leaseItemAmount": 100,
    "financeAmount": 100,
    "expectDeliveryDate": get_time2() + " 00:00:00",
    "platform": "5888",
    "cn001f2_vTab_gCompete_table_hlcnChance_hlcnChanceCompete_ds": [],
    "cn001f2_vTab_gProcess_table_hlcnChance_hlcnChanceProcess_ds": [],
    "cn001f2_vTab_gAttachment_table_hlcnChance_hlcnChanceAttachment_ds": [
        {
            "chanceId": chanceId,
            "documentName": "客户融资意向函",
            "attachmentUuid": "05ebbe6e10016449e8882618a64bc328b",
            "bucketName": "hlcn-chance-attachment"
        }
    ],
    "hlsCusProjectQuotationsList": [],
    "hlsCusChanceAttachmentList": [
        {
            "chanceId": chanceId,
            "documentName": "客户融资意向函",
            "attachmentUuid": "05ebbe6e10016449e8882618a64bc328b",
            "bucketName": "hlcn-chance-attachment"
        }
    ],
    "chanceCompetesList": [],
    "hlsCusChanceProcessList": []
}
res3 = requests.post(url=url2, json=data2, headers=header2)
# print(res3.json())
platform = res3.json()['platform']

# 查询project_id,project_number
project = get_project(chanceId)
project_id = project[0]
project_number = project[1]
project_info = project[2]
prjBpId = project[3]

# ======================保存授信数据=========================
url3 = "https://sit-icbs-ifs-api.fehorizon-ph.com/hlba/v1/0/dynamic-crud/save"
header3 = {"Content-Type": "application/json",
           "Authorization": token}

data3 = [
    {
        "layoutCode": "PRJ001F311",
        "metaKeys": {
            "top": [
                "prj001f311_vBasic1_fProBasic_form__hlpjProject_ds"
            ],
            "prj001f311_vBasic1_fProBasic_form__hlpjProject_ds": [
                "prj001f311_vLast_fHisTran_form_hlpjProject_hlpjProjectGatherInfo_ds",
                "prj001f311_vLast_gCreditDel_table_hlpjProject_hlpjProjectBp_ds",
                "prj001f311_vBasic1_gAsseorInfo_table_hlpjProject_hlpjProjectBp_ds",
                "prj001f311_vBasic1_gRelatedEnt_table_hlpjProject_hlpjProjectRelatedEnt_ds",
                "prj001f311_vBasic1_gDecisionHistory_table_hlpjProject_hlpjDecisionEngineHistory_ds",
                "prj001f311_tVerify_gTenant_table_hlpjProject_hlpjProjectVerification_ds",
                "prj001f311_tVerify_gController_table_hlpjProject_hlpjProjectVerification_ds",
                "prj001f311_tVerify_gAsseor_table_hlpjProject_hlpjProjectVerification_ds",
                "prj001f311_tVerify_gOther_table_hlpjProject_hlpjProjectVerification_ds",
                "prj001f311_vIncomeCheck3_gFixedAssetsAs_table_hlpjProject_hlpjProjectFixedAssets_ds",
                "prj001f311_tTaxD_gTaxE_table_hlpjProject_hlpjProjectIncomeVerify_ds",
                "prj001f311_tTaxD_gTaxF_table_hlpjProject_hlpjProjectIncomeVerify_ds",
                "prj001f311_vScheme_gScheme_table_hlpjProject_hlpjProjectScheme_ds",
                "prj001f311_tList_gFile_table_hlpjProject_hlpjProjectAttachment_ds",
                "prj001f311_tList_gPhoto_table_hlpjProject_hlpjProjectAttachment_ds",
                "prj001f311_tList_gAgfile_table_hlpjProject_hlpjProjectAttachment_ds"
            ],
            "prj001f311_vLast_fHisTran_form_hlpjProject_hlpjProjectGatherInfo_ds": [

            ],
            "prj001f311_vLast_gCreditDel_table_hlpjProject_hlpjProjectBp_ds": [

            ],
            "prj001f311_vBasic1_gAsseorInfo_table_hlpjProject_hlpjProjectBp_ds": [

            ],
            "prj001f311_vBasic1_gRelatedEnt_table_hlpjProject_hlpjProjectRelatedEnt_ds": [

            ],
            "prj001f311_vBasic1_gDecisionHistory_table_hlpjProject_hlpjDecisionEngineHistory_ds": [

            ],
            "prj001f311_tVerify_gTenant_table_hlpjProject_hlpjProjectVerification_ds": [

            ],
            "prj001f311_tVerify_gController_table_hlpjProject_hlpjProjectVerification_ds": [

            ],
            "prj001f311_tVerify_gAsseor_table_hlpjProject_hlpjProjectVerification_ds": [

            ],
            "prj001f311_tVerify_gOther_table_hlpjProject_hlpjProjectVerification_ds": [

            ],
            "prj001f311_vIncomeCheck3_gFixedAssetsAs_table_hlpjProject_hlpjProjectFixedAssets_ds": [

            ],
            "prj001f311_tTaxD_gTaxE_table_hlpjProject_hlpjProjectIncomeVerify_ds": [

            ],
            "prj001f311_tTaxD_gTaxF_table_hlpjProject_hlpjProjectIncomeVerify_ds": [

            ],
            "prj001f311_vScheme_gScheme_table_hlpjProject_hlpjProjectScheme_ds": [

            ],
            "prj001f311_tList_gFile_table_hlpjProject_hlpjProjectAttachment_ds": [

            ],
            "prj001f311_tList_gPhoto_table_hlpjProject_hlpjProjectAttachment_ds": [

            ],
            "prj001f311_tList_gAgfile_table_hlpjProject_hlpjProjectAttachment_ds": [

            ]
        },
        "prj001f311_vBasic1_fProBasic_form__hlpjProject_ds": [
            {
                "creationDate": get_time2() + " 00:00:00",
                "createdBy": ownerUserId,
                "lastUpdateDate": get_time2() + " 00:00:00",
                "lastUpdatedBy": ownerUserId,
                "objectVersionNumber": 2,
                "_token": _token,
                "projectId": project_id,
                "projectNumber": project_number,
                "projectName": chanceName,
                "documentType": "PRJL",
                "documentCategory": "PROJECT",
                "businessType": "LEASE",
                "projectStatus": "NEW",
                "companyId": unitCompanyId,
                "chanceId": chanceId,
                "ownerUserId": ownerUserId,
                "employeeId": ownerUserId,
                "unitId": unitId,
                "employeeIdOfManager": employeeIdOfManager,
                "projectSource": "CHANNEL_RECOMMENDATION",
                "chanceName": chanceName,
                "employeeName": ownerUserName,
                "productId": 10042,
                "productCode": "MICRO_LEASE_FIFTY",
                "projectSourceDescription": "qweeqw",
                "platform": platform,
                "assessorId": bpid,
                "assessorWhetherTenantFlag": "1",
                "clickContractFlag": 0,
                "orderCustomerFlag": 0,
                "transportMethod": "DOMESTIC_TRANSPORT",
                "raiseLevelFlag": 0,
                "newFlag": 1,
                "levelUpReason": "No",
                "schemeType": "scheme1",
                "microFiftyVersion": 1,
                "microThreeVersion": 1,
                "replyThreeVersion": 1,
                "wflLevel": "Auto",
                "hasTutorFlag": "N",
                "remoteDueDiligence": "0",
                "checkWorkflow": 0,
                "assessorName": bpname,
                "unitName": unitName,
                "assessorBpClass": "ORG",
                "parentUnitName": "广州分公司",
                "provinceName": "广东省",
                "cityName": "广州市",
                "registeredDate": "2019-06-17 00:00:00",
                "registeredCapital": 0,
                "legalPerson": "刘松",
                "certificateAddress": "阿萨大厦发飞洒",
                "economicInduClassify": "机械加工",
                "economicInduClassSec": "机械零部件加工",
                "certificateScope": "食品经营：餐饮服务、食品销售及网上销售以及其他按法律、法规、国务院决定等规定未禁止或无需经营许可的项目和未列入地方产业发展负面清单的项目。（依法须经批准的项目，经相关部门批准后方可开展经营活动）",
                "industryRating": "ENCOURAGE",
                "productName": "标品-直50",
                "creditTerm": 24,
                "economicInduClassifyNew": "机加",
                "economicInduClassSecNew": "机械零部件加工",
                "economicInduClassifyId": 1,
                "economicInduClassSecId": 6,
                "economicInduClassifyNewId": 1,
                "economicInduClassSecNewId": 6,
                "assessorIdLov": {
                    "bpId": bpid,
                    "bpName": bpname
                },
                "unitLov": {
                    "unitId": unitId,
                    "unitName": unitName
                },
                "employeeLov": {
                    "id": ownerUserId,
                    "realName": ownerUserName
                },
                "ignoreRequiredFlag": True,
                "prj001f311_vLast_fHisTran_form_hlpjProject_hlpjProjectGatherInfo_ds": [
                    {
                        "creationDate": get_time2() + " 00:00:00",
                        "createdBy": ownerUserId,
                        "lastUpdateDate": get_time2() + " 00:00:00",
                        "lastUpdatedBy": ownerUserId,
                        "objectVersionNumber": 1,
                        "_token": _token,
                        "projectInfoId": project_info,
                        "projectId": project_id,
                        "businessQueryDate": get_time2() + " 00:00:00",
                        "businessConclusion": "asdasd",
                        "nearlyEquityChangeFlag": "1",
                        "equityStabilityJudgement": "A",
                        "creditAmountTotal": 100,
                        "creditAmountAdd": 100,
                        "creditTerm": "24",
                        "actualExposurePeriod": 12,
                        "mortgageFlag": 1,
                        "creditAmountEmployee": "100",
                        "ifNoInvoice": "0",
                        "adjustRange": 0,
                        "validityCredit": "SIX_MONTHS",
                        "comprehensiveReview": "123",
                        "supplierAttributes": "A",
                        "deviceProperties": "A",
                        "premises": "0",
                        "boom": "ENCOURAGE",
                        "productName": "标品-直50",
                        "businessArea": "广东省",
                        "establishmentPeriod": "3",
                        "priceTotalAb": "0.000000",
                        "rateAb": "0.0000",
                        "fixScale": 0,
                        "__id": 2606,
                        "_status": "update"
                    }
                ],
                "prj001f311_vLast_gCreditDel_table_hlpjProject_hlpjProjectBp_ds": [
                    {
                        "creationDate": get_time2() + " 00:00:00",
                        "createdBy": ownerUserId,
                        "lastUpdateDate": get_time2() + " 00:00:00",
                        "lastUpdatedBy": ownerUserId,
                        "objectVersionNumber": 3,
                        "_token": _token,
                        "prjBpId": prjBpId,
                        "projectId": project_id,
                        "bpCategory": "TENANT",
                        "bpId": bpid,
                        "bpCode": bpCode,
                        "bpType": "TENANT",
                        "bpClass": "ORG",
                        "bpName": bpname,
                        "registeredPlace": "阿萨大厦发飞洒",
                        "foundedDate": "2019-06-17 00:00:00",
                        "registeredCapital": "0",
                        "organizationCode": "MA2GRTGM-3",
                        "idType": "UNIFIED_SOCIAL_CREDIT_CODE",
                        "idCardNo": "92330282MA2GRTGM34",
                        "licenseTermsIfLong": 0,
                        "legalPerson": "刘松",
                        "registeredDate": "2019-06-17 00:00:00",
                        "enabledFlag": 1,
                        "economicInduClassify": "机械加工",
                        "economicInduClassSec": "机械零部件加工",
                        "certificateScope": "食品经营：餐饮服务、食品销售及网上销售以及其他按法律、法规、国务院决定等规定未禁止或无需经营许可的项目和未列入地方产业发展负面清单的项目。（依法须经批准的项目，经相关部门批准后方可开展经营活动）",
                        "industryRating": "ENCOURAGE",
                        "mainBodyType": "TENANT",
                        "economicInduClassifyNewId": 1,
                        "economicInduClassSecNewId": 6,
                        "economicInduClassifyNew": "机加",
                        "economicInduClassSecNew": "机械零部件加工",
                        "economicInduClassifyId": 1,
                        "economicInduClassSecId": 6,
                        "bpSource": "SELF",
                        "ucsbgPhoneNumber": "158336658954",
                        "ucsbgPhone": "asd",
                        "queryAllFlag": False,
                        "controllerBirthEnd": 0,
                        "productCode": "MICRO_LEASE_FIFTY",
                        "bpIdLov": {
                            "bpCode": bpCode,
                            "bpId": bpid,
                            "bpType": "TENANT",
                            "bpName": bpname,
                            "bpCategory": "TENANT"
                        },
                        "productTypeCode": "LEASE_INTERNAL",
                        "creditTerm": "24",
                        "actualExposurePeriod": 12,
                        "creditApplyAmount": 100,
                        "validResDoc": "BOARD_RESOLUTION",
                        "proportionType": "TWO_THIRDS",
                        "signingProportion": 0.667,
                        "paymentWay": "ARRIVAL",
                        "paymentObjectType": "VENDER",
                        "bpLov": {
                            "registeredDate": "2019-06-16T16:00:00.000Z",
                            "registeredCapital": "0",
                            "certificateAddress": "阿萨大厦发飞洒",
                            "economicInduClassify": "机械加工",
                            "economicInduClassSec": "机械零部件加工",
                            "industryRating": "ENCOURAGE",
                            "legalPerson": "刘松"
                        },
                        "__id": 2366,
                        "_status": "update"
                    }
                ],
                "prj001f311_vBasic1_gAsseorInfo_table_hlpjProject_hlpjProjectBp_ds": [

                ],
                "prj001f311_vBasic1_gRelatedEnt_table_hlpjProject_hlpjProjectRelatedEnt_ds": [

                ],
                "prj001f311_vBasic1_gDecisionHistory_table_hlpjProject_hlpjDecisionEngineHistory_ds": [

                ],
                "prj001f311_tVerify_gTenant_table_hlpjProject_hlpjProjectVerification_ds": [
                    {
                        "projectId": project_id,
                        "verificationType": "TENANT",
                        "enabledFlag": 1,
                        "verificationName": "asd",
                        "verificationSource": "ZHONGDENGWANG",
                        "webSite": "https://www.zhongdengwang.org.cn",
                        "verificationSketch": "asd",
                        "discloserLov": {
                            "id": ownerUserId,
                            "realName": ownerUserName
                        },
                        "discloserId": ownerUserId,
                        "discloserName": ownerUserName,
                        "__id": 2902,
                        "_status": "create"
                    }
                ],
                "prj001f311_tVerify_gController_table_hlpjProject_hlpjProjectVerification_ds": [
                    {
                        "projectId": project_id,
                        "verificationType": "REAL_CONTROLLER",
                        "verificationName": "sdf",
                        "verificationSource": "ZHONGDENGWANG",
                        "webSite": "https://www.zhongdengwang.org.cn",
                        "verificationSketch": "asd",
                        "discloserLov": {
                            "id": ownerUserId,
                            "realName": ownerUserName
                        },
                        "discloserId": ownerUserId,
                        "discloserName": ownerUserName,
                        "__id": 2911,
                        "_status": "create"
                    }
                ],
                "prj001f311_tVerify_gAsseor_table_hlpjProject_hlpjProjectVerification_ds": [
                    {
                        "projectId": project_id,
                        "verificationType": "EVALUATION_SUBJECT",
                        "verificationName": "asd",
                        "verificationSource": "ZHONGDENGWANG",
                        "webSite": "https://www.zhongdengwang.org.cn",
                        "verificationSketch": "asd",
                        "discloserLov": {
                            "id": ownerUserId,
                            "realName": ownerUserName
                        },
                        "discloserId": ownerUserId,
                        "discloserName": ownerUserName,
                        "__id": 2920,
                        "_status": "create"
                    }
                ],
                "prj001f311_tVerify_gOther_table_hlpjProject_hlpjProjectVerification_ds": [

                ],
                "prj001f311_vIncomeCheck3_gFixedAssetsAs_table_hlpjProject_hlpjProjectFixedAssets_ds": [

                ],
                "prj001f311_tTaxD_gTaxE_table_hlpjProject_hlpjProjectIncomeVerify_ds": [
                    {
                        "projectId": project_id,
                        "__id": 2605,
                        "_status": "create"
                    }
                ],
                "prj001f311_tTaxD_gTaxF_table_hlpjProject_hlpjProjectIncomeVerify_ds": [
                    {
                        "projectId": project_id,
                        "verifyDate": "2021-01-01 00:00:00",
                        "__id": 2469,
                        "_status": "create"
                    },
                    {
                        "projectId": project_id,
                        "verifyDate": "2020-01-01 00:00:00",
                        "__id": 2470,
                        "_status": "create"
                    },
                    {
                        "projectId": project_id,
                        "verifyDate": "2019-01-01 00:00:00",
                        "__id": 2471,
                        "_status": "create"
                    }
                ],
                "prj001f311_vScheme_gScheme_table_hlpjProject_hlpjProjectScheme_ds": [

                ],
                "prj001f311_tList_gFile_table_hlpjProject_hlpjProjectAttachment_ds": [

                ],
                "prj001f311_tList_gPhoto_table_hlpjProject_hlpjProjectAttachment_ds": [

                ],
                "prj001f311_tList_gAgfile_table_hlpjProject_hlpjProjectAttachment_ds": [

                ],
                "__id": 2225,
                "_status": "update"
            }
        ],
        "__id": 1018,
        "_status": "update",
        "checkUrls": {
            "hlpj_project": "fe-bus/v1/0/projects/micro/check/{datasetName}"
        },
        "serverNames": {
            "hlpj_project": "fe-bus",
            "hlpj_project_gather_info": "fe-bus",
            "hlpj_decision_engine_history": "fe-bus",
            "hlpj_project_bp": "fe-bus"
        }
    }
]
res4 = requests.post(url=url3, json=data3, headers=header3)
print(res4.json())
