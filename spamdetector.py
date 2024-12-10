import streamlit as st
import pickle


model = pickle.load(open(r'C:\Users\bhoom\OneDrive\Documents\Desktop\AICTE_SPAM_PRO\SafeMailAI-main\spam123.pkl', 'rb'))
cv = pickle.load(open(r'C:\Users\bhoom\OneDrive\Documents\Desktop\AICTE_SPAM_PRO\SafeMailAI-main\vec123.pkl', 'rb'))

def main():
    st.title("SafeMailAI: Email Spam Classification")
    st.markdown("Classify emails as **Spam** or **Not Spam** using Machine Learning.")

  
    user_input = st.text_area("Enter your email for classification", height=150, max_chars=1000)
    
    if st.button("Classify Email"):
        if user_input:
            data = [user_input]
            vect = cv.transform(data).toarray()
            result = model.predict(vect)
            if result[0] == 0:
                st.success("✅ This is NOT a Spam Email")
            else:
                st.error("❌ This is a Spam Email")
        else:
            st.warning("⚠️ Please enter an email to classify.")


main()
