import streamlit as st
import google.generativeai as genai
from PIL import Image

# إعدادات الواجهة الملكية
st.set_page_config(page_title="JOSEPH FAHMY AI", page_icon="👑")

# تصميم ذهبي وملكي فاخر وسريع جداً
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1 { color: #D4AF37; text-align: center; font-family: 'serif'; font-size: 55px; text-shadow: 2px 2px #222; }
    .stChatInputContainer { border: 2px solid #D4AF37; border-radius: 30px; }
    .stButton>button { background: linear-gradient(45deg, #D4AF37, #BF953F); color: black; font-weight: bold; border-radius: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>🔱 JOSEPH FAHMY AI </h1>", unsafe_allow_html=True)

# تفعيل المحرك الصاروخي Gemini 1.5 Flash
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # واجهة رفع الصور
    uploaded_file = st.file_uploader("📸 ارفع صورة السؤال هنا للحل الفوري", type=["jpg", "png", "jpeg"])
    
    if prompt := st.chat_input("أمرك مطاع يا جوزيف... اكتب سؤالك"):
        with st.chat_message("assistant"):
            with st.spinner("🚀 جاري الحل بسرعة الصاروخ..."):
                try:
                    if uploaded_file:
                        img = Image.open(uploaded_file)
                        response = model.generate_content([prompt, img])
                    else:
                        response = model.generate_content(prompt)
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"خطأ: {e}")
else:
    st.error("⚠️ يا إمبراطور، تأكد من إضافة GOOGLE_API_KEY في الـ Secrets!")
