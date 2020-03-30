
# coding: utf-8

# In[5]:

import psycopg2
import bs4 as bs
import urllib.request
import string
from datetime import datetime
def prediction():
    #connection to database
    conn = psycopg2.connect("dbname=agroprediction user=erin password=admin host=localhost")
    #activate connection cursor
    cur = conn.cursor()

    #getting the data from url
    sauce = urllib.request.urlopen('http://agribiz.gov.np/dailyprice/pricelist/kalimati.app').read()
    soup = bs.BeautifulSoup(sauce,'lxml')

    #getting the table data from the url
    prices = []
    table_rows = soup.find_all('tr')
    s=0
    for tr in table_rows:
            td = tr.find_all('td')
            row = [i.text for i in td]
            print(row)
            value=row[0:6]
            prices.append(value)
            s= s+1

    #formatting the data for filteration of important data
    map(str.rstrip, prices)
    price = prices[4:]

    #removing the empty data from the list
    final_price = []
    for list in price:
        if len(list) != 0:
            final_price.append(list)

    #inserting into the database        
    d = datetime.now()
    date = d.date()
    for p in final_price: 
        mini=float(p[4])
        maxi=float(p[5])
        avg = (mini + maxi)/2
        mi = str(mini)
        ma = str(maxi)
        av = str(avg)
        cur.execute("INSERT INTO product_rate (id, date, min, max, avg) VALUES (%s,%s,%s,%s,%s)",(p[0],date,mini,maxi,avg))
        conn.commit()

    cur.close()
    conn.close()
    
prediction()
