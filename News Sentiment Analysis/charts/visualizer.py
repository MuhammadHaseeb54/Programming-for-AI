import matplotlib.pyplot as plt
import os
import uuid

def create_sentiment_chart(sentiment):
    # Dummy confidence values for now
    data = {
        'positive': 0.7 if sentiment.lower() == 'positive' else 0.1,
        'negative': 0.7 if sentiment.lower() == 'negative' else 0.1,
        'neutral': 0.7 if sentiment.lower() == 'neutral' else 0.1
    }

    labels = list(data.keys())
    values = list(data.values())

    plt.figure(figsize=(6, 4))
    bars = plt.bar(labels, values, color=['#28a745', '#dc3545', '#ffc107'])
    plt.ylim(0, 1)
    plt.title("Sentiment Confidence")
    plt.xlabel("Sentiment")
    plt.ylabel("Confidence Score")

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + 0.25, yval + 0.02, f"{yval:.2f}")

    # Save chart
    filename = f"{uuid.uuid4().hex}.png"
    charts_dir = os.path.join("static", "charts")
    os.makedirs(charts_dir, exist_ok=True)
    chart_path = os.path.join(charts_dir, filename)
    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()

    return f"charts/{filename}"  # Return relative path for HTML
