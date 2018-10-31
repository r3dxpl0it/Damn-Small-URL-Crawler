## Damn Small URL Crawler
 Minimal But Powerful Crawler for Extracting all The Internal/External/Fuzz-able Links from a website it can also crawl until 2 depth for each link given. This Script is Used for Penetration-Testing and During Ethical Hacking Engagments
### Usage 
##### Instalation
`git clone https://github.com/r3dxpl0it/Damn_Small_URL_Crawler && cd Damn_Small_URL_Crawler && pip install -r	requirements.txt`
##### Examples 
 - Normal Crawl
`python3 dsuc.py -u http://testsite.com`
 - Show Fuzzable Links 
`python3 dsuc.py -u http://testsite.com -f` 
 - Show External Links 
`python3 dsuc.py -u http://testsite.com -e` 
 - DeepCrawl and Show Fuzzable Links 
`python3 dsuc.py -u -d http://testsite.com -f`
