import mymodule
url = "https://www.thsrc.com.tw/TimeTable/Search"
headers = {
"User-Agent":"Googlebot"
}
basicdata = {
    "SearchType": "S",
    "Lang": "TW",
    "StartStation": "BanQiao",
    "EndStation": "XinZhu",
    "OutWardSearchDate": "2020/10/04",
    "OutWardSearchTime": "15:00",
    "ReturnSearchDate": "2020/10/05",
    "ReturnSearchTime": "15:00"
}

Connection = mymodule.Connection(url, headers, basicdata)
Connection.PostTest()