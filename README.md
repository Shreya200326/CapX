# CapX
Analyzed and predict stock movements by extracting and analyzing social media data e.g., from  Reddit
**Overview
This project performs sentiment analysis on posts from the subreddit r/stockstobuytoday. It utilizes the Reddit API to fetch the top posts, analyze their sentiment, and visualize the results.

**Dependencies
To run this project, you need the following Python packages:
asyncpraw : Asynchronous PRAW for accessing the Reddit API.
pandas: Data manipulation and analysis.
textblob: Natural language processing for sentiment analysis.
matplotlib: Plotting library for data visualization.
seaborn: Statistical data visualization based on matplotlib.
nest_asyncio: A workaround for using asyncio in Jupyter Notebooks.
You can install the required packages using pip:
#pip install asyncpraw pandas textblob matplotlib seaborn nest_asyncio

**Setup
Create a Reddit App:

1.Go to Reddit's App Preferences.
2.Create a new application.
3.Note down your client_id, client_secret, and user_agent.
4.Replace Credentials:

Open the script and replace the placeholders with your Reddit app credentials in the asyncpraw.Reddit initialization section:
##
reddit = asyncpraw.Reddit(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    user_agent='YOUR_USER_AGENT'
)##
**Running the Code:
Ensure you have Python installed (preferably Python 3.7 or higher).
Run the script in an environment that supports asynchronous code (like Jupyter Notebook or an appropriate IDE).
Call the asyncio.run(main()) function to execute the data fetching and analysis.

**Output
The script fetches the top 100 posts from r/stockstobuytoday and performs the following:

1.Sentiment Analysis: Analyzes both the titles and bodies of the posts to categorize them as positive, negative, or neutral.
2.Frequency Analysis: Counts the frequency of stock mentions in the titles.
3.Visualizations: Plots sentiment distribution and stock mention frequencies.
4.Buy/Sell Recommendations: Generates possible buy and sell signals based on sentiment analysis.
**Troubleshooting
Ensure that you have an active internet connection.
Check your Reddit app credentials if you encounter authentication errors.
Make sure the necessary packages are installed.
