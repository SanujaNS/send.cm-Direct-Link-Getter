from bs4 import BeautifulSoup
import cloudscraper
from re import findall
from time import sleep

# Accepting Sendcm URL from User
input_string = input("Enter a list element separated by space\n").split()
print("Checking input list")

base_url = "https://send.cm/"
client = cloudscraper.create_scraper(allow_brotli=False)
hs = {"Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}

for url in input_string:
        resp = client.get(url)
        scrape = BeautifulSoup(resp.text, "html.parser")
        inputs = scrape.find_all("input")
        file_id = inputs[1]["value"]
        file_name = findall("URL=(.*?) - ", resp.text)[0].split("]")[1]
        parse = {"op":"download2", "id": file_id, "referer": url}
        sleep(2)
        resp2 = client.post(base_url, data=parse, headers=hs, allow_redirects=False)
        dl_url = resp2.headers["Location"]
        dl_url = dl_url.replace(" ", "%20")
        print ("\n")
        print ("Fιℓє Nαмє: ",file_name)
        print ("Fɪʟᴇ Lɪɴᴋ: ",url)
        print ("Dᴏᴡɴʟᴏᴀᴅ Lɪɴᴋ: ",dl_url)
        print ("\n")
