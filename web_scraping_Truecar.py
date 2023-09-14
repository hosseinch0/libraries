from bs4 import BeautifulSoup
import requests
import re

# THIS IS A SIMPLE LIST FOR OUR RETRIEVED DATA FROM SCRAPING
storage_list = list()


# YOU ENTER A CAR BRAND AND IT SEARCHES THROUGH THE WEBSITE
car_brand = str(input())


# THE CAR BRAND GETS ATTACHED TO END OF THE URL
URL = "https://www.truecar.com/used-cars-for-sale/listings/%s/" % car_brand


# GET REQUEST WILL BE SENT
req = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
req_status = req.status_code


# CHECKS THE STATUS OF THE REQUEST
if req_status == 200:
    # WE MAKE OUR SOUP HERE
    soup = BeautifulSoup(req.content, "html.parser")

    # TRYING TO FIND THE SPECIFIC PART THAT WE WANT IN THE SOUP
    result = soup.find_all(
        "div", class_="linkable card card-shadow vehicle-card")

    # BECAUSE WE HAVE MULTIPLE RESULTS FOR LOOP IS BEING USED
    for res in result:
        txt = res.text

        # THIS PART I USED REGEX THAT ONLY WORKS FOR THIS SPECIFIC SCRIPT OBVIOUSLY
        # IF YOU DON'T KNOW HOW TO USE REGEX SEARCH IN MY WEBSITE TI LEARN ABOUT IT
        regexTemp = re.findall(
            r'[\d\w](\$+\d*\,\d{3})(\d*\,\d*\w\ \w*)', txt)

        # ADD THE FILTERED VALUES TO THE LIST THAT DECLARED ABOVE
        storage_list.append(regexTemp)

    # LOOPING THROUGH THE LIST
    for element in storage_list:
        if element:
            print(element)


else:
    # ANY STATUS EXCEPT 200 DON'T FORGET 403 MEANS FORBIDDEN SO YOU MAY NEED TO USE A V.P.N OR ANYTHING THAT CHANGES YOUR IP
    print(req_status)
