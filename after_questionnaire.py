
import streamlit as st

AFTER_TEXT = """Please take a moment to answer the following questionnaire on your experience with our models' translation capabilities.\n"""


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


def after_with_all_survey():
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

    st.radio('How often do you use LLMs in your daily life?',
             options=['1 - never', '2', '3', '4', '5 - all the time'],
             key='llms_usage', index=None)
    st.radio('How much do you trust the output that your favorite LLM generates?',
             options=['1 - poorly, I always edit what the model generates', '2', '3', '4', '5 - greatly, I use its output as is'],
             key='llms_trust_before', index=None)
    st.radio('How satisfied are you with the experiment of using LLMs?',
             options=['1 - not at all', '2', '3', '4', '5 - completely satisfied'],
             key='llms_satisfy_before', index=None)
    st.selectbox('Do you pay subscription to any LLM service?', key='llms_subscription', options=['yes', 'no'], index=None)
    st.text_input('Which tasks do you use LLMs for?')

    st.selectbox('Age', key='age', options=['18-24', '25-34', '35-44', '45-54', '55-64', '65+'], index=None)
    st.radio('Gender', options=['male', 'female', 'other', 'prefer not to say'], key='gender', index=None)

    st.button('Finish', key='next_button1', on_click=next_page)

