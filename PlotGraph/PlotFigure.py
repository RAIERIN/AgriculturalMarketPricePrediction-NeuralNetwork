
# coding: utf-8

# In[47]:


import psycopg2
from datetime import datetime
import numpy as np
import random
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


# In[50]:


conn = psycopg2.connect("dbname=agroprediction user=erin password=admin host=localhost")
#activate connection cursor
cur = conn.cursor()
a=cur.execute("SELECT name from product_detail where id=1 or id=3 or id =9 or id=27 or id=28")
name = cur.fetchall()
n = [element for tupl in name for element in tupl]

def plotgraph():
    conn = psycopg2.connect("dbname=agroprediction user=erin password=admin host=localhost")
    #activate connection cursor
    cur = conn.cursor()
    for record in n: 
        if str(n[0]) == record:
            predit_date=cur.execute("SELECT date from product_predict where id=1 order by date asc")
            date_predict = cur.fetchall()
            predictdate = [element for tupl in date_predict for element in tupl]
            avg_date=cur.execute("SELECT date from product_average where id=1 order by date asc")
            date_avg = cur.fetchall()
            avgdate = [element for tupl in date_avg for element in tupl]
            prod_avg=cur.execute("SELECT avg from product_average where id=1 order by date asc")
            avg = cur.fetchall()
            average = [element for tupl in avg for element in tupl]
            c=cur.execute("SELECT prediction from product_predict where id=1 order by date asc")
            pred = cur.fetchall()
            predict = [element for tupl in pred for element in tupl]

            fig = plt.figure()
            ax = fig.add_axes([0,0,1,1])
            p1 = ax.plot(predictdate,predict, 'r--')
            p2 = ax.plot(avgdate,average, 'b',)
            plt.legend((p1[0], p2[0]), ('Predicted Price', 'Actual Price'))
            ax.set_xlabel('Date')
            ax.set_ylabel('Rate (Rs.)')
            ax.set_title('Prediction Vs Actual')
            apple = fig.savefig(r'C:\Fyp\Development\API\static\images\apple.png', bbox_inches='tight')
        elif str(n[1]) == record:
            predit_date=cur.execute("SELECT date from product_predict where id=3 order by date asc")
            date_predict = cur.fetchall()
            predictdate = [element for tupl in date_predict for element in tupl]
            avg_date=cur.execute("SELECT date from product_average where id=3 order by date asc")
            date_avg = cur.fetchall()
            avgdate = [element for tupl in date_avg for element in tupl]
            prod_avg=cur.execute("SELECT avg from product_average where id=3 order by date asc")
            avg = cur.fetchall()
            average = [element for tupl in avg for element in tupl]
            c=cur.execute("SELECT prediction from product_predict where id=3 order by date asc")
            pred = cur.fetchall()
            predict = [element for tupl in pred for element in tupl]

            fig = plt.figure()
            ax = fig.add_axes([0,0,1,1])
            p1 = ax.plot(predictdate,predict, 'r--')
            p2 = ax.plot(avgdate,average, 'b',)
            plt.legend((p1[0], p2[0]), ('Predicted Price', 'Actual Price'))
            ax.set_xlabel('Date')
            ax.set_ylabel('Rate (Rs.)')
            ax.set_title('Prediction Vs Actual')
            apple = fig.savefig(r'C:\Fyp\Development\API\static\images\banana.png', bbox_inches='tight')
        elif str(n[2]) == record:
            predit_date=cur.execute("SELECT date from product_predict where id=9 order by date asc")
            date_predict = cur.fetchall()
            predictdate = [element for tupl in date_predict for element in tupl]
            avg_date=cur.execute("SELECT date from product_average where id=9 order by date asc")
            date_avg = cur.fetchall()
            avgdate = [element for tupl in date_avg for element in tupl]
            prod_avg=cur.execute("SELECT avg from product_average where id=9 order by date asc")
            avg = cur.fetchall()
            average = [element for tupl in avg for element in tupl]
            c=cur.execute("SELECT prediction from product_predict where id=9 order by date asc")
            pred = cur.fetchall()
            predict = [element for tupl in pred for element in tupl]

            fig = plt.figure()
            ax = fig.add_axes([0,0,1,1])
            p1 = ax.plot(predictdate,predict, 'r--')
            p2 = ax.plot(avgdate,average, 'b',)
            plt.legend((p1[0], p2[0]), ('Predicted Price', 'Actual Price'))
            ax.set_xlabel('Date')
            ax.set_ylabel('Rate (Rs.)')
            ax.set_title('Prediction Vs Actual')
            apple = fig.savefig(r'C:\Fyp\Development\API\static\images\carrot.png', bbox_inches='tight')
        elif str(n[3]) == record:
            predit_date=cur.execute("SELECT date from product_predict where id=27 order by date asc")
            date_predict = cur.fetchall()
            predictdate = [element for tupl in date_predict for element in tupl]
            avg_date=cur.execute("SELECT date from product_average where id=27 order by date asc")
            date_avg = cur.fetchall()
            avgdate = [element for tupl in date_avg for element in tupl]
            prod_avg=cur.execute("SELECT avg from product_average where id=27 order by date asc")
            avg = cur.fetchall()
            average = [element for tupl in avg for element in tupl]
            c=cur.execute("SELECT prediction from product_predict where id=27 order by date asc")
            pred = cur.fetchall()
            predict = [element for tupl in pred for element in tupl]

            fig = plt.figure()
            ax = fig.add_axes([0,0,1,1])
            p1 = ax.plot(predictdate,predict, 'r--')
            p2 = ax.plot(avgdate,average, 'b',)
            plt.legend((p1[0], p2[0]), ('Predicted Price', 'Actual Price'))
            ax.set_xlabel('Date')
            ax.set_ylabel('Rate (Rs.)')
            ax.set_title('Prediction Vs Actual')
            apple = fig.savefig(r'C:\Fyp\Development\API\static\images\bigtomato.png', bbox_inches='tight')
        elif str(n[4]) == record: 
            predit_date=cur.execute("SELECT date from product_predict where id=28 order by date asc")
            date_predict = cur.fetchall()
            predictdate = [element for tupl in date_predict for element in tupl]
            avg_date=cur.execute("SELECT date from product_average where id=28 order by date asc")
            date_avg = cur.fetchall()
            avgdate = [element for tupl in date_avg for element in tupl]
            prod_avg=cur.execute("SELECT avg from product_average where id=28 order by date asc")
            avg = cur.fetchall()
            average = [element for tupl in avg for element in tupl]
            c=cur.execute("SELECT prediction from product_predict where id=28 order by date asc")
            pred = cur.fetchall()
            predict = [element for tupl in pred for element in tupl]

            fig = plt.figure()
            ax = fig.add_axes([0,0,1,1])
            p1 = ax.plot(predictdate,predict, 'r--')
            p2 = ax.plot(avgdate,average, 'b',)
            plt.legend((p1[0], p2[0]), ('Predicted Price', 'Actual Price'))
            ax.set_xlabel('Date')
            ax.set_ylabel('Rate (Rs.)')
            ax.set_title('Prediction Vs Actual')
            apple = fig.savefig(r'C:\Fyp\Development\API\static\images\smalltomato.png', bbox_inches='tight')


# In[51]:


plotgraph()


# In[28]:





# In[37]:





# In[38]:





# In[35]:





# In[45]:





# In[46]:




