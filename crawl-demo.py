#coding=utf-8
import requests
from bs4 import BeautifulSoup

resp=requests.get('https://www.hostinger.vn/cloud-hosting?utm_medium=affiliate&utm_source=aff26166&utm_campaign=aff439&session=10254a1451f51f4007021a28107fb2') #request toi trang can crawl
# print(resp) #in ra status code response
# print(resp.content) #in tat ca source code response

bs_obj=BeautifulSoup(resp.content,'lxml') #tao doi tuong BeautifulSoup

# Crawl "Cloud chuyen nghiep"
data = str(bs_obj.find(id="pricing-table-plan-hosting-cloud-professional"))

bs_obj_ul=BeautifulSoup(data,'lxml')
p_list = bs_obj_ul.find_all('p')
li_list = bs_obj_ul.find_all('li')

print(p_list[0].string)

categories = []
for i in range(2, 10):
    categories.append(p_list[i].string)

count = [0, 5, 9, 11, 15, 18, 22, 25, 32]

for i in range(1, 9):
    print("\n" + categories[i-1] + "\n")
    for j in range(count[i-1], count[i]):
        text = li_list[j].get_text()
        if text.endswith('help_outline') == True:
            print(text[:-14])
        else:
            print(text)
