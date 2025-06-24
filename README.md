# CapX
Here’s a detailed `README.md` file for your Reddit sentiment analysis project:
# 📈 Reddit Stock Sentiment Analyzer
This project is a sentiment analysis tool built using Python to analyze stock-related discussions on Reddit. It pulls top posts from the `r/stockstobuytoday` subreddit and performs sentiment analysis using **TextBlob**, identifies potential **buy/sell signals**, visualizes sentiment trends, and tracks **stock symbol mentions**.
---

## 📌 Features

* 🔍 **Fetches top 100 posts** from `r/stockstobuytoday` asynchronously using `asyncpraw`
* 📊 Performs **sentiment analysis** on both title and body of posts
* 🔁 Tracks **frequency of stock symbols** mentioned (e.g., AAPL, TSLA)
* 🛍️ Identifies **buy/sell signals** based on polarity thresholds
* 📈 Plots:

  * Sentiment distribution
  * Stock mentions frequency
  * Daily sentiment trends
* 💡 Generates **actionable recommendations** based on sentiment scores

---

## 🛠️ Technologies Used

* `asyncpraw` – Asynchronous Reddit API Wrapper
* `TextBlob` – Sentiment Analysis
* `matplotlib` & `seaborn` – Data Visualization
* `pandas` – Data Handling
* `re` & `collections.Counter` – Regex for symbol extraction and frequency count

---

## 📦 Installation

1. Clone the repository or copy the code into your Jupyter Notebook / Google Colab environment.

2. Install the required libraries:

```bash
pip install asyncpraw praw textblob matplotlib pandas seaborn nest_asyncio
```

> ✅ Tip: If using Google Colab, prefix `!` before the commands:

```python
!pip install asyncpraw praw textblob matplotlib pandas seaborn nest_asyncio
```

---

## 🧠 How It Works

1. **Data Collection**:
   Connects to Reddit using `asyncpraw`, retrieves top posts from `r/stockstobuytoday`.

2. **Sentiment Analysis**:
   Uses `TextBlob` to analyze the polarity of titles and bodies of posts.

3. **Stock Mentions**:
   Uses regex to extract stock tickers (capitalized words with 1–5 letters).

4. **Signal Generation**:

   * Posts with polarity > 0.1 → potential **buy** signals
   * Posts with polarity < -0.1 → potential **sell** signals

5. **Visualization**:

   * Bar charts for sentiment distribution and stock mentions
   * Line plots for daily sentiment trends

6. **Recommendations**:
   Summarizes findings in plain English for actionable insights.

---

## 🧪 Example Output

* 📊 **Sentiment Chart**:
  ![Sentiment Chart Example](#)

* 📈 **Daily Trends**:
  ![Trend Plot Example](#)

* 💡 **Buy/Sell Recommendations**:

  ```
  Based on the analysis, the following stocks show potential buy signals:
  - 'Apple will explode after earnings!' with an overall sentiment of 0.45
  ```

---

## 📁 File Structure

```
Capx1.ipynb            # Main Jupyter notebook (or Colab notebook)
README.md              # Documentation
```

---

