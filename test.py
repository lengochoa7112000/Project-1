#coding=utf-8
import requests
from bs4 import BeautifulSoup
import argparse
import json

# Input
data =  '''{
  "hostinger": {
    "url": "https://www.hostinger.vn/cloud-hosting?utm_medium=affiliate&utm_source=aff26166&utm_campaign=aff439&session=10254a1451f51f4007021a28107fb2",
    "tag_id": "pricing-table-plan-hosting-cloud-professional",
    "tag_category": "p",
    "tag_detail": "li"
  },
  "siteground": {
    "url": "https://www.siteground.com/web-hosting.htm?afcode=117c8e94c19e8b921cf05d22c15a113b&campaign=qsp10005",
    "tag_id": "view-growbig",
    "tag_category": "p",
    "tag_detail": "li"
  }
}'''

# parse x:
hosts = json.loads(data)

# the result is a Python dictionary:
# print(hosts['hostinger']['url'])

def Crawl_test():
    resp = requests.get(hosts[PROVIDER]['url']) #request toi trang can crawl
    print('\n[+] Get data from %s' % PROVIDER)
    print(resp) #in ra status code response
    print('[+] Result')
    bs_obj = BeautifulSoup(resp.content,'lxml') #tao doi tuong BeautifulSoup
    
    # Crawl "Cloud chuyen nghiep"
    data = str(bs_obj.find(id = hosts[PROVIDER]['tag_id']))
    bs_obj_ul=BeautifulSoup(data, 'lxml')
    # category tag
    p_list = bs_obj_ul.find_all(hosts[PROVIDER]['tag_category'])
    # detail tag
    li_list = bs_obj_ul.find_all(hosts[PROVIDER]['tag_detail'])

    categories = []
    for i in range(len(p_list)):
        categories.append(p_list[i].get_text())

    details = []
    for i in range(len(li_list)):
        details.append(li_list[i].get_text())
    
    print(categories)
    print(details)

parser = argparse.ArgumentParser()
parser.add_argument("-provider", dest="provider", help="-provider [ hostinger | siteground ]")
args = parser.parse_args()

PROVIDER = args.provider

if PROVIDER:
    Crawl_test()
else:
    parser.print_help()
