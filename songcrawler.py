import time
import urllib
import bs4
import requests
import startcrawl
import types

def remove_smart_quotes (text):
  return text.replace(u"\u2018", "'") \
             .replace(u"\u2019", "'") \
             .replace(u"\u201c", '"') \
             .replace(u"\u201d", '"')


def getFromSongsmeanings(search_query):
	target_url = startcrawl.findUrl(search_query)
	if target_url is not None:
		response = requests.get(target_url)
		html = response.text
		soup = bs4.BeautifulSoup(html, "html.parser")
		#commentsHolder = soup.find(class_= "holder-comments")\
		print(soup.find(class_ = "heading_meanings").text)
		commentsList = soup.find(id= "comments-list")
		comments = commentsList.find_all(class_="text")
		outputList = []
		for index, comment in enumerate(comments):
			if comment.find(class_ = "sign") is not None:
				comment.find(class_ = "sign").decompose()
				comment.find(class_ = "title").decompose()
				comment.find(class_ = "answers").decompose()
				com = comment.get_text(strip=True)
				com = com.replace('\\', '')
				com = remove_smart_quotes(com)
				com = com.strip('\\')
				payload = {}
				#comment = comment.replace(\t', '')
				payload["meaning"] = com
				outputList.append(payload)
				##print(index, comment.get_text())
			
		# for index, nu in enumerate(outputList):
		# 	print(index)
		if len(outputList) == 0:
			return getFromSongFacts(search_query)
		print
		return outputList
	elif target_url is None:
		return getFromSongFacts(search_query)

		



def getFromSongFacts(search_query):
	target_url = startcrawl.findSongFact(search_query)
	response = requests.get(target_url)
	html = response.text
	soup = bs4.BeautifulSoup(html, "html.parser")
	factlist = soup.find(class_= "factsullist-sf clearfix")
	#print(factlist.prettify())
	songfact = []
	chunks = factlist.find_all("li")

	payload = {}
	payload["meaning"] = ""
	for chunk in chunks:
		text = chunk.contents[0]
		for br in text.find_all("br"):
			br.replace_with("\n")
		com = text.get_text(strip=True)
		payload["meaning"] += com
	songfact.append(payload)
	return songfact
	
if __name__ == '__main__':
	#getFromSongFacts("ll")
	getFromSongsmeanings("FEEL IT STILL PORTUGAL THE MAN")
