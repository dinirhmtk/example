#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import numpy as np
import pandas as pd
import altair as alt


# In[ ]:


# Page title
st.set_page_config(page_title='Exploratory Investment Viewer', page_icon='📊')
st.title('📊 Exploratory Investment Viewewr')

with st.expander('About this app'):
    st.markdown('**What can this app do?**')
    st.info('This app shows the use of Pandas for data wrangling, Altair for chart creation and editable dataframe for data interaction.')


# In[ ]:


st.header("Investment Sum Asuransi Jiwa")
file_path_1 = st.file_uploader("Upload the first Excel file", type=["xlsx"])
if file_path_1 is not None:
    data1 = load_data(file_path_1)
    st.write(data1)


# In[ ]:


st.header("Investment Sum Asuransi Umum")
file_path_2 = st.file_uploader("Upload the second Excel file", type=["xlsx"], key="second_file")
if file_path_2 is not None:
    data2 = load_data(file_path_2)
    st.write(data2)


# In[ ]:


if file_path_1 is not None and file_path_2 is not None:
    st.header("Descriptive Statistics for Both Datasets")
    st.subheader("Descriptive Statistics for Asuransi Jiwa")
    st.write(data1.describe())
    st.subheader("Descriptive Statistics for Asuransi Umum")
    st.write(data2.describe())


# In[ ]:


# Visualisasi Time Series
if file_path_1 is not None:
    st.header("Time Series Analysis for First Dataset")
    data1['REPORT_DATE'] = pd.to_datetime(data1['REPORT_DATE'])
    grouped_data1 = data1.groupby('NAMA_PERUSAHAAN')
    
    st.subheader("Total Investment Over Time for Each Company (First Dataset)")
    for name, group in grouped_data1:
        st.line_chart(group.set_index('REPORT_DATE')['TOTAL KESELURUHAN INVESTASI'], width=0, height=0, use_container_width=True)

if file_path_2 is not None:
    st.header("Time Series Analysis for Second Dataset")
    data2['REPORT_DATE'] = pd.to_datetime(data2['REPORT_DATE'])
    grouped_data2 = data2.groupby('NAMA_PERUSAHAAN')
    
    st.subheader("Total Investment Over Time for Each Company (Second Dataset)")
    for name, group in grouped_data2:
        st.line_chart(group.set_index('REPORT_DATE')['TOTAL KESELURUHAN INVESTASI'], width=0, height=0, use_container_width=True)

