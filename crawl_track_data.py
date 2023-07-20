import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def deal_string(str1):
    """
    处理爬取的字符串
    """
    str2=str1.partition("Image")[0].replace("\n","\t").replace("\t\t\t\t","\n")
    return str2

home="http://agora.ex.nii.ac.jp/digital-typhoon/summary/wnp/l/202302.html.en"
html=urlopen(url=home).read().decode("utf-8")
soup=BeautifulSoup(html,features="lxml")

track_info=soup.find(name="table",attrs={"class":"TRACKINFO"})
title=track_info.find_all(name="th")
content_list=track_info.find_all(name="tr")
        
with open(file="track_result.txt",mode="w+",encoding="utf-8") as f:
    for i in title:
        if "Image" in i.get_text():
            break
        else:
            f.write(i.get_text().replace("\n",""))
    f.write("\n")
    for content in content_list:
        if content.has_attr("id")==True:
            result=deal_string(content.get_text())
            f.writelines(result)
            
            

