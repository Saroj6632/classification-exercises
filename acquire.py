#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import env
import os


# In[2]:


def get_connection(db, user=env.username, host=env.host, password=env.password):
    return f'mysql+pymysql://{env.username}:{env.password}@{env.host}/{db}'


# In[3]:


# Make a function named get_titanic_data that returns the titanic data from the codeup data science database as a pandas data frame.
# Obtain your data from the Codeup Data Science Database.


# In[4]:


titanic_df = pd.read_sql('Select * from passengers', get_connection('titanic_db'))
titanic_df.head(1)


# In[5]:


# returns titanic data from codeup data science database
def get_titanic_data():
    return titanic_df


# In[6]:


get_titanic_data()


# In[7]:


# Make a function named get_iris_data that returns the data from the iris_db on the codeup data science database as a pandas data frame. 
# The returned data frame should include the actual name of the species in addition to the species_ids. 
# Obtain your data from the Codeup Data Science Database.


# In[8]:


sql= '''select * from measurements 
join species using (species_id)
'''
iris_db = pd.read_sql(sql, get_connection('iris_db'))
iris_db.head()


# In[9]:


def get_iris_data():
    return iris_db

get_iris_data()


# In[10]:


# Make a function named get_telco_data that returns the data from the telco_churn database in SQL. 
# In your SQL, be sure to join all 4 tables together, so that the resulting dataframe contains all the contract, payment, and internet service options.
# Obtain your data from the Codeup Data Science Database.


# In[11]:


sql= ''' select * from customers
join customer_payments using(payment_type_id)
join internet_service_types using(internet_service_type_id)
join customer_contracts using(contract_type_id)
'''


# In[ ]:


telco_db = pd.read_sql(sql, get_connection('telco_churn'))
telco_db.head()


# In[ ]:


def get_telco_data():
    return telco.db

get_telco_data()


# ###  Once you've got your get_titanic_data, get_iris_data, and get_telco_data functions written, now it's time to add caching to them. To do this, edit the beginning of the function to check for the local filename of telco.csv, titanic.csv, or iris.csv. If they exist, use the .csv file. If the file doesn't exist,  then produce the SQL and pandas necessary to create a dataframe, then write the dataframe to a .csv file with the appropriate name.

# In[ ]:


def get_titanic_data():
    filename = "titanic.csv"
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        titanic_df = pd.read_sql('Select * from passengers', get_connection('titanic_db'))
        titanic_df.to_file(filename)
        return titanic_df
    


# In[ ]:


def get_iris_data():
    filename = "iris.csv"
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        iris_db = pd.read_sql('select * from measurements join species using (species_id)', get_connection('iris_db'))
        titanic_df.to_file(filename)
        return titanic_df


# In[ ]:


def get_telco_data():
    filename= "telco.csv"
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        telco_db = pd.read_sql('''select * from customers
                                  join customer_payments using(payment_type_id)
                                  join internet_service_types using(internet_service_type_id)
                                  join customer_contracts using(contract_type_id)''', get_connection('telco_churn'))

        telco_db.tofile(filename)
        return telco.db


# In[ ]:




