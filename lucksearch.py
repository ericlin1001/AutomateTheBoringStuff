#! python3
# lucksearch.py  -  Open several Google search results.
import requests,  sys,  webbrowser,  bs4
#get the command line args.
print('Googling...');
res = requests.get('https://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status();

#get the top5 links in search page.
soup = bs4.BeautifulSoup(res.text);

#open all the 5 links.
link = soup.select('.r a');
numOpen = min(5, len(link));
for i in range(numOpen):
    webbrowser.open('https://google.com' + link[i].get('href'));
