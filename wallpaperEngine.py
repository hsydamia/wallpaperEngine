
# coding: utf-8

# In[127]:
#

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


# In[128]:


myurl = 'https://steamcommunity.com/app/431960/reviews/?browsefilter=toprated&snr=1_5_reviews_&filterLanguage=english'


# In[129]:


uClient = uReq(myurl)
page_html=uClient.read()
uClient.close()


# In[130]:


page_soup = soup(page_html,"html.parser")


# In[131]:


containers = page_soup.findAll("div",{"class":"apphub_UserReviewCardContent"})


# In[132]:


filename="review.csv"
f = open(filename, "w")

headers="Class, Review\n"

f.write(headers)

for container in containers:
    
    unwanted = container.find("div",{"class":"date_posted"})
    unwanted.extract()
    
    unwanted1 = container.find("div",{"class":"early_access_review"})
    unwanted1.extract()
    
    unwanted2 = container.find("div",{"class":"hours"})
    unwanted2.extract()
    
    review_container = container.findAll("div",{"class":"apphub_CardTextContent"}) 
    review = review_container[0].text
    
    class_container = container.findAll("div",{"class":"reviewInfo"})
    classcon = class_container[0].text.strip()
    
    print("review: "+review)
    print("class: "+classcon)
    
    f.write(classcon+","+review.replace(",","")+"\n")
    
f.close()

