import streamlit as st
from platform.after_questionnaire import after_with_all_survey, demographics
from platform.before_questionnaire import before
from platform.instructions_and_examples import instructions_page
from platform.training import training
from platform.experiment import experiment


def init():
    st.set_page_config(layout="wide")
    st.title('Machine-Translation Evaluation')
    if 'cur_page' not in st.session_state:
        #st.session_state.cur_page = 'before'
        st.session_state.cur_page = 'instructions'
        # st.session_state.samples_csv = load()


def load_page():
    if st.session_state.cur_page == 'before':
        before()
    elif st.session_state.cur_page == 'instructions':
        instructions_page()
    elif st.session_state.cur_page == 'training':
        training()
    elif st.session_state.cur_page == 'experiment':
        experiment()
    elif st.session_state.cur_page == 'after':
        #after()
        #after_with_all_survey()
        demographics()
    elif st.session_state.cur_page == 'finish':
        st.write('Thank you for participating in the experiment!')
    else:
        st.error('Invalid page state')


if __name__ == '__main__':
    init()
    load_page()
