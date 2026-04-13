#main module of this entire code 
import requests
#scans the website given with a file containing the common directory names and scans it with those
def Scanner(website):
    with open(r"Place your common.txt file here either use the name directly or js copy file path(delete this entire thing within string)","r") as f:
     words = f.read().splitlines()
    for word in words:
         Url =website + "/" + word
         response = requests.get(Url)
         print(response.status_code)
         if response.status_code == 200:
          print(f"found: {Url}")



Website = input("enter your desired Site:")
Scanner(Website)
    











