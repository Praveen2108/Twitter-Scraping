import snscrape.modules.twitter as snt
import pandas as pd
import streamlit as st
import datetime

def get_tweets(search_text,date_start,date_end,limit):

    tweet_list = []

    for i,tweet in enumerate(snt.TwitterSearchScraper(search_text+' since:'+str(date_start)+' until:'+str(date_end)).get_items()):
        if i>limit:
            break
        tweet_list.append([tweet.id,tweet.date, tweet.username,tweet.url,tweet.content,tweet.replyCount,tweet.retweetCount,tweet.source])
    df = pd.DataFrame(tweet_list,
                    columns=[tweet.id,tweet.date, tweet.username, tweet.url,tweet.content,tweet.replyCount, tweet.retweetCount,tweet.source])
    file_csv = df.to_csv().encode('utf-8')
    st.download_button(
        label="Download data as CSV",
        data=file_csv,
        file_name= file_name+'.csv',
        mime='text/csv',
    )
    file_json = df.to_json().encode('utf-8')
    st.download_button(
        label="Download data as JSON",
        data=file_json,
        file_name= file_name+'.json',
        mime='text/json',
    )


st.header("Twitter Data Scrapper")
search_text = st.text_input('Search Text','Elon musk')
date_start = st.date_input("Starting date",datetime.date(2021, 11, 21))
date_end = st.date_input("Ending date",datetime.date(2022, 2, 15))
tweet_amount = st.slider('Enter the number of tweets', 0, 1000, 100)
file_name = st.text_input('Name of the file to create','tweet_data')

if st.button('Load Data'):

    get_tweets(search_text, date_start, date_end, tweet_amount)