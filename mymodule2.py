import requests
class Connection:
    def __init__(self, url):
        self.url = url
        pass

    def GetTest(self):
        res = requests.get(self.url)
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
    
    def PostTest(self):
        res = requests.post(self.url)
        if res.status_code == 200:
            print(res, "Post successfully")
            pass
        else: 
            print(res, "Post error")
            # print(res.text)
            pass
        pass
    
    def PostPrint(self):
        res = requests.post(self.url)
        print(res.text)

url = "https://namedmaster.com/"
Connection = Connection(url)
Connection.GetTest()
