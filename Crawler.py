import urllib
import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import re


def process():
	url_template = "https://uk.indeed.com/jobs?q=Data%20Analyst&l=United%20Kingdom&start=0&vjk=7251c2622e8ec1bf" #&l={}&start={}
	max_results_per_city = 20 
	i = 0
	results = []
	df_more = pd.DataFrame(columns=["Location", "Synopsis"])
	for city in set(['London', 'Bristol', 'Leeds', 'England', 'Cambridge', 'Newcastle', 'Bradford', 'cardiff', 'Liverpool']):
		for start in range(0, max_results_per_city, 10):
			url = url_template.format(city, start)
			print(url)
			html = requests.get(url)
			soup = BeautifulSoup(html.content, 'html.parser', from_encoding="utf-8")
			for each in soup.find_all(class_= "result" ):
				
				try:
					location = each.find(class_="companyLocation").text.replace('\n', '')
				except:
					location = 'None'
				try:
					synopsis = each.find(class_="job-snippet").text.replace('\n', '')
				except:
					synopsis = 'None'
				
				df_more = df_more.append({'Location':location,'Synopsis':synopsis}, ignore_index=True)
				i += 1
				if i % 1000 == 0:  
					print('You have ' + str(i) + ' results. ' + str(df_more.dropna().drop_duplicates().shape[0]) + " of these aren't rubbish.")    
	df_more.to_csv('Indeed_Project.csv', encoding='utf-8',index=False)
