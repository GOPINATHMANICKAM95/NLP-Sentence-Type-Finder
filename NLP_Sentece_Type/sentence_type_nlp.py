import streamlit as st
import joblib

# Load the pre-trained model
model = joblib.load('sentence_type_nlp.joblib')

# Define app title
st.title("Sentence Predictor")

# Input text for prediction
review_text = st.text_area("Enter a sentence:")

# Button to predict sentiment
if st.button("Predict sentence"):
    # Predict the sentiment
    prediction = model.predict([review_text])[0]
    st.write(f"Sentiment: {prediction}")
    
    
