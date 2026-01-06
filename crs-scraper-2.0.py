from pywebcopy import save_website
import os
import string

years = range(2000, 2002)  # inclusive (i.e., in this case it includes years 2000-2001 and 2025-2026)
#digits = ["1", "2", "4"] # this includes the midyear
digits = ["1", "2"]
permutations = []
permutations2=[]
for year in years:
    for d in digits:
        permutations.append(f"1{year}{d}/")

for year in years:
    for d in digits:
        permutations2.append(f"{year}-{year+1}-{d}")   

for x in range(0,2886): # An utterly lazy way of just looping through all. The program ends with an IndexError intentionally. Handle exceptions instead? No. Beautiful.
    save_website(
        url = "https://crs.upd.edu.ph/schedule/"+permutations[x],
        project_folder=os.getcwd()+'\\Scraper-2.0-Results',
        project_name=permutations2[x],
        bypass_robots=True,
        debug=False,
        open_in_browser=False,
        delay=None,
        threaded=False,
    )


