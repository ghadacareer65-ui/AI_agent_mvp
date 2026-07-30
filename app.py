import streamlit as st

from agent import generate_draft

<<<<<<< HEAD
from database import (
    create_conversation,
    save_message,
    get_conversations,
    get_messages,
)
# Session State
if "conversation_id" not in st.session_state:
    st.session_state.conversation_id = None
=======
# Session State 
>>>>>>> dd4ee81b650b252cc12fc84b17ee2f9c8de841dc

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
# Sidebar
with st.sidebar:

    st.title("المحادثات")

    if st.button("محادثة جديدة"):

        st.session_state.conversation_id = None
        st.session_state.user_problem = ""
        st.session_state.draft_response = ""
        st.session_state.final_response = ""

        st.rerun()

    st.divider()

    st.subheader("المحادثات السابقة")

    conversations = get_conversations()

    for conversation in conversations:

        title = conversation["title"]

        if st.button(
            title,
            key=f"chat_{conversation['id']}"
        ):

            st.session_state.conversation_id = conversation["id"]

            messages = get_messages(
                conversation["id"]
            )

            st.session_state.user_problem = ""
            st.session_state.draft_response = ""
            st.session_state.final_response = ""

            for message in messages:

                if message["role"] == "user":
                    st.session_state.user_problem = message["message"]

                elif message["role"] == "assistant":
                    st.session_state.draft_response = message["message"]

                elif message["role"] == "final":
                    st.session_state.final_response = message["message"]

            st.rerun()
# الصفحة الرئيسية
st.title("مساعد الدعم الذكي")

st.divider()
# المستخدم
st.header("المستخدم")

user_problem = st.text_area(
    "اكتب مشكلتك:",
    value=st.session_state.user_problem,
    height=150
)

submit_button = st.button("إرسال المشكلة")

if submit_button:

    if user_problem.strip():

        st.session_state.user_problem = user_problem

        conversation_id = create_conversation(
            user_problem[:40]
        )

        st.session_state.conversation_id = conversation_id

        save_message(
            conversation_id,
            "user",
            user_problem
        )

        with st.spinner("جارٍ إنشاء المسودة..."):

            draft = generate_draft(
                user_input=user_problem,
                previous_draft="",
                admin_feedback=""
            )

        st.session_state.draft_response = draft
        st.session_state.final_response = ""

        save_message(
            conversation_id,
            "assistant",
            draft
        )

        st.success("تم إنشاء المسودة بنجاح.")

    else:

        st.warning("يرجى كتابة المشكلة أولًا.")

st.divider()
# المشرف
st.header("المشرف")

st.text_area(
    "مسودة الرد",
    value=st.session_state.draft_response,
    height=220,
    disabled=True
)

admin_feedback = st.text_area(
    "ملاحظات المشرف",
    height=120
)

col1, col2 = st.columns(2)

with col1:
    approve_button = st.button("موافقة")

with col2:
    reject_button = st.button("رفض وإعادة التوليد")
# رفض وإعادة التوليد
if reject_button:

    if st.session_state.draft_response == "":

        st.warning("لا توجد مسودة لإعادة توليدها.")

    elif admin_feedback.strip() == "":

        st.warning("يرجى كتابة ملاحظات المشرف.")

    else:
        # حفظ ملاحظات المشرف
        save_message(
            st.session_state.conversation_id,
            "admin",
            admin_feedback
        )

        with st.spinner("جارٍ إعادة توليد الرد..."):

            new_response = generate_draft(
                user_input=st.session_state.user_problem,
                previous_draft=st.session_state.draft_response,
                admin_feedback=admin_feedback
            )
        # تحديث المسودة
        st.session_state.draft_response = new_response
        # إرسالها مباشرة للمستخدم
        st.session_state.final_response = new_response
        # حفظ المسودة الجديدة
        save_message(
            st.session_state.conversation_id,
            "assistant",
            new_response
        )
        # حفظ الرد النهائي
        save_message(
            st.session_state.conversation_id,
            "final",
            new_response
        )
        st.success("تم إعادة توليد الرد وإرساله للمستخدم.")
# الموافقة
if approve_button:

    if st.session_state.draft_response == "":
        st.warning("لا توجد مسودة للموافقة عليها.")
    else:
        st.session_state.final_response = (
            st.session_state.draft_response
        )

        save_message(
            st.session_state.conversation_id,
            "final",
            st.session_state.final_response
        )

        st.success("تم إرسال الرد للمستخدم.")
# الرد النهائي
st.divider()
st.header("الرد النهائي للمستخدم")
st.text_area(
    "الرد النهائي",
    value=st.session_state.final_response,
    height=220,
    disabled=True
)
<<<<<<< HEAD
# عرض المحادثة الحالية
if st.session_state.conversation_id is not None:

    st.divider()

    st.header("سجل المحادثة")

    messages = get_messages(
        st.session_state.conversation_id
    )

    for message in messages:

        role = message["role"]

        if role == "user":

            with st.chat_message("user"):

                st.write(message["message"])

        elif role == "assistant":

            with st.chat_message("assistant"):

                st.write(message["message"])

        elif role == "admin":

            with st.chat_message("assistant"):

                st.info(" ملاحظات المشرف")

                st.write(message["message"])

        elif role == "final":

            with st.chat_message("assistant"):

                st.success(" الرد النهائي")

                st.write(message["message"])
=======
>>>>>>> dd4ee81b650b252cc12fc84b17ee2f9c8de841dc
