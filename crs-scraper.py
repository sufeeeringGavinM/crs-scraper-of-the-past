from selenium import webdriver
import os
import codecs
#set chromedriver.exe path
driver = webdriver.Chrome()
#launch URL

import string

# change years as you will
years = range(2000, 2025)  # inclusive (i.e., in this case it includes years 2000-2001 and 2025-2026)
digits = ["1", "2", "4"]
letters = list(string.ascii_uppercase)

permutations = []
permutations2=[]
for year in years:
    for d in digits:
        for letter in letters:
            permutations.append(f"1{year}{d}/{letter}")

for year in years:
    for d in digits:
        for letter in letters:
            permutations2.append(f"{year}-{year+1} {d}-{letter}")         

where_Ya_wantit_Boss='It-all-be-saved-here'

if where_Ya_wantit_Boss not in os.listdir():
    os.mkdir(where_Ya_wantit_Boss)

for x in range(0,2886):
    driver.get("https://crs.upd.edu.ph/schedule/"+ permutations[x])
    #get file path to save page
    driver.implicitly_wait(0.1)
    n=os.path.join(os.getcwd()+'\\It-all-be-saved-here',permutations2[x]+".html")
    #open file in write mode with encoding
    f = codecs.open(n, "w", "utf−8")
    #obtain page source
    h = driver.page_source
    #write page source content to file
    f.write(h)
    print("Downloaded", permutations2[x])
#close browser
driver.quit()

# Dutifully copy pasted from other sources I will not name. Fuck you

# From the future here, sorry to those I've possibly stolen from.
# Uhm. It was from a bunch of stack exchange answers, I'm guessing.
