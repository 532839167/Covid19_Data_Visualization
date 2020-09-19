#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plotly


# In[22]:


dataset_url = 'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
df = pd.read_csv(dataset_url)
df = df.sort_values(['Date', 'Confirmed'], ascending=[True, False])


# In[23]:


df.head()


# In[24]:


df.tail()


# In[25]:


df.shape


# In[26]:


df = df[df['Confirmed'] > 0]


# In[27]:


df.head()


# In[28]:


df[df['Country'] == 'China']


# In[31]:


fig = px.choropleth(df, locations = 'Country', locationmode = 'country names', color = 'Confirmed', animation_frame = 'Date')
fig.update_layout(title_text = "Global Spread of Covid - 19")
fig.show()


# In[34]:


death_fig = px.choropleth(df, locations = 'Country', locationmode = 'country names', color = 'Deaths', animation_frame = 'Date')
death_fig.update_layout(title_text = "Global Death of Covid - 19")
death_fig.show()


# ###    Visualization of how intensive the Covid-19 transmission has been in each of the country ###

# In[36]:


df_china = df[df['Country'] == 'China']
df_china.head()


# In[37]:


df_china = df_china[['Date', 'Confirmed']]


# In[38]:


df_china.head()


# In[39]:


df_china['Infection Rate'] = df_china['Confirmed'].diff()
df_china.head()


# In[40]:


px.line(df_china, x = 'Date', y = ['Confirmed', 'Infection Rate'])


# In[41]:


df_china['Infection Rate'].max()


# **Calculate maximum infection rate for all countries**

# In[44]:


countries = list(df['Country'].unique())


# In[47]:


max_infection_rates = []
for c in countries:
    mir = df[df['Country'] == c]['Confirmed'].diff().max()
    max_infection_rates.append(mir)


# In[48]:


df_mir = pd.DataFrame()
df_mir['Country'] = countries
df_mir['Max Infection Rate'] = max_infection_rates
df_mir.head()


# In[50]:


px.bar(df_mir, x = 'Country',  y = 'Max Infection Rate', color = 'Country', title = 'Global Maximum Infection Rate', log_y = True)


# ## How National Lockdowns Impacts Covid Transmission in Italy ##

# In[82]:


italy_lockdown_start_date = '2020-03-09'
italy_lockdown_a_month_later = '2020-04-09'

df_italy = df[df['Country'] == 'Italy']
df_italy.head()


# Calculate the infection rate in Italy

# In[83]:


df_italy['Infection Rate'] = df_italy['Confirmed'].diff()
df_italy.head()


# In[84]:


fig = px.line(df_italy, x = 'Date', y = 'Infection Rate', title = 'Infection Rate Before and After Lockdown')

fig.add_shape(
    dict(
    type = 'line',
    x0 = italy_lockdown_start_date,
    y0 = 0,
    x1 = italy_lockdown_start_date,
    y1 = df_italy['Infection Rate'].max(),
    line = dict(
            color = 'red', 
            width = 2
        )
    )
)

fig.add_annotation(
    dict(
        x = italy_lockdown_start_date,
        y = df_italy['Infection Rate'].max(),
        text = 'Lockdown started'
    )
)

fig.add_shape(
    dict(
    type = 'line',
    x0 = italy_lockdown_a_month_later,
    y0 = 0,
    x1 = italy_lockdown_a_month_later,
    y1 = df_italy['Infection Rate'].max(),
    line = dict(
            color = 'orange', 
            width = 2
        )
    )
)

fig.add_annotation(
    dict(
        x = italy_lockdown_a_month_later,
        y = df_italy['Infection Rate'].max(),
        text = 'A month later'
    )
)

fig.show()


# ### How National Lockdowns Impacts Covid Deaths in Italy ###

# Calculate death rate

# In[85]:


df_italy['Death Rate'] = df_italy['Deaths'].diff()
df_italy.head()


# In[87]:


fig = px.line(df_italy, x = 'Date', y = ['Infection Rate', 'Death Rate'], title = 'Infection Rate and Death Rate Before and After Lockdown')

fig.add_shape(
    dict(
    type = 'line',
    x0 = italy_lockdown_start_date,
    y0 = 0,
    x1 = italy_lockdown_start_date,
    y1 = df_italy['Infection Rate'].max(),
    line = dict(
            color = 'red', 
            width = 2
        )
    )
)

fig.add_annotation(
    dict(
        x = italy_lockdown_start_date,
        y = df_italy['Infection Rate'].max(),
        text = 'Lockdown started'
    )
)

fig.add_shape(
    dict(
    type = 'line',
    x0 = italy_lockdown_a_month_later,
    y0 = 0,
    x1 = italy_lockdown_a_month_later,
    y1 = df_italy['Infection Rate'].max(),
    line = dict(
            color = 'orange', 
            width = 2
        )
    )
)

fig.add_annotation(
    dict(
        x = italy_lockdown_a_month_later,
        y = df_italy['Infection Rate'].max(),
        text = 'A month later'
    )
)

fig.show()


# Normalize the columns

# In[89]:


df_italy['Infection Rate'] = df_italy['Infection Rate'] / df_italy['Infection Rate'].max()
df_italy['Death Rate'] = df_italy['Death Rate'] / df_italy['Death Rate'].max()


# In[90]:


fig = px.line(df_italy, x = 'Date', y = ['Infection Rate', 'Death Rate'], title = 'Normalized Infection Rate and Death Rate Before and After Lockdown')

fig.add_shape(
    dict(
    type = 'line',
    x0 = italy_lockdown_start_date,
    y0 = 0,
    x1 = italy_lockdown_start_date,
    y1 = df_italy['Infection Rate'].max(),
    line = dict(
            color = 'red', 
            width = 2
        )
    )
)

fig.add_annotation(
    dict(
        x = italy_lockdown_start_date,
        y = df_italy['Infection Rate'].max(),
        text = 'Lockdown started'
    )
)

fig.add_shape(
    dict(
    type = 'line',
    x0 = italy_lockdown_a_month_later,
    y0 = 0,
    x1 = italy_lockdown_a_month_later,
    y1 = df_italy['Infection Rate'].max(),
    line = dict(
            color = 'orange', 
            width = 2
        )
    )
)

fig.add_annotation(
    dict(
        x = italy_lockdown_a_month_later,
        y = df_italy['Infection Rate'].max(),
        text = 'A month later'
    )
)

fig.show()


# In[ ]:




