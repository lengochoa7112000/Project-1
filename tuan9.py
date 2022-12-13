#coding=utf-8
import requests
from bs4 import BeautifulSoup
import argparse
import json

# Input
data =  '''{
  "providers": ["hostinger", "siteground", "sitebunker"],
  "urls": ["https://www.hostinger.com/cloud-hosting",
           "https://www.siteground.com/web-hosting.htm",
           "https://sitebunker.net/web-ssd-hosting"],
  "pakage": {
    "full_tag_names": ["id", ""],
    "full_tag_values": [["pricing-table-plan-hosting-cloud-economy", "pricing-table-plan-hosting-cloud-enterprise", "pricing-table-plan-hosting-cloud-professional"],
                        ["", "", ""]],
    "details_tag": ["li",
                    "li",
                    "li"]
  }
}'''

# parse json:
data = json.loads(data)

def crawl():
  # duyet tat ca url
  for url in data['urls']:
    # luu so thu tu
    id = data['urls'].index(url)
    resp = requests.get(url)
    soap = BeautifulSoup(resp.content,'html.parser')
    details = soap.find_all(data['pakage']['details_tag'][id])

    # duyet tat ca yeu to trong checklist
    for check in checklist:
      # chi tim kiem cac thong tin user cung cap
      if check[1] != None:
        for detail in details:
          # kiem tra ton tai thong tin cung cap hay khong, vi du ton tai thong tin ve RAM?
          if check[0] in detail.get_text().upper():
            # kiem tra phu hop voi thong tin user cung cap?
            if check[1] in detail.get_text():
              # +1 vao check_output neu phu hop
              check_output[id] = check_output[id] + 1
    # kiem tra muc do phu hop va in ra thong tin provider
    if check_output[id] >= 3:
      print('Provider: ', data['providers'][id])
      print('Website crawl: ', data['urls'][id])


parser = argparse.ArgumentParser()
parser.add_argument("-RAM", dest="RAM", help="In GB, example for 6 GB RAM: -RAM 6")
parser.add_argument("-CPU", dest="CPU", help="CPU Cores, example for 4 CPU Cores: -CPU 4")
parser.add_argument("-Storage", dest="Storage", help="In GB, example for 250 GB SSD Storage: -Storage 200")
parser.add_argument("-Websites", dest="Websites", help="Example for 300 Websites: -Websites 300")
args = parser.parse_args()

RAM = args.RAM
CPU = args.CPU
STORAGE = args.Storage
WEBSITES = args.Websites
checklist = [("RAM", RAM), ("CPU", CPU), ("STORAGE", STORAGE), ("WEBSITES", WEBSITES)]
check_output = [0, 0, 0]

crawl()
