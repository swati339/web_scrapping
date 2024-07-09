import re 

print(re.findall("ab*c", "ac"))
print(re.findall("ab*c", "acc"))
print(re.findall("ab*c", "abcac"))
print( re.findall("ab*c", "abdc"))
print(re.findall("ab*c", "ABC", re.IGNORECASE)) #to print the input as it is.
print(re.findall("a.c", "abc"))#for single charater.
print(re.findall("a.c", "abbc"))
print(re.findall("a.*c", "acc"))# for substings in between

match_results = re.search("ab*c", "ABC", re.IGNORECASE)
print(match_results.group())

#re.sub() like .replace()
string = "Everything is <replaced> if it's in <tags>."
string = re.sub("<.*>", "ELEPHANTS", string)
print(string)

string = "Everything is <replaced> if it's in <tags>."
string = re.sub("<.*?>", "ELEPHANTS", string)
print(string)

# regex_soup.py

import re
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")

pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title) # Remove HTML tags

print(title)


