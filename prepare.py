#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import acquire
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer


# # Using the Iris Data:
# 
# - ### Use the function defined in acquire.py to load the iris data.
# 
# - ### Drop the species_id and measurement_id columns.
# 
# - ### Rename the species_name column to just species.
# 
# - ### Create dummy variables of the species name and concatenate onto the iris dataframe. (This is for practice, we don't always have to encode the target, but if we used species as a feature, we would need to encode it).
# 
# - ### Create a function named prep_iris that accepts the untransformed iris data, and returns the data with the transformations above applied.

# In[2]:


df = acquire.get_iris_data()
df.head()


# In[3]:


df.info()


# In[4]:


## dropped species_id, measeurement_id and unnamed columns from data frame
df = df.drop(columns=['species_id','measurement_id','Unnamed: 0'])
df.head()


# In[5]:


# renaming the species column
df = df.rename(columns={'species_name':'species'})
df.head()


# In[6]:


## creating a dummy variables for species name
dummy_df = pd.get_dummies(df['species'])
dummy_df.head()


# In[7]:


dummy_df = pd.get_dummies(df['species'],dummy_na=False, drop_first=True)
dummy_df.head()


# In[8]:


# concat dummy dataframe  with our original dataframe
df= pd.concat([df, dummy_df], axis=1)
df.head()


# In[9]:


'''This function cleans the data as done in above sequence
'''
def clean_data(df):
    df = df.drop(columns=['species_id','measurement_id','Unnamed: 0'])
    df = df.rename(columns={'species_name':'species'})
    dummy_df = pd.get_dummies(df['species'],dummy_na=False, drop_first=True)
    df= pd.concat([df, dummy_df], axis=1)
    return df


# In[10]:


df= acquire.get_iris_data()
df.head()


# In[11]:


df= clean_data(df)
df.head()


# In[12]:


# splitting data to 20% test, 80%=(70% train,30% validate)
train, test = train_test_split(df, test_size = .2, random_state=123, stratify=df.species)
print(train.shape, test.shape)


# In[13]:


train, validate= train_test_split(train, test_size=.2,random_state=123, stratify=train.species)
print(f'Train:{train.shape}\n.....\nValidate:{validate.shape}\n.....\nTest:{test.shape}')


# In[14]:


def split_data(df):
    train, test = train_test_split(df, test_size = .2, random_state=123, stratify=df.species)
    train, validate= train_test_split(train, test_size=.2,random_state=123, stratify=train.species)
    return train,validate,test


# In[18]:


train,validate,test= split_data(df)
print('Train:',train.shape)
print('Validate:' ,validate.shape)
print('Test:',test.shape)


# In[20]:


def prep_iris(df):
    df= clean_data(df)
    train,validate,test= split_data(df)
    return train,validate,test
    


# In[21]:


df= acquire.get_iris_data()
df.head()


# In[25]:


prep_iris(df)
train.info()


# # Using the Titanic dataset
# 
# - ### Use the function defined in acquire.py to load the Titanic data.
# 
# - ### Drop any unnecessary, unhelpful, or duplicated columns.
# 
# - ### Encode the categorical columns. Create dummy variables of the categorical columns and concatenate them onto the dataframe.
# 
# - ### Create a function named prep_titanic that accepts the raw titanic data, and returns the data with the transformations above applied.

# In[39]:


# calling function get_titanic_data from acquire.py module

df = acquire.get_titanic_data()
df.head()


# In[40]:


# no of rows and columns of original dataframe
df.shape


# In[41]:


df.info()


# In[42]:


# dropping  duplicates. shows no duplicates
df= df.drop_duplicates()
print(df.shape)


# In[43]:


#missing values in the dataframe columns
missing= df.isnull().sum()
missing[missing>0]


# In[44]:


# droppping unnecessary columns
df = df.drop(columns=['Unnamed: 0','deck','age','embarked','class'])
df.head()


# In[45]:


# using .fillna() to the embark_town columns and validated the missing values has been adjusted
df['embark_town']= df.embark_town.fillna(value='Southampton')
df.embark_town.isna().sum()


# In[46]:


dummy_df = pd.get_dummies(df[['sex','embark_town']], dummy_na= False, drop_first=[True, True])
dummy_df.head()


# In[47]:


# add dummy datframe to dtaframe horizontally
df = pd.concat([df, dummy_df], axis=1)
df.head()


# In[48]:


# the function below  returns the data that has all the transformations applied above
def clean_data(df):
    df= df.drop_duplicates()
    df= df.drop(columns=['Unnamed: 0','deck','age','embarked','class'])
    df['embark_town']= df.embark_town.fillna(value='southampton')
    dummy_df= pd.get_dummies(df[['sex','embark_town']], dummy_na=False, drop_first=[True,True])
    df= pd.concat([df,dummy_df], axis=1)
    return df
    
    
    

    


# In[49]:


df = acquire.get_titanic_data()
df.head()


# In[50]:


df = clean_data(df)
df.head()


# In[66]:


# splitting data
# 20 % test, 80% validat& train
train, test = train_test_split(df, test_size = .2, random_state=123, stratify=df.survived)
print(train.shape, test.shape)


# In[67]:


#split train from previous code to 30% validate,70% train
train, validate = train_test_split(train, test_size=.3, random_state=123, stratify=train.survived)


