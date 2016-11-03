import re,html,time,requests

def crawl_joke_list(page=1):
	url = "http://www.qiushibaike.com/text/" + str(page)
	res = requests.get(url)
	pattern = re.compile("<div class = \"article block untagged mb15.*?<div class = \"content\">.*?</div>",re.S)

	body = html.unescape(res.text).replace("<br/>","\n")
	m = pattern.findall(body)

	user_pattern = re.compile("<div class=\"author clearfix\">.*?<h2>(.*?)</h2>",re.S)
	content_pattern = re.compile("<div class=\"content\">(.*?)</div>",re.S)
	for joke in m :
		user = user_pattern.findall(joke)
		output = []
		if len(user) >0:
			output.append(user[0])
		content = content_pattern.findall(joke)
		if len(content) >0 :
			output.append(content[0].replace('\n',''))
		print('\t'.join(output))
		print('hello')
	time.sleep(1)

if __name__ == '__main__':
	for i in range(1,3):
		crawl_joke_list(i)
