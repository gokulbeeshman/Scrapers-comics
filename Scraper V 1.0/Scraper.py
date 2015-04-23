import sys
import os
import urllib.request
from html.parser import HTMLParser
from bs4 import BeautifulSoup

class comic:
	index=-1
	isPresent=0
	title=""
	alt_text=""
	next=-1

def getxkcd(id):
	url='http://xkcd.com/%d' %id
	page=urllib.request.urlopen(url)

	soup=BeautifulSoup(page.read())	
	page.close();

	div=soup.findAll('div',attrs={'id':'comic'})

	for link in div:
		l=link.findAll('img')
		for x in l:
			yay='http:'+x['src']

	if not os.path.exists('xkcd/'):
		os.makedirs('xkcd/')
	urllib.request.urlretrieve(yay, 'xkcd/%d.jpg' %id)
	print('%d downloaded' %id)
	return id+1

def getdoghouse(id):
	url='http://thedoghousediaries.com/%d' %id
	page=urllib.request.urlopen(url)

	soup=BeautifulSoup(page.read())	
	page.close();

	div=soup.findAll('div',attrs={'id':'imgdiv'})

	for link in div:
		l=link.findAll('img')
		for x in l:
			yay='http://thedoghousediaries.com/'+x['src']

	if not os.path.exists('doghouse/'):
		os.makedirs('doghouse/')
	urllib.request.urlretrieve(yay, 'doghouse/%d.png' %id)
	print('%d downloaded' %id)
	next=soup.find('a', {'id':'nextlink'})
	next=next['href']
	next=next[-2:]
	next=int(next)
	return next

def getsmbc(id):
	url='http://www.smbc-comics.com/index.php?id=%d' %id
	page=urllib.request.urlopen(url)

	soup=BeautifulSoup(page.read())	
	page.close();

	img=soup.find('img',{'id':'comic'})
	img=img['src']
	img='http://www.smbc-comics.com/'+img
	if not os.path.exists('smbc/'):
		os.makedirs('smbc/')
	urllib.request.urlretrieve(img, 'smbc/%d.png' %id)
	print('%d downloaded' %id)
	return id+1

"""def getcyanideandhappiness(id):
	url='http://explosm.net/comics/%d' %id
	page=urllib.request.urlopen(url)

	soup=BeautifulSoup(page.read())	
	page.close();
	comic=soup.find('img',{'id':'main-comic'})
	comic=comic['src']
	comic='http:'+comic
	if not os.path.exists('cyanideandhappiness/'):
		os.makedirs('cyanideandhappiness/')
	print(comic)
	urllib.request.urlretrieve(comic, 'cyanideandhappiness/%d.png' %id)
	print('%d downloaded' %id) """




#def getchannelate(url):

getcyanideandhappiness(3892)