# In[68]:


print(f'Train:{train.shape}\n.....\nValidate:{validate.shape}\n.....\nTest:{test.shape}')


# In[61]:


def split_data(df):
    train, test = train_test_split(df, test_size = .2, random_state=123, stratify=df.survived)
    train, validate = train_test_split(train, test_size=.3, random_state=123, stratify=train.survived)
    return train, validate, test


# In[62]:


imputer = SimpleImputer(strategy='most_frequent')
imputer


# In[63]:


imputer= imputer.fit(train[['embark_town']])
imputer


# In[60]:


# using imputer to transform the column with null values
train[['embark_town']] = imputer.transform(train[['embark_town']])

validate[['embark_town']] = imputer.transform(validate[['embark_town']])

test[['embark_town']] = imputer.transform(test[['embark_town']])


# In[ ]:


# this function helps to replace the nulls in embark_town
def impute_mode(train, validate, test):
    imputer = SimpleImputer(strategy='most_frequent')
    train[['embark_town']] = imputer.transform(train[['embark_town']])
    validate[['embark_town']] = imputer.transform(validate[['embark_town']])
    test[['embark_town']] = imputer.transform(test[['embark_town']])
    return train,validate,test


# In[64]:


def prep_titanic_data(df):
    df= clean_data(df)
    train, validate, test = split_data(df)
    return train, validate, test
    


# In[70]:


df= acquire.get_titanic_data()
train, validate,test = prep_titanic_data(df)
print(f'train:{train.shape},\nvalidate:{validate.shape},\ntest:{test.shape}')


# In[71]:


train.info()


# # Using the Telco dataset
# 
# - ### Use the function defined in acquire.py to load the Telco data.
# 
# - ### Drop any unnecessary, unhelpful, or duplicated columns. This could mean dropping foreign key columns but keeping the corresponding string values, for example.
# 
# - ### Encode the categorical columns. Create dummy variables of the categorical columns and concatenate them onto the dataframe.
# 
# - ### Create a function named prep_telco that accepts the raw telco data, and returns the data with the transformations above applied.

# In[143]:


df= acquire.get_telco_data()
df.head()


# In[144]:


print(df.shape)
print(df.info())


# In[145]:


# just to make sure there is no duplicates and missing values even tho it is claear from .shape that there is no missing values in the data frame
df= df.drop_duplicates()
print(df.shape)


# In[146]:


df.total_charges


# In[147]:


missing= df.isnull().sum()
missing[missing>0]
# no any missing values in the columns


# In[148]:


# removing unwanted coluimns from the dataframe
df = df.drop(columns=['Unnamed: 0','contract_type_id','internet_service_type_id','payment_type_id'])
df.head()


# In[149]:


print(df.shape)


# In[150]:


df.info()


# In[151]:


dummy_df= pd.get_dummies(df[['gender','partner','dependents','phone_service','multiple_lines','online_security','online_backup','device_protection','tech_support','streaming_tv','streaming_movies','paperless_billing','churn','contract_type','internet_service_type','payment_type']],dummy_na=False, drop_first=[True * 16])
dummy_df.head()


# In[152]:


dummy_df.shape


# In[153]:


df= pd.concat([df, dummy_df],axis=1)
df.head()


# In[154]:


df.shape


# In[159]:


#converting total_charges column to float from object type
df['total_charges']= df.total_charges.str.strip().replace('',0).astype(float)


# In[163]:


df['total_charges'].dtypes


# In[164]:


# function to clean the data
def clean_data(df):
    df=df.drop_duplicates()
    df = df.drop(columns=['Unnamed: 0','contract_type_id','internet_service_type_id','payment_type_id'])
    dummy_df= pd.get_dummies(df[['gender','partner','dependents','phone_service','multiple_lines','online_security','online_backup','device_protection','tech_support','streaming_tv','streaming_movies','paperless_billing','churn','contract_type','internet_service_type','payment_type']],dummy_na=False, drop_first=[True * 16])
    df= pd.concat([df, dummy_df],axis=1)
    df['total_charges']= df.total_charges.str.strip().replace('',0).astype(float)
    return df
    

    
    


# In[165]:


df = acquire.get_telco_data()
df.head()


# In[166]:


df= clean_data(df)
df.head()


# In[178]:


train, test = train_test_split(df, test_size = .2, random_state=123, stratify=df.churn)
print(train.shape, test.shape)


# In[179]:


train, validate = train_test_split(train, test_size=.3, random_state=123, stratify=train.churn)
print(train.shape,validate.shape, test.shape)


# In[180]:


def split_data(df):
    train, test = train_test_split(df, test_size = .2, random_state=123, stratify=df.churn)
    train, validate = train_test_split(train, test_size=.3, random_state=123, stratify=train.churn)
    return train, validate,test


# In[181]:


train, validate, test = split_data(df)
print(train.shape,validate.shape, test.shape)


# In[182]:


def prep_telco(df):
    df= clean_data(df)
    train, validate, test = split_data(df)
    return train, validate, test
    


# In[183]:


df= acquire.get_telco_data()
df.head()


# In[184]:


prep_telco(df)


# In[185]:


train.info()


# In[ ]:


#df.total_charges = df.total_charges.str.strip().replace('',0).astype(float)
#telco_df[telco_df.isnull().any(axis=1)]

