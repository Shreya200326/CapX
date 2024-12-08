import re
from collections import Counter
from textblob import TextBlob
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import nest_asyncio
import asyncio
import asyncpraw
import streamlit as st
nest_asyncio.apply()

# Asynchronous function to fetch Reddit data
async def fetch_reddit_data(subreddit_name, post_limit=100):
    reddit = asyncpraw.Reddit(
        client_id="Cj1v99waA7sQLep9PH6yZA",
        client_secret="D7XwLuoMbm7xusItSJuzQQiWQiV8DA",
        user_agent="Capx1 Sentiment Analysis v1.0 (by /u/yourusername)"
    )
    subreddit = await reddit.subreddit(subreddit_name)
    posts = []

    try:
        async for post in subreddit.top(limit=post_limit):
            posts.append([post.title, post.selftext, post.created_utc])
    except Exception as e:
        st.error(f"Error fetching posts: {e}")
        return pd.DataFrame()

    return pd.DataFrame(posts, columns=["Title", "Body", "Created"])

# Sentiment analysis function
def get_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "positive"
    elif analysis.sentiment.polarity < 0:
        return "negative"
    else:
        return "neutral"

# Extract stock symbols
def extract_symbols(text):
    return re.findall(r"\b[A-Z]{1,5}\b", text)

# Streamlit App
st.title("Reddit Sentiment Analysis for Stocks")
st.sidebar.header("Configuration")

# Sidebar options
subreddit_name = st.sidebar.text_input("Enter Subreddit Name", "stockstobuytoday")
post_limit = st.sidebar.slider("Number of Posts to Analyze", 10, 500, 100)

# Fetch data button
if st.sidebar.button("Fetch Data"):
    with st.spinner("Fetching Reddit data..."):
        data = asyncio.run(fetch_reddit_data(subreddit_name, post_limit))
    
    if not data.empty:
        data["Created"] = pd.to_datetime(data["Created"], unit="s")
        data["Title Sentiment"] = data["Title"].apply(get_sentiment)
        data["Body Sentiment"] = data["Body"].apply(get_sentiment)

        # Display data
        st.subheader("Fetched Data")
        st.write(data)

        # Sentiment distribution
        sentiment_counts = data["Title Sentiment"].value_counts()
        st.subheader("Sentiment Distribution")
        st.bar_chart(sentiment_counts)

        # Stock mentions
        all_symbols = []
        for title in data["Title"]:
            all_symbols.extend(extract_symbols(title))
        symbol_counts = Counter(all_symbols)
        symbol_df = pd.DataFrame(symbol_counts.items(), columns=["Symbol", "Frequency"]).sort_values(by="Frequency", ascending=False)
        
        st.subheader("Top Stock Mentions")
        st.write(symbol_df.head(10))

        # Visualization
        st.subheader("Sentiment Trends Over Time")
        daily_sentiment = data.groupby(data["Created"].dt.date).agg({
            "Title Sentiment": lambda x: x.value_counts().get("positive", 0),
            "Body Sentiment": lambda x: x.value_counts().get("positive", 0)
        }).reset_index()
        daily_sentiment.columns = ["Date", "Positive Title Sentiment", "Positive Body Sentiment"]
        
        st.line_chart(daily_sentiment.set_index("Date"))
        
        # Buy/Sell signals
        st.subheader("Buy/Sell Signals")
        buy_signals = data[(data["Title Sentiment"] == "positive") | (data["Body Sentiment"] == "positive")]
        sell_signals = data[(data["Title Sentiment"] == "negative") | (data["Body Sentiment"] == "negative")]

        st.write("**Buy Signals**")
        st.write(buy_signals[["Title", "Body"]])

        st.write("**Sell Signals**")
        st.write(sell_signals[["Title", "Body"]])
    else:
        st.warning("No data available to analyze.")

