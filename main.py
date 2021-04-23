# Exercise 1
import requests
gov_ge_url = "https://www.mes.gov.ge/index.php?lang=geo"
response = requests.get(gov_ge_url)
print(response.status_code)
a= response.text

print(a.count("განათლება"))

# Exercise 2
import requests
a_photo_url="https://httpbin.org/image/jpeg"
response= requests.get(a_photo_url)
print(response.status_code)

response_headers= dict(response.headers)
print("Content type-",response_headers["Content-Type"])

with open("photo1.jpeg","wb") as f:
    f.write(response.content)
print("-"*50)

b_photo="https://httpbin.org/image/png"
response=requests.get(b_photo)
print(response.status_code)

response_headers= dict(response.headers)
print("Content type-",response_headers["Content-Type"])

with open("photo2.png","wb") as file:
    file.write(response.content)

print("-" * 50)

c_photo="https://httpbin.org/image/svg"
response = requests.get(c_photo)
print(response.status_code)


response_headers= dict(response.headers)
print("content type-",response_headers["Content-Type"])

with open("photo3.svg","wb") as pf:
    pf.write(response.content)

print("-" * 50)

#Exercise 3

import requests
url="https://httpbin.org/ip"
response= requests.get(url)
print(response.text)

with open("my-ip.txt","w") as ipfile:
    ipfile.write(response.text)