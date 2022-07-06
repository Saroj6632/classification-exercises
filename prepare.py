#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import acquire
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer


# In[2]:


def train_validate_test_split(df, target, seed=123):
    '''
    This function takes in a dataframe, the name of the target variable
    (for stratification purposes), and an integer for a setting a seed
    and splits the data into train, validate and test. 
    Test is 20% of the original dataset, validate is .30*.80= 24% of the 
    original dataset, and train is .70*.80= 56% of the original dataset. 
    The function returns, in this order, train, validate and test dataframes. 
    '''
    train_validate, test = train_test_split(df, test_size=0.2, 
                                            random_state=seed, 
                                            stratify=df[target])
    train, validate = train_test_split(train_validate, test_size=0.2, 
                                       random_state=seed,
                                       stratify=train_validate[target])
    return train, validate, test


# In[3]:


def prep_titanic_data(df):
    df= df.drop_duplicates()
    df= df.drop(columns=['Unnamed: 0','deck','age','embarked','class'])
    df['embark_town']= df.embark_town.fillna(value='southampton')
    dummy_df= pd.get_dummies(df[['sex','embark_town']], dummy_na=False, drop_first=[True,True])
    df= pd.concat([df,dummy_df], axis=1)
    return df


# In[4]:


def prep_iris(df):
    df = df.drop(columns=['species_id','measurement_id','Unnamed: 0'])
    df = df.rename(columns={'species_name':'species'})
    dummy_df = pd.get_dummies(df['species'],dummy_na=False, drop_first=True)
    df= pd.concat([df, dummy_df], axis=1)
    return df


# In[5]:


def prep_telco(df):
    df=df.drop_duplicates()
    df = df.drop(columns=['Unnamed: 0','contract_type_id','internet_service_type_id','payment_type_id'])
    dummy_df= pd.get_dummies(df[['gender','partner','dependents','phone_service','multiple_lines','online_security','online_backup','device_protection','tech_support','streaming_tv','streaming_movies','paperless_billing','churn','contract_type','internet_service_type','payment_type']],dummy_na=False, drop_first=[True * 16])
    df= pd.concat([df, dummy_df],axis=1)
    df['total_charges']= df.total_charges.str.strip().replace('',0).astype(float)
    return df


# In[ ]:




