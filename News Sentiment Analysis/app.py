from flask import Flask, render_template, request, url_for, redirect, flash
from models.load_model import predict_sentiment 
from utils.scraper import scrape_latest_news
from charts.visualizer import create_sentiment_chart
from voice.speak import speak_text
from utils.explain_tone import explain_sentiment_choice

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a secure random secret key

@app.route('/')
def index():
    news = scrape_latest_news().get("news", [])
    return render_template('index.html', news=news)

@app.route('/result', methods=['POST'])
def result():
    headline = request.form.get('headline', '').strip()
    description = request.form.get('description', '').strip()

    if not headline or not description:
        flash("Both headline and description are required.", "danger")
        return redirect(url_for('index'))

    try:
        sentiment = predict_sentiment(headline, description)
        explanation = explain_sentiment_choice(headline, description, sentiment)
        chart_path = create_sentiment_chart(sentiment)
        audio_path = speak_text(f"The sentiment is {sentiment}")

        return render_template(
            'result.html',
            headline=headline,
            description=description,
            sentiment=sentiment,
            explanation=explanation,
            chart_path=chart_path,
            audio_path=audio_path
        )
    except Exception as e:
        flash(f"An error occurred: {str(e)}", "danger")
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
