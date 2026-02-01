import pandas as pd
from textblob import TextBlob

df = pd.read_csv("Dataset.csv")
df["sentiment_score"] = df["Feedback"].apply(
    lambda x: TextBlob(str(x)).sentiment.polarity
)
def label(score):
    if score > 0.1:
        return "Positive"
    elif score < -0.1:
        return "Negative"
    else:
        return "Neutral"

df["sentiment_label"] = df["sentiment_score"].apply(label)

def theme(text):
    text = str(text).lower()
    if "communication" in text:
        return "Communication"
    elif "delay" in text or "slow" in text:
        return "Support Delay"
    elif "price" in text or "cost" in text:
        return "Pricing"
    elif "quality" in text:
        return "Quality"
    else:
        return "Other"

df["theme"] = df["Feedback"].apply(theme)
df.to_csv("st.csv", index=False)
