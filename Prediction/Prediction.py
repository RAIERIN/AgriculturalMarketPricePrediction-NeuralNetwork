
# coding: utf-8

# In[20]:


import pickle
import numpy as np
import os
import scipy.special
import os, sys
import psycopg2
import datetime


# In[21]:


conn = psycopg2.connect("dbname=agroprediction user=erin password=admin host=localhost")
#activate connection cursor
cur = conn.cursor()


# In[22]:


today = datetime.date.today()
first = today.replace(day=1)
lastMo = first - datetime.timedelta(days=1)
lastMonth = lastMo.replace(day=1)
lastMonth


# In[23]:


a=cur.execute("SELECT name from product_detail where id=1 or id=3 or id =9 or id=27 or id=28")
name = cur.fetchall()
n = [element for tupl in name for element in tupl]
n


# In[24]:


for record in n:
    print(record)


# In[29]:


def prediction():    
    conn = psycopg2.connect("dbname=agroprediction user=erin password=admin host=localhost")
    #activate connection cursor
    cur = conn.cursor()
    for record in n: 
        if str(n[0]) == record:
            entry = open(os.path.join(sys.path[0],"Pickle/apple.pickle"), 'rb')
            data = pickle.load(entry)
            a = data['hidden and output layers']
            b = data['hidden and input layers']
            wih = b
            who = a
            entry.close()
            activation_function = lambda x: scipy.special.expit(x)
            
            def query(input_list):
                inputs= np.array(input_list, ndmin=2).T
                #calculate signals into hidden layer
                hidden_inputs = np.dot(wih, inputs)
                #calculate signals emerging from hidden layerit
                hidden_outputs = activation_function(hidden_inputs)

                #calculate signals inte tho final output layer
                final_inputs = np.dot(who, hidden_outputs)
                #calculate the signals emerging from final output layer
                final_output = activation_function(final_inputs)
            
                return final_output 
            apple=cur.execute("SELECT avg FROM product_rate WHERE date >= date_trunc('month', current_date - interval '1' month) and date < date_trunc('month', current_date) and id=3")
            input_data = cur.fetchall()             
            apple = [element for tupl in input_data for element in tupl]
            average = np.average(apple)
            inputs = (np.asfarray(apple[0:24]) / 255.0 * 0.99) + 0.01
            output = query(inputs)
            actual_output = (output * (255.0 * 0.99)) - 0.01 
            final = int(actual_output)
            predict = float(actual_output)
            
            cur.execute("INSERT INTO product_predict (id, date, prediction) VALUES (%s,%s,%s)",("1",first,final))
            cur.execute("INSERT INTO product_average (id, date, avg) VALUES (%s,%s,%s)",("1",lastMonth,average))
            print(actual_output)
            print("Apple")
        elif str(n[1]) == record:
            entry = open(os.path.join(sys.path[0],"Pickle/banana.pickle"), 'rb')   
            data = pickle.load(entry)
            a = data['hidden and output layers']
            b = data['hidden and input layers']
            wih = b
            who = a
            entry.close()
            activation_function = lambda x: scipy.special.expit(x)

            def query(input_list):
                inputs= np.array(input_list, ndmin=2).T
                #calculate signals into hidden layer
                hidden_inputs = np.dot(wih, inputs)
                #calculate signals emerging from hidden layerit
                hidden_outputs = activation_function(hidden_inputs)

                #calculate signals inte tho final output layer
                final_inputs = np.dot(who, hidden_outputs)
                #calculate the signals emerging from final output layer
                final_output = activation_function(final_inputs)

                return final_output    
            
            banana=cur.execute("SELECT avg FROM product_rate WHERE date >= date_trunc('month', current_date - interval '1' month) and date < date_trunc('month', current_date) and id=3")
            input_data = cur.fetchall()             
            banana = [element for tupl in input_data for element in tupl]
            average = np.average(banana)
            inputs = (np.asfarray(banana[0:24]) / 255.0 * 0.99) + 0.01
            output = query(inputs)
            actual_output = (output * (255.0 * 0.99)) - 0.01 
            final = int(actual_output)
            cur.execute("INSERT INTO product_predict (id, date, prediction) VALUES (%s,%s,%s)",("3",first,final))
            cur.execute("INSERT INTO product_average (id, date, avg) VALUES (%s,%s,%s)",("3",lastMonth,average))
            print(actual_output)
            print("Banana")
        elif str(n[2]) == record:
            entry = open(os.path.join(sys.path[0],"Pickle/carrot.pickle"), 'rb')   
            data = pickle.load(entry)
            a = data['hidden and output layers']
            b = data['hidden and input layers']
            wih = b
            who = a
            entry.close()
            activation_function = lambda x: scipy.special.expit(x)

            def query(input_list):
                inputs= np.array(input_list, ndmin=2).T
                #calculate signals into hidden layer
                hidden_inputs = np.dot(wih, inputs)
                #calculate signals emerging from hidden layerit
                hidden_outputs = activation_function(hidden_inputs)

                #calculate signals inte tho final output layer
                final_inputs = np.dot(who, hidden_outputs)
                #calculate the signals emerging from final output layer
                final_output = activation_function(final_inputs)

                return final_output    
            carrot=cur.execute("SELECT avg FROM product_rate WHERE date >= date_trunc('month', current_date - interval '1' month) and date < date_trunc('month', current_date) and id=9")
            input_data = cur.fetchall()             
            carrot = [element for tupl in input_data for element in tupl]
            average = np.average(carrot)
            inputs = (np.asfarray(carrot[0:24]) / 255.0 * 0.99) + 027.01
            output = query(inputs)
            actual_output = (output * (255.0 * 0.99)) - 0.01 
            final = int(actual_output)
            cur.execute("INSERT INTO product_predict (id, date, prediction) VALUES (%s,%s,%s)",("9",first,final))
            cur.execute("INSERT INTO product_average (id, date, avg) VALUES (%s,%s,%s)",("9",lastMonth,average))
            print(actual_output)
            print("Carrot")
            
        elif str(n[3]) == record:
            entry = open(os.path.join(sys.path[0],"Pickle/bigtomato.pickle"), 'rb')   
            data = pickle.load(entry)
            a = data['hidden and output layers']
            b = data['hidden and input layers']
            wih = b
            who = a
            entry.close()
            activation_function = lambda x: scipy.special.expit(x)

            def query(input_list):
                inputs= np.array(input_list, ndmin=2).T
                #calculate signals into hidden layer
                hidden_inputs = np.dot(wih, inputs)
                #calculate signals emerging from hidden layerit
                hidden_outputs = activation_function(hidden_inputs)

                #calculate signals inte tho final output layer
                final_inputs = np.dot(who, hidden_outputs)
                #calculate the signals emerging from final output layer
                final_output = activation_function(final_inputs)

                return final_output    
            bigTomato=cur.execute("SELECT avg FROM product_rate WHERE date >= date_trunc('month', current_date - interval '1' month) and date < date_trunc('month', current_date) and id=27")
            input_data = cur.fetchall()             
            bigTomato = [element for tupl in input_data for element in tupl]
            average = np.average(bigTomato)
            inputs = (np.asfarray(bigTomato[0:24]) / 255.0 * 0.99) + 0.01
            output = query(inputs)
            actual_output = (output * (255.0 * 0.99)) - 0.01 
            final = int(actual_output)
            cur.execute("INSERT INTO product_predict (id, date, prediction) VALUES (%s,%s,%s)",("27",first,final))
            cur.execute("INSERT INTO product_average (id, date, avg) VALUES (%s,%s,%s)",("27",lastMonth,average))
            print(actual_output)
            print("Big Tomato")
        
        elif str(n[4]) == record:
            entry = open(os.path.join(sys.path[0],"Pickle/smalltomato.pickle"), 'rb')   
            data = pickle.load(entry)
            a = data['hidden and output layers']
            b = data['hidden and input layers']
            wih = b
            who = a
            entry.close()
            activation_function = lambda x: scipy.special.expit(x)

            def query(input_list):
                inputs= np.array(input_list, ndmin=2).T
                #calculate signals into hidden layer
                hidden_inputs = np.dot(wih, inputs)
                #calculate signals emerging from hidden layerit
                hidden_outputs = activation_function(hidden_inputs)

                #calculate signals inte tho final output layer
                final_inputs = np.dot(who, hidden_outputs)
                #calculate the signals emerging from final output layer
                final_output = activation_function(final_inputs)

                return final_output    
            smallTomato=cur.execute("SELECT avg FROM product_rate WHERE date >= date_trunc('month', current_date - interval '1' month) and date < date_trunc('month', current_date) and id=28")
            input_data = cur.fetchall()             
            smallTomato = [element for tupl in input_data for element in tupl]
            average = np.average(smallTomato)
            inputs = (np.asfarray(smallTomato[0:24]) / 255.0 * 0.99) + 0.01
            output = query(inputs)
            actual_output = (output * (255.0 * 0.99)) - 0.01 
            final = int(actual_output)
            cur.execute("INSERT INTO product_predict (id, date, prediction) VALUES (%s,%s,%s)",("28",first,final))
            cur.execute("INSERT INTO product_average (id, date, avg) VALUES (%s,%s,%s)",("28",lastMonth,average))
            conn.commit()
            cur.close()
            conn.close()
            print(actual_output)
            print("Small Tomato")



# In[30]:


prediction()


# In[57]:




