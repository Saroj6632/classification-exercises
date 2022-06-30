#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import env
import os


# In[2]:


def get_connection(db, user=env.username, host=env.host, password=env.password):
    return f'mysql+pymysql://{env.username}:{env.password}@{env.host}/{db}'


# In[3]:


# Make a function named get_titanic_data that returns the titanic data from the codeup data science database as a pandas data frame.
# Obtain your data from the Codeup Data Science Database.


# In[ ]:





# In[4]:


# returns titanic data from codeup data science database
def new_titanic_data():
    sql='Select * from passengers'
    df = pd.read_sql(sql, get_connection('titanic_db'))
                        
    
    
    return df


# In[5]:


new_titanic_data()


# In[6]:


# Make a function named get_iris_data that returns the data from the iris_db on the codeup data science database as a pandas data frame. 
# The returned data frame should include the actual name of the species in addition to the species_ids. 
# Obtain your data from the Codeup Data Science Database.


# In[8]:


def iris_data():
    sql= '''
        select * from measurements 
        join species using (species_id)
        '''
    df = pd.read_sql(sql, get_connection('iris_db'))
    return df

iris_data()


# In[ ]:


# Make a function named get_telco_data that returns the data from the telco_churn database in SQL. 
# In your SQL, be sure to join all 4 tables together, so that the resulting dataframe contains all the contract, payment, and internet service options.
# Obtain your data from the Codeup Data Science Database.


# In[10]:


def new_telco_data():
    sql_query = """
                select * from customers
                join contract_types using (contract_type_id)
                join internet_service_types using (internet_service_type_id)
                join payment_types using (payment_type_id)
                """
    
    # Read in DataFrame from Codeup db.
    df = pd.read_sql(sql_query, get_connection('telco_churn'))
    
    return df

new_telco_data().head()


# In[ ]:





# ###  Once you've got your get_titanic_data, get_iris_data, and get_telco_data functions written, now it's time to add caching to them. To do this, edit the beginning of the function to check for the local filename of telco.csv, titanic.csv, or iris.csv. If they exist, use the .csv file. If the file doesn't exist,  then produce the SQL and pandas necessary to create a dataframe, then write the dataframe to a .csv file with the appropriate name.

# In[17]:


# below reads iris database from codeup, writes data to csv file if local file doenot exist
def get_titanic_data():
    filename = "titanic.csv"
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        df = new_titanic_data()
        df.to_csv(filename)
        return df
    

    


# In[18]:


titanic= get_titanic_data()
titanic.head()


# In[15]:


# function below reads iris database from codeup, writes data to csv file if local file doenot exist
def get_iris_data():
    filename = "iris.csv"
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        df= iris_data()  # data from dataframe
        df.to_csv(filename)    #cache data
        return df


# In[16]:


get_iris_data().head()


# In[24]:


def get_telco_data():
    filename= "telco.csv"
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        df= new_telco_data()
        df.to_csv(filename)
        return df


# In[25]:


get_telco_data().head()


# In[ ]:




