import json
import hashlib
# don't forget to import these two modules below by changing into directory Python2/Scripts
# use command "easy_install.exe <module>"
import requests
import xmltodict

username = "085368933577"
password = "8605f7d5a702e742"
username_bytes = username.encode('utf-8')
password_bytes = password.encode('utf-8')


def price_list():
    signature = hashlib.md5(username_bytes + password_bytes +
                            "pl".encode('utf-8')).hexdigest()
    dataJson = """{
        \"commands\" : \"pricelist\",
        \"username\" : \"""" + username + """\",
        \"sign\"     : \"""" + signature + """\"
    }"""

    url = "https://testprepaid.mobilepulsa.net/v1/legacy/index/data/telkomsel"
    headers = {'content-type': 'application/json'}

    data_request = requests.post(
        url, data=dataJson, headers=headers, timeout=30).text
    data = json.loads(data_request)
    return data['data']
