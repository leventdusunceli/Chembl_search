#!/usr/bin/env python
# coding: utf-8

# # Searching for Chemical Structures from ChEMBL Database 

# ChEMBL is a database for chemical molecules that are active against certain proteins and possess drug-like properties. (https://www.ebi.ac.uk/chembl/) 
# 
# Database consists of over 2 million unique compounds showing bioactivity against over 14 thousand targets.
# 
# In this notebook, I'll demonstrate how to search biologically active compounds for a specific target using Python. 
# 
# ChEMBL has a very user-friendly website, however using Python to query searches is more convenient for compiling search results and filtering out certain properties of compounds.  

# ## Installing ChEMBL webresource client and necessary packages

# In[ ]:


#This is the official Python client library and will allow us to access ChEMBL from Python

get_ipython().system('pip install chembl_webresource_client')

from chembl_webresource_client.new_client import new_client 

#We'll also need pandas to perform certain operations on the results 

import pandas as pd 


# ## Searching for a target protein
# 
# First we'll select a target protein from the database. 
# 
# new_client.target.search() function is used to create a query for targets. Keyword or the name of the protein is given as a string inside the function and results will return all the targets containing the keyword. 
# 
# If you know the exact way your protein is recorded into the ChEMBL database you can skip this step.
# 
# In our case we want to search for compounds active against human TP53, also known as cellular tumor antigen p53.
# 
# 

# In[ ]:


#We'll also import the search results into a dataframe 


compounds = pd.DataFrame(new_client.target.search("p53"))

compounds.head()


# ## Searching for compounds active against protein of interest
# 
# new_client.activity() function is used for compound search.  
# 
# .filter(target_chembl_id = ...) will be added to filter for the protein of interest. We'll use the ChEMBL ID of tp53 from the previous step. 
# 
# 
# For uniformity of the results you'll also want to filter for the type of bioactivity unit defined for the compound.  For our case we want compounds with defined IC50 values. 

# In[ ]:


tp53_chembl_id = compounds.target_chembl_id[0] 

res1 = new_client.activity.filter(target_chembl_id = tp53_chembl_id).filter(standard_type = "IC50")

df1 = pd.DataFrame(res1)

#Let's get rid of compounds with missing IC50 data 

df2 = df1[df1.standard_value.notna()]

df2.head()


# Now we have our table with compounds showing bioactivity properties against our target of interest.  
# 
# From this point on one can perform different analysis on this dataset. 
# 
# Lastly, let's save our data to csv file

# In[ ]:


df2.columns


# In[ ]:


df2.to_csv("p53_active_compounds.csv",index=False)


# In[ ]:




