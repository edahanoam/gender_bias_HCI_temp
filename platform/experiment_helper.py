

import streamlit as st
from instructions_and_examples import INSTRUCTIONS


def display_single_example(current_sample, submit_button_callback):
    with st.popover("Instructions"):
        st.write(INSTRUCTIONS)
    st.markdown('Fix the suggested translation for the following sentence, if necessary:')
    st.write('Original sentence:')
    st.markdown(f'<p style="background-color:#F0FFFF;border-radius:2%;">{current_sample["input"]}</p>',
                unsafe_allow_html=True)
    st.text_input('Suggested translation (edit here)', key='training_translation', value=current_sample['output'])
    st.button('Submit', key='submit_training', on_click=submit_button_callback)
    with st.popover("Display original suggested translation"):
        st.write(f"Model's original suggested translation:\n{current_sample['output']}")


def save_annotation():
    pass
