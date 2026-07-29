import streamlit as st


def initialize_memory():
    """Initialize chat history if it doesn't exist."""
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []


def add_message(role, content):
    """Add a message to the chat history."""
    st.session_state.chat_history.append(
        {
            "role": role,
            "content": content
        }
    )


def get_messages():
    """Return the full chat history."""
    return st.session_state.chat_history