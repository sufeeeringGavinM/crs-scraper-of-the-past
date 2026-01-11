# Description

Ever wanted to just download the entirety of UP Diliman's class schedules from the past and present? Well, here you've got that. Personally, I use this to see if there are any professors that only take certain time slots to "bypass" the CONCEALED thing.

The first, simply downloads every year specified (Read the .py file) and all letters as separate HTML files. For example, for the academic year 2000-2001, 1st semester, subjects starting sith letter B... this would be saved as 2000-2001 1-B.html

The second, downloads each year as a folder, wherein you can then use index.html within the folder to navigate the year through clicks and all. That is, you're able to click through the letters yourself.

# Installation

1. Install Python and Chrome

2. Install the requirements using the following command while your terminal/command prompt window is in the same folder as the included requirements.txt.
```python
pip install -r requirements.txt
```
3. Place the scrapers in some folder. Launch from there and it'll just save in a subfolder depending on which you use.

# Usage

Open whichever scraper you want. First version is titled crs-scraper.py, second is titled crs-scraper-2.0.py. 

First one opens a chrome browser to do the stuff (ie visit each webpage, download webpage, go to next, repeat etc) so don't be scared. Second one does stuff fully in Python but takes fucking forever so that's that.

A folder will be created within the folder you put the scraper in depending on which scraper you use. Delete them if you wanna run the scrapers again for some reason.
