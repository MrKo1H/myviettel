import requests
import random
import json
"""
import requests

cookies = {
    'apimyvt_session': 'aob8kofjqopgvc8ij531o33dt4',
}

headers = {
    'Host': 'apivtp.vietteltelecom.vn:6768',
    'Connection': 'keep-alive',
    'Accept': '*/*',
    'User-Agent': 'My Viettel/5.11 (iPhone; iOS 15.3; Scale/3.00)',
    'Accept-Language': 'en-VN;q=1, vi-VN;q=0.9',
    'Content-Length': '253',
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = {
  'build_code': '2022.1.27',
  'device_id': '9A3A5594-E4B4-44AE-8F4A-0D58228698E3',
  'device_name': 'iPhone (iPhone14,2)',
  'is_app': '1',
  'list_all': '1',
  'os_type': 'ios',
  'os_version': '15.300000',
  'token': '549ACED5-33CA-6DED-B7C4-93C90C018F55-ODQ5NjQyMDYzNDg=',
  'type': 'data_all',
  'version_app': '5.11'
}

response = requests.post('https://apivtp.vietteltelecom.vn:6768/myviettel.php/getPromotionDataMyvtV2', headers=headers, cookies=cookies, data=data)
"""

"""
import requests

cookies = {
    'apimyvt_session': 'aob8kofjqopgvc8ij531o33dt4',
}

headers = {
    'Host': 'apivtp.vietteltelecom.vn:6768',
    'Connection': 'keep-alive',
    'Accept': '*/*',
    'User-Agent': 'My Viettel/5.11 (iPhone; iOS 15.3; Scale/3.00)',
    'Accept-Language': 'en-VN;q=1, vi-VN;q=0.9',
    'Content-Length': '228',
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = {
  'build_code': '2022.1.27',
  'device_id': '9A3A5594-E4B4-44AE-8F4A-0D58228698E3',
  'device_name': 'iPhone (iPhone14,2)',
  'os_type': 'ios',
  'os_version': '15.300000',
  'token': '549ACED5-33CA-6DED-B7C4-93C90C018F55-ODQ5NjQyMDYzNDg=',
  'type': 'all',
  'version_app': '5.11'
}

response = requests.post('https://apivtp.vietteltelecom.vn:6768/myviettel.php/getAccOfContract', headers=headers, cookies=cookies, data=data)
"""

"""
"""

class Client:
    def genMachineAddress():
        x = [chr(i) for i in range(ord("a"), ord("z")+1)] + [str(i) for i in range(10)]
        s = ""
        for i in range(8):
            s += random.choice(x)
        s += '-'
        for i in range(4):
            s += random.choice(x)
        s += '-'
        for i in range(4):
            s += random.choice(x)
        s += '-'
        for i in range(4):
            s += random.choice(x)
        s += '-'
        for i in range(12):
            s += random.choice(x)
        return s


class MyViettel:
    def __init__(self,account, password):
        self.account = account
        self.password = password
        self.deviceID = Client.genMachineAddress()
        self.imei = Client.genMachineAddress()

    def getOTP(self):
        headers = {
            'Host': 'apivtp.vietteltelecom.vn:6768',
            'Connection': 'keep-alive',
            'Accept': '*/*',
            'User-Agent': 'My Viettel/5.11 (iPhone; iOS 15.3; Scale/3.00)',
            'Accept-Language': 'en-VN;q=1, vi-VN;q=0.9',
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = {
          'build_code': '2022.1.27',
          'device_id': f'{self.deviceID}',
          'device_name': 'iPhone (iPhone14,2)',
          'os_type': 'ios',
          'os_version': '15.300000',
          'phone': f'{self.account}',
          'version_app': '5.11'
        }
        response = requests.post('https://apivtp.vietteltelecom.vn:6768/myviettel.php/getOTPLogin', headers=headers, data=data)
        print(json.loads(response.text))

    def loginWithOtp(self, otp):

        headers = {
            'Host': 'apivtp.vietteltelecom.vn:6768',
            'Connection': 'keep-alive',
            'Accept': '*/*',
            'User-Agent': 'My Viettel/5.11 (iPhone; iOS 15.3; Scale/3.00)',
            'Accept-Language': 'en-VN;q=1, vi-VN;q=0.9',
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = {
          'account': f'{self.account}',
          'build_code': '2022.1.27',
          'checksum': f'{self.imei}',
          'cmnd': '',
          'device_id': f'{self.deviceID}',
          'device_name': 'iPhone (iPhone14,2)',
          'keyDeviceAcc': '',
          'os_type': 'ios',
          'os_version': '15.300000',
          'otp_trust': '',
          'password': f'{otp}',
          'version_app': '5.11'
        }

        response = requests.post('https://apivtp.vietteltelecom.vn:6768/myviettel.php/loginMobileV4', headers=headers, data=data)
        response_data = json.loads(response.text)
        data = response_data["data"]
        self.token = data["data"]["token"]
        self.keyRefresh = data["data"]["keyRefresh"]
        self.keyRefreshFingerPrint = data["data"]["keyRefreshFingerPrint"]
        self.keyDeviceAcc = data["data"]["keyDeviceAcc"]
        self.subId = data["data"]["sub_id"]
        self.cusId = data["data"]["cusId"]

        print(self.token)
        print(self.keyRefresh)
        print(self.keyRefreshFingerPrint)
        print(self.keyDeviceAcc)
        print(self.subId)
        print(self.cusId)


        return response

me = MyViettel("0964206348", "thai1412")

me.getOTP()
otp = input("OTP=")
print(me.loginWithOtp(otp))
