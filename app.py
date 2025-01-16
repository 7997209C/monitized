import streamlit as st

# Set page config
st.set_page_config(
    page_title="Support Cato Carling",
    page_icon=":moneybag:",
    layout="centered",
    initial_sidebar_state="expanded",
)

colm = st.columns(2, gap="large")
with colm[0]:
        
    # Main header
    st.title("Support Cato Carling :moneybag:")
    st.markdown("""
    Welcome to this page where you can support **Cato Carling**!
    Cato is an 11-year-old who loves cooking, enjoys golf, and has a deep interest in the Bible and Christianity, use the payment link below. 😊
    """)
    st.divider()
    st.link_button("Pay for your food and drink", "https://donate.stripe.com/dR68wBfcT88Zbm0288",type="primary")

with colm[1]:
    st.image("catopic.jpeg", caption="Cato Carling")
   

# Button to pay
# st.subheader("Click the button below to make a payment:")

# About section
st.header("About Cato")

st.markdown("""
Cato is a bright and active individual who enjoys:
- 🥘 Exploring the art of cooking
- ⛳ Practicing golf skills
- 📖 Studying the Bible and learning about Christianity



Your support helps Cato continue pursuing these passions. Thank you! 🙏
""")

# Footer
st.divider()
st.markdown("**Created** with ❤️ by Cato Carling")


