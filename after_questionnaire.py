
import streamlit as st

AFTER_TEXT = """<After questionnaire text>.\n"""


def next_page():
    st.session_state.cur_page = 'finish'


def after():
    st.markdown(AFTER_TEXT)
    st.radio('How much did you trust the LLM that generated the translations?',
             options=['1 - poorly, I always edited what the model generates', '2', '3', '4',
                      '5 - greatly, I use its output as is'],
             key='llm_trust_after', index=None)
    st.radio('How satisfied are you with the LLM that generated the translations?',
             options=['1 - not at all', '2', '3', '4', '5 - completely satisfied'],
             key='llm_satisfy_after', index=None)
    st.radio('How gender biased do you think that this LLM is?',
             options=['1 - not biased at all', '2', '3', '4', '5 - 100% biased'],
             key='llm_bias', index=None)
    st.button('Finish', key='next_button1', on_click=next_page)

