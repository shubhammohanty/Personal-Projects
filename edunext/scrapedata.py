import requests
session = requests.session()


login_url = 'https://summerfields.edunexttechnologies.com/SignUp'
hw_url = 'https://summerfields.edunexttechnologies.com/mvc/std/homework'

payload = {
    'username':'KC/004160',
    'password':'swayam@2012'
}

r = session.post(login_url, data=payload)
print(r)

hw = session.get(hw_url)
print(hw.json)

session.close()


