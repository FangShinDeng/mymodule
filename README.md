# 搭配OOP引用自己寫的類別
    這一篇主要教學如何引用自己寫的函式
    因為每次要查詢到底有沒有爬蟲成功，Get,Post網站成功都要重新打一次代碼真的很麻煩，因此我們自己寫一個Connection類別，並把函式定義在類別裡面
    下次我們要爬重新的網頁時，就可以直接import使用拉!! 賀:D

## request套件 get及post基本用法
    我們先新增一個demo.py，然後引用requests套件，並將基礎的用法打上
    import requests
    res = requests.get(url) 或是 res = requests.post(url)
    if res.status_code == 200:
        print(res, "successfully connect")
    else:
        print(res, "error connect")
    
    但其實這種寫法每次都要重新寫一遍，真的非常麻煩，因此我們決定來寫一個Connection的類別!

## 寫一個Connection()的類別
    我們新增一個mymodule.py

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

## mymodule實體化及操作!
    我們在mymodule.py最下方直接實體化並且引入url打印結果！
    原本還要寫if else的代碼，直接能快速Get跟Post了阿！！！賀！！！

## 將mymodule.py放入python lib裡面，之後開發就方便引用了
    import sys
    print(sys.path)
    能靠這兩行打印出目前的檔案路徑，像我的就是在C:\Users\Mark\AppData\Local\Programs\Python\Python38-32\Lib
    我們將mymodule.py的檔案儲存到這個路徑裡面，再來就可以直接引用拉！！！

## 引用Lib路徑裡面的mymodule.py檔案時別忘了實體化也要加mymodule！
    我們新增一個index.py的檔案，直接進行import mymodule的動作，並直接實測有沒有成功GET
    <<記得要把原本資料夾的mymodule.py的檔名改掉，這邊我們調整成mymodule2.py，避免衝突>>