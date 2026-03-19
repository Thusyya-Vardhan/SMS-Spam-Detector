import streamlit as st
import pickle

# Load model
model = pickle.load(open('model.pkl', 'rb'))

# App config
st.set_page_config(page_title="SMS Spam Detector", page_icon="📩")

# Header
st.title("📩 SMS Spam Detector")
st.write("Enter a message below to check if it is spam or not.")
st.divider()

# Input
user_input = st.text_area("Your Message", height=150, placeholder="Type your message here...")

# Predict button
col1, col2, col3 = st.columns([1,1,1])
with col2:
    predict_btn = st.button("Check Message", use_container_width=True)

# Result
if predict_btn:
    if user_input.strip() == "":
        st.warning("Please enter a message!")
    else:
        result = model.predict([user_input])[0]
        prob = model.predict_proba([user_input])[0]
        
        st.divider()
        if result == 1:
            st.error(f"SPAM! Confidence: {prob[1]*100:.1f}%")
            st.progress(prob[1])
        else:
            st.success(f"Not Spam! Confidence: {prob[0]*100:.1f}%")
            st.progress(prob[0])