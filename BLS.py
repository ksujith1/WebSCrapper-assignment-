#!/usr/bin/env python
# coding: utf-8

# ## Pick a website and describe objective

# ## Project Outline : 
# 
# -we're going to scrape : https://www.bls.gov/
# -we'll get a titel of each content. For each content, we'll get content title,content page URL
# -for each repository, we'll grab the content_name as title and the corresponding url
# -for each topic we'll create a csv file in the following format:
# ```
# title,url
# Skip to Content,https://www.bls.gov#startcontent
#   United States Department of Labor,https://www.bls.govhttps://www.dol.gov/
# U.S. Bureau of Labor Statistics,https://www.bls.govhttps://www.bls.gov/
# Follow Us,https://www.bls.govhttp://twitter.com/BLS_gov
# ,https://www.bls.govhttp://twitter.com/BLS_gov
# Release Calendar,https://www.bls.gov/schedule/news_release/
# Blog,https://www.bls.govhttps://blogs.bls.gov/blog/
# ```

# In[ ]:





# ## Use the Requests library to download webpages

# In[2]:


get_ipython().system('pip3 install requests --upgrade --quiet')


# In[3]:


import requests


# In[4]:


bls_url = 'https://www.bls.gov/'


# In[5]:


res = requests.get(bls_url)


# In[6]:


res.status_code


# In[7]:


len(res.text)


# In[10]:


page_contents = (res.text)


# In[11]:


page_contents[:1000]


# In[12]:


with open('webpage.html','w') as f:
    f.write(page_contents)


# In[ ]:





# ## Use Beautiful Soup to parse and extract information

# In[13]:


get_ipython().system('pip3 install beautifulsoup4 --upgrade --quiet')


# In[14]:


from bs4 import BeautifulSoup


# In[15]:


doc = BeautifulSoup(page_contents, 'html.parser')


# In[16]:


type(doc)


# In[18]:


a_tags = doc.find_all('a')


# In[19]:


len(a_tags)


# In[20]:


a_tags[:5]


# In[45]:


a_tag_40 = a_tags[40]['href']
a_tag_40


# In[46]:


ppi_url = "https://www.bls.gov"+ a_tag_40
print(ppi_url)


# In[47]:


a_tags[0].text


# In[49]:


topic_titles= []
for tag in a_tags:
    topic_titles.append(tag.text)
print(topic_titles[:10])


# In[54]:


topic_urls = []
base_url = "https://www.bls.gov"

for tag in a_tags:
    topic_urls.append(base_url + tag['href'])
print(topic_urls[35:45])


# In[ ]:





# ## Create CSV file with the extracted information 

# In[55]:


get_ipython().system('pip3 install pandas --quiet')


# In[ ]:





# In[57]:


topics_dict = {
    'title':topic_titles,
    'url':topic_urls
}


# In[59]:


topic_df = pd.DataFrame(topics_dict)


# In[60]:


topic_df


# In[63]:


topic_df.to_csv('bls.csv',index = None)


# In[ ]:





# ## Getting Information out of a topic page

# In[74]:


topic_page_url = topic_urls[39]
print(topic_page_url)


# In[75]:


res = requests.get(topic_page_url)


# In[76]:


res.status_code


# In[77]:


len(res.text)


# In[78]:


topic_doc = BeautifulSoup(res.text,'html.parser')


# In[83]:


div_selection_id = 'program-title'
headings = topic_doc.find_all('div',{'id':div_selection_id})


# In[84]:


print(headings)


# In[ ]:




