from bs4 import BeautifulSoup
import urllib.request as urllib2
import requests

emailList=[]
noEmailList=[]
#function that extracts all emails from a page you provided and stores them in a list
def emailExtractor(urlString):
    getH=requests.get(urlString)
    h=getH.content
    soup=BeautifulSoup(h,'html.parser')
    mailtos = soup.select('a[href^=mailto]')
    for i in mailtos:
        href=i['href']
        try:
            str1, str2 = href.split(':')
        except ValueError:
            break
        if str2.startswith('info@comuni'): #This filters some email directions that we don't want to have on our principal list
            noEmailList.append(str2)
        else:
            emailList.append(str2)

#This function saves the email directions that are included in the list we pass from parameters
#We also gotta give to it the name of the archive where we want to store the email directions
def mailSaver(emailListAux,archivo):
    f=open(archivo,'w')
    for email in emailListAux:
        f.write(f'{email}\n')
    f.close()

x=1
for comuna in range(1,99):
    if x<10:
        l='00'+str(x)
    else:
        l='0'+str(x)
    try:
        html_page = urllib2.urlopen(f"http://www.comuni-italiani.it/alfa/{l}.html")
        soup = BeautifulSoup(html_page,'html.parser')
    except Exception:
        pass
    links=[]
    for link in soup.findAll('a'):
        links.append(link.get('href'))
    for link in links:
        link = link.replace('..','')
        emailExtractor(f"http://www.comuni-italiani.it/{link}")
    x+=1
    mailSaver(emailList,'mail.txt')
    mailSaver(noEmailList, 'noMail.txt')


    
