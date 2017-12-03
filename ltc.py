import os
import sys
import json
import time
import requests

currency = sys.argv[1].upper()

url = r"https://api.coinbase.com/v2/prices/LTC-{currency}/spot"

btc = requests.get(url.format(currency=currency)).json()

#Add a for difference in check
first_date = last_date = str(time.time())
first_price = last_price = float(btc["data"]["amount"])

print "First: "+str(first_price)+" "+currency+" - "+first_date

lower_limit = 50
sleep_time = 1

while True:
    btc = requests.get(url.format(currency=currency)).json()
    date = time.time()
    price = float(btc["data"]["amount"])
    out = str(price)+" "+currency
    
    last_diff = ""
    total_diff = ""
    if last_date != date and last_price != price:
        #Update sleep time for API calls
        sleep_time = 60

        if price < last_price:
            #os.system("afplay /System/Library/Sounds/Submarine.aiff")
            last_percentage = "-"+str(100-round(price/last_price*100,2))
            last_colour = 31
        else:
            #os.system("afplay /System/Library/Sounds/Pop.aiff")
            last_percentage = "+"+str(round(price/last_price*100,2)-100)
            last_diff = "+"
            last_colour = 32
        
        if price < lower_limit:
            os.system("afplay \"~/Sounds/popoff.mp3\"")
        
        if price < first_price:
            total_percentage = "-"+str(100-round(price/first_price*100,2))
            total_colour = 31
        else:
            total_percentage = "+"+str(round(price/first_price*100,2)-100)
            total_diff = "+"
            total_colour = 32
    
        last_diff = last_diff + str(price - last_price)+" ("+last_percentage+"%)"
        last_diff = "\x1b[{colour}m{text}L\x1b[0m".format(colour=last_colour, text=last_diff)
        
        total_diff = total_diff + str(price - first_price)+" ("+total_percentage+"%)"
        total_diff = "\x1b[{colour}m{text}T\x1b[0m".format(colour=total_colour, text=total_diff)
        
        diff = last_diff+" - "+total_diff + ": "

        last_date = date
        last_price = price
        
        with open("./ltc-"+currency+".txt", "a") as file:
            file.write(str(date)+":"+str(price)+":"+currency + os.linesep)
            print diff+out

    time.sleep(sleep_time)
