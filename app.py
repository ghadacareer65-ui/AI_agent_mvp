import streamlit as st
from agent import generate_draft

# Session State 

if "draft_response" not in st.session_state:
    st.session_state.draft_response = ""

if "final_response" not in st.session_state:
    st.session_state.final_response = ""

if "user_problem" not in st.session_state:
    st.session_state.user_problem = ""

# إعداد الصفحة

st.set_page_config(
    page_title="مساعد الدعم الذكي",
    layout="wide"
)
# عنوان التطبيق

st.title("مساعد الدعم الذكي")

st.divider()

# قسم المستخدم

st.header("المستخدم")

user_problem = st.text_area(
    "اكتب مشكلتك:",
    height=150
)
submit_button = st.button("إرسال المشكلة")

st.divider()

# قسم المشرف

st.header("المشرف")

if submit_button:

    if user_problem.strip():

        with st.spinner("جارٍ معالجة طلبك..."):

            st.session_state.user_problem = user_problem

            st.session_state.draft_response = generate_draft(
                user_problem
            )

        st.success("تم استلام طلبك بنجاح ")

    else:

        st.warning("يرجى كتابة المشكلة أولًا !")

st.text_area(
    "مسودة الرد",
    value=st.session_state.draft_response,
    height=180,
    disabled=True
)

admin_feedback = st.text_area(
    "ملاحظات المشرف",
    height=120
)

col1, col2, col3 = st.columns([1, 1, 6])

with col1:
    approve_button = st.button("موافقة")

    if approve_button:st.session_state.final_response = st.session_state.draft_response

with col2:
    reject_button = st.button("رفض وإعادة التوليد")

if reject_button:

    if admin_feedback.strip():

        with st.spinner("جارٍ إعادة توليد المسودة..."):

            st.session_state.draft_response = generate_draft(
                st.session_state.user_problem,
                admin_feedback
            )

    else:

        st.warning("!يرجى كتابة ملاحظات المشرف أولًا")

st.divider()

# الرد النهائي

st.header("الرد المُرسل للمستخدم")

final_response = st.text_area(
    "الرد النهائي",
    value=st.session_state.final_response,
    height=180,
    disabled=True
)
