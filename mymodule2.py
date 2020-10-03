import requests
class Connection:
    def __init__(self, url):
        self.url = url
        pass

    def GetTest(self):
        res = requests.get(self.url, headers = self.headers)
        self.res = res
        if res.status_code == 200:
            print(res, "Get successfully")
            pass
        else: 
            print(res, "Get error")
            # print(res.text)
            pass
        pass
    pass
    def GetPrint(self):
        res = requests.get(self.url)
        print(res.text)
    
    def PostTest(self, headers, data):
        self.headers = headers
        self.data = data
        res = requests.post(self.url, headers = self.headers, data = self.data)
        self.res = res
        if res.status_code == 200:
            print(res, "Post successfully")
            pass
        else: 
            print(res, "Post error")
            # print(res.text)
            pass
        pass
    
    def PostPrint(self):
        res = requests.post(self.url, headers = self.headers, data = self.data)
        print(res.text)

# url = "https://namedmaster.com/"
# Connection = Connection(url)
# Connection.GetTest()

url = "https://www.thsrc.com.tw/TimeTable/Search"
headers = {
"User-Agent":"Googlebot"
}
basicdata = {
    "SearchType": "S",
    "Lang": "TW",
    "StartStation": "BanQiao",
    "EndStation": "ZuoYing",
    "OutWardSearchDate": "2020/10/28",
    "OutWardSearchTime": "11:00",
    "ReturnSearchDate": "2020/10/30",
    "ReturnSearchTime": "11:00"
}

Connection = Connection(url)
Connection.PostTest(headers, basicdata)
# print(Connection.res)
Connection.PostPrint()
# print(Connection.url)

# res = requests.post(url, headers = headers, data = basicdata)
# print(res.text)