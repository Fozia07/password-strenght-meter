import streamlit as st
import re

def check_password_strength(password: str) -> str:
    length_score = min(len(password) / 12, 1)  # Max 1 point for length
    uppercase_score = bool(re.search(r"[A-Z]", password))
    lowercase_score = bool(re.search(r"[a-z]", password))
    number_score = bool(re.search(r"\d", password))
    special_score = bool(re.search(r"[@$!%*?&]", password))
    
    total_score = sum([length_score, uppercase_score, lowercase_score, number_score, special_score])
    
    if total_score < 2:
        return "Weak"
    elif total_score < 4:
         return "Moderate"
    else:
        return "strong password"
    
st.set_page_config(page_title="Password Strength Meter", page_icon="🔐", layout="centered")

st.markdown(
    """
    <style>
        .stApp {
            background-color: #E2EAF4;
        }
        .stTextInput {
            border-radius: 10px;
            padding: 10px;
            background-color:#807DDF ;
            color:white
        }
        .stbutton{
            background-color:#0F0D4D ;
            color:white;
            border-radius:10px;
            padding:10px;
            font-size:16px;
            font-weight:bold;
            cursor:pointer;
            transition:background-color 0.3s ease;
        }
        .stbutton:hover{
            background-color:#605CDD;
        }
        .sttittle{
            font-size:24px;
            font-weight:bold;
            color:#0F0D4D;
        }
        .stSubheader {
            font-size: 20px;
            font-weight: bold;
        }
        .stError, .stWarning, .stSuccess {
            font-weight: bold;
            padding: 10px;
            border-radius: 10px;
        }
        .stwrite{
            font-size:20px;
            color:white;
            font-style:italic;

        }
    </style>
    """,
    unsafe_allow_html=True
)  

st.title("🔐 Password Strength Meter")
st.write("Check the strenght of your password")
password = st.text_input("Enter your password", type="password")
st.button("check password")

st.markdown("""
✅ **Feature 1:** Use the password strenght meter to check the strenght of your password 
🚀 **Feature 2:** use uppercase, Lowercase, number and special charchters to make your password strong 
📊 **Feature 3:** get a good password and use it to secure your account
""")


if password:
     strength = check_password_strength(password)
    
     st.subheader(f"Password Strength: {strength}")
    
     if strength == "Weak":
        st.error("Your password is too weak. Consider adding uppercase letters, numbers, and special characters.")
     elif strength == "Moderate":
        st.warning("Your password is okay but could be stronger. Try adding more special characters and numbers.")
     else:
        st.success("Your password is strong!")

