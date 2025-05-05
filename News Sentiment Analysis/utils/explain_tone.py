def explain_sentiment_choice(headline, description, sentiment):
    explanation = {
        "positive": "The headline conveys optimism, approval, or a favorable tone.",
        "negative": "The headline suggests criticism, fear, or disapproval.",
        "neutral": "The headline presents information without strong emotional bias."
    }

    # Normalize sentiment to lowercase
    sentiment = sentiment.lower()

    # Fallback if sentiment key not found
    sentiment_reason = explanation.get(
        sentiment,
        "The model prediction could not be confidently explained with predefined logic."
    )

    text_sample = (
        f"Headline: {headline}\n"
        f"Description: {description}\n\n"
        f"Prediction: {sentiment}\n\n"
        f"Explanation: {sentiment_reason}"
    )

    return text_sample
