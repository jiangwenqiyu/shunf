import requests
from apps import constance
import time



def getListInfo():
    url = 'https://sl-api-cloud-gw.sf-express.com:1080/shiva-trtms-ground-trade-personal/queryBidding/queryBiddingPage'
    header = {'Content-Type': 'application/json; charset=utf-8',
              'appUserName': 'P2011151855513953',
              'apiVersion': '8.9',
              'appName': 'sl',
              'appPackage': 'com.sf.trtms.driver',
              'appType': '6',
              'appVersion': '11.2.1',
              'billUserType': '0',
              'channel': 'android',
              'clientType': 'C',
              'deviceId': constance.DEVICEID,
              'token': constance.TOKEN}
    data = {
        "orderType": "",
        "vehicleLength": "1.8,2.7,3.5,4.2",
        "originTownCode": "110100",
        "biddingType": "",
        "destinationTownCode": "",
        "pageSize": 100,
        "vehicleTypeCode": "300",
        "orderBy": "exposureTimes",
        "destinationProvinceCode": "",
        "page": 1,
        "originProvinceCode": ""
    }
    res = requests.post(url, headers = header, json=data).json()

    total100 = list()
    try:
        for i in res['obj']:
            temp = list()
            orignPrice = i['price']   # 低价   0
            srcPrice = i['srcPrice']  # 原始价格  1
            planGainPrice = i['planGainPrice']   # 预计收益  2
            totalKm = i['totalKm']   # 全程公里  3
            vehicleTypeName = i['vehicleTypeName']    # 车辆  4
            maxVehicleLength = i['maxVehicleLength']   # 车长  5
            oilPrice = i['oilPrice']  # 油费  6

            startAddr = i['lineInfo'][0]['passList'][0]['detailAddress']  # 起始地  7
            endAddr = i['lineInfo'][0]['passList'][1]['detailAddress']   # 结束地  8

            packStartTm = i['packStartTm'] / 1000
            packEndTm = i['packEndTm'] / 1000
            createTm = i['createTm'] / 1000


            packStartTm = time.localtime(packStartTm)
            packStartTm = time.strftime("%Y-%m-%d %H:%M:%S", packStartTm)

            packEndTm = time.localtime(packEndTm)
            packEndTm = time.strftime("%Y-%m-%d %H:%M:%S", packEndTm)

            createTm = time.localtime(createTm)
            createTm = time.strftime("%Y-%m-%d %H:%M:%S", createTm)


            temp.append(orignPrice)
            temp.append(srcPrice)
            temp.append(planGainPrice)
            temp.append(totalKm)
            temp.append(vehicleTypeName)
            temp.append(maxVehicleLength)
            temp.append(oilPrice)
            temp.append(startAddr)
            temp.append(endAddr)
            temp.append(packStartTm)
            temp.append(packEndTm)
            temp.append(createTm)

            total100.append(temp)
    except:
        raise str(res)
    else:
        return total100


