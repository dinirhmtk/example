#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[10]:


data1 = pd.read_excel('Investment Sum.xlsx', sheet_name='AJ')
data2 = pd.read_excel('Investment Sum.xlsx', sheet_name='AU')


# In[3]:


data1['REPORT_DATE'] = pd.to_datetime(data1['REPORT_DATE'])
nama_perusahaan = data1['NAMA_PERUSAHAAN'].unique()


# In[4]:


num_companies = len(nama_perusahaan)
fig, axs = plt.subplots(num_companies, 1, figsize=(14, 7 * num_companies))

for i, company in enumerate(nama_perusahaan):
    data_perusahaan = data1[data1['NAMA_PERUSAHAAN'] == company]
    data_perusahaan.set_index('REPORT_DATE', inplace=True)

    axs[i].plot(data_perusahaan.index, data_perusahaan['TOTAL OBLIGASI'], label='Total Obligasi')
    axs[i].plot(data_perusahaan.index, data_perusahaan['TOTAL REKSADANA'], label='Total Reksadana')
    axs[i].plot(data_perusahaan.index, data_perusahaan['TOTAL SAHAM'], label='Total Saham')
    axs[i].plot(data_perusahaan.index, data_perusahaan['TOTAL INV LAINNYA'], label='Total Investasi Lainnya')

    axs[i].set_title(f'Analisis Time Series untuk {company}')
    axs[i].set_xlabel('Tahun')
    axs[i].set_ylabel('Total')
    axs[i].legend()
    axs[i].grid(True)

plt.tight_layout()

plt.show()


# In[11]:


data2['REPORT_DATE'] = pd.to_datetime(data2['REPORT_DATE'])
nama_perusahaan = data2['NAMA_PERUSAHAAN'].unique()


# In[13]:


num_companies = len(nama_perusahaan)
subplots_per_figure = 5
num_figures = len(nama_perusahaan) // subplots_per_figure + (1 if len(nama_perusahaan) % subplots_per_figure != 0 else 0)

for start_idx in range(0, num_companies, subplots_per_figure):
    end_idx = min(start_idx + subplots_per_figure, num_companies)
    fig, axs = plt.subplots(end_idx - start_idx, 1, figsize=(14, 7 * (end_idx - start_idx)))

    for i, company in enumerate(nama_perusahaan[start_idx:end_idx]):
        data_perusahaan = data2[data2['NAMA_PERUSAHAAN'] == company]
        data_perusahaan.set_index('REPORT_DATE', inplace=True)

        ax = axs[i] if (end_idx - start_idx) > 1 else axs

        ax.plot(data_perusahaan.index, data_perusahaan['TOTAL OBLIGASI'], label='Total Obligasi')
        ax.plot(data_perusahaan.index, data_perusahaan['TOTAL REKSADANA'], label='Total Reksadana')
        ax.plot(data_perusahaan.index, data_perusahaan['TOTAL SAHAM'], label='Total Saham')
        ax.plot(data_perusahaan.index, data_perusahaan['TOTAL INV LAINNYA'], label='Total Investasi Lainnya')

        ax.set_title(f'Analisis Time Series untuk {company}')
        ax.set_xlabel('Tanggal')
        ax.set_ylabel('Total')
        ax.legend()
        ax.grid(True)

    plt.tight_layout()
    plt.show()


# In[ ]:




