import streamlit as st
from send_email import send_message
import re
import pandas
st.header("Contact Us📧")
df = pandas.read_csv("topics.csv")
EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
with st.form(key="email_form"):
    user_email = st.text_input("Your email address",placeholder = "example@domain.com",
                               help="Please enter a valid email address!")

    topics = st.multiselect("What topics do you want to discuss?",df)
    message = st.text_area("Your message",placeholder = "Please enter your message here!")

    button = st.form_submit_button("Submit")

    message = message + "\n" + "Topics:" + " ".join(topics)  + "\n" + user_email
    if button:
        if re.match(EMAIL_REGEX,user_email):
            send_message(message,user_email)
            st.info("Your email has been sent successfully!")
        else:
            st.error("Please enter a valid email address!")
