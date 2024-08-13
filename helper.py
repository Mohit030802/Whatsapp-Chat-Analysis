from urlextract import URLExtract
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
def fetch_stats(selected_user,df):
     
    if selected_user!='Overall':
        df=df[df['Sender']==selected_user]
    num_message=df.shape[0]
    words=[]
    for message in df['Message']:
        words.extend(message.split())
    num_media_messages=df[df['Message']=='image omitted'].shape[0]
    links=[]
    extractor=URLExtract()
    for message in df['Message']:
        link=extractor.find_urls(message)
        links.extend(link)

    num_of_links=len(links)
    return num_message,words,num_media_messages,num_of_links

def get_busy_user(df):
    X=df['Sender'].value_counts().head(6)
    df=round((df['Sender'].value_counts()/df.shape[0])*100,2).reset_index().rename({'Sender':'name','count':'percentage'})
    return X,df

def create_word_cloud(selected_user,df):
    if selected_user!='Overall':
        df=df[df['Sender']==selected_user]
    wc=WordCloud(width=500,height=500,min_font_size=10,background_color='white')
    df_sw=wc.generate(df['Message'].str.cat(sep=" "))
    return df_sw

def most_common_words(selected_user,df):
    f=open('stop_hinglish.txt','r')
    stop_words=f.read()
    if selected_user!='Overall':
        df=df[df['Sender']==selected_user]
    words=[]
    for message in df['Message']:
        for word in message.lower():
            if word not in stop_words:
                words.extend(word)
    return_df=pd.DataFrame(Counter(words).most_common(20))
    return return_df
    
     