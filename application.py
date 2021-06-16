#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import numpy as np

st.title('ABS INDEX')


h = pd.read_csv("C:\\Users\\Mohamed.Bounouar\\Downloads\\Angola.csv", dtype = {'k':str}).drop(['Unnamed: 0'], axis = 1)

st.table(h)
