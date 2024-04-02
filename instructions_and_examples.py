
import streamlit as st

INSTRUCTIONS = """<Instructions for the task>.\n"""
EXAMPLES = """<Examples for the task>.\n"""


def next_page():
    st.session_state.cur_page = 'training'


def instructions_page():
    st.markdown(INSTRUCTIONS)
    st.markdown(EXAMPLES)
    st.button('Start training', key='next_button2', on_click=next_page)

