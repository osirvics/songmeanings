import time
import urllib
import bs4
import requests
import songcrawler
import startcrawl
import mechanicalsoup


#https://genius.com/search?q=new%20rules%20dua%20lipa
#https://genius.com/search?q=havana%20camila%20cabello
 
def findUrl(search_query):
	query_string = search_query.replace(" ", "+")
	target_url = ('http://songmeanings.com/query/?query=%s&type=all' %(query_string))
	response = requests.get(target_url)
	html = response.text
	soup = bs4.BeautifulSoup(html, "html.parser")
	table = soup.find(summary = "table")
	child = table.find(class_ = "item")
	link = ""
	try:
		link =  child.select("a")[0].get('href')
	except IndexError:
		#songcrawler.getFromSongFacts(search_query)
		return None
	full_link = urllib.parse.urljoin('https:', link)
	print(full_link)
	return full_link

def findSongFact(search_query):
	query_string = search_query.replace(" ", "+")
	query_string = query_string + " site:songfacts.com"
	print("Query url: " + str(query_string))
	browser = mechanicalsoup.StatefulBrowser()
	browser.open("https://duckduckgo.com/")
	# Fill-in the search form
	browser.select_form('#search_form_homepage')
	browser["q"] = query_string 
	browser.submit_selected()
	link = browser.get_current_page().select('a.result__a')[0].attrs['href']
	print(link)
	return link

def fingGeniusSongUrl(search_query):
	#query_string = search_query.replace(" ", "+")
	query_string = search_query + " site:genius.com"
	print("Query url: " + str(query_string))
	browser = mechanicalsoup.StatefulBrowser()
	browser.open("https://duckduckgo.com/")
	browser.select_form('#search_form_homepage')
	browser["q"] = query_string 
	browser.submit_selected()
	link = browser.get_current_page().select('a.result__a')[0].attrs['href']
	print(link)
	return link

if __name__ == '__main__':
	fingGeniusSongFactUrl("sorry not sorry demi lovato")
	

#print(table.find('a', recursive=False))