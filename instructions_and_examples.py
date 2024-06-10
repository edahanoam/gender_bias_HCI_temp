
import streamlit as st

INSTRUCTIONS = """For each sentence in English, you will be presented with a Hebrew translation that is the output of a machine translation model.

Unfortunately, some of the translations might include errors that need corrections.

Please edit the translations if needed so they would be accurate and grammatically correct. 

Thank you so much for participating!

\n"""
EXAMPLES = """<Examples for the task>.\n"""


def next_page():
    st.session_state.cur_page = 'training'
    #st.session_state.cur_page = 'experiment'


def instructions_page():
    st.title('Machine-Translation Evaluation: Instructions')
    st.markdown(INSTRUCTIONS)
    #st.markdown(EXAMPLES)
    st.button('Start training', key='next_button2', on_click=next_page)
    #st.button('Start', key='next_button2', on_click=next_page)

