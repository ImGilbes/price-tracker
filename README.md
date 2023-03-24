# How to use
---
### On Windows
- Be sure to have python installed (better if >=3.7)
- run install-req.bat or optionally run `pip install -r requirements.txt`
- set up the user agent simply by googling "my user agent" and replacing the values in the useragent.txt file
- Now add URLs to your item list, item lists are different for each website
- Now run the tracker for the specific website
- The prices will be show for every website and every item you're keeping track of
- To add a new item just add the URL to the list
- To remove an item, remove the URL from the list, then delete its file from the tracked folder
---
### On Ubuntu
* Open current folder in terminal (right click -> open in terminal)
* run `bash install-req.sh`
* set up the user agent simply by googling "my user agent" and replacing the values in the useragent.txt file
* execute the tracker with `bash amazon-tracker.sh` or `bash ebay-tracker.sh` or any `bash {vendor}-tracker.sh`
---
* In the .csv file the price are reported in chronological oreder. Thta mean that the last line of the file should always be the newest, whereas the first line is the oldest.

* Use tracker to update the newset prices, then plot with analyzer

+ Ease of use: select the desired .bat file
Each vendor has a separate .bat and a separate itemslist
