from website import Website
from topic import Topic
from content import Content

import requests
from bs4 import BeautifulSoup
import sys
from io import StringIO
import csv


class Crawler:
	conn = None
	cur = None



	def printContent(self, topic, title, url):
		print("New book found for" + topic.name)
		print(title)
		print(body)


	def getTopicFromName(self, topicName):
		topic = Topic(0, topicName)
		return topic

	def getPage(self, url):
		print("Retrieving book URL: \n" + url)
		session = requests.Session()
		headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}
		try:
			req = session.get(url, headers=headers)
		except requests.exceptions.RequestException:
			return None
		bsObj = BeautifulSoup(req.text, "lxml")
		return bsObj

	def safeGet(self, pageObj, selector):
		childObj = pageObj.select(selector)
		if childObj is not None and len(childObj) > 0:
			return childObj[0].get_text()
		return ""

	def search(self, topic, site):
		bsObj = self.getPage(site.searchURL + topic.name)
        table = bsObj.find("table", {"class":"tableList"})
        book = table.findAll("tr")
        for tr in book:
            cols = tr.findAll('td')
            site.url = cols[1].find("a").get('href')
            pageObj = self.getPage(site.url+url)
            title = self.safeGet(pageObj, site.pageTitle)
            