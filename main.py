import streamlit as st
from after_questionnaire import validated
from before_questionnaire import before
from instructions_and_examples import instructions_page
from training import training
from experiment import experiment, qualification
import gspread
import pandas as pd
import pandas
import time


valid_usernames = ['1','2','3','4','5','6','7','8','9','10','test']
assign_dictionary = {'5':'65.1', '8':'65.2', '3':'75.1', '10':'75.2', '1':'85.1', '6':'85.2', '7':'95.1', '2':'95.2','9':'100.1', '4':'100.2','test':'from_bug'}
def sign_in():
    with st.columns([1, 2, 1])[1]:
        #st.header('Machine-Translation Evaluation')
        st.markdown('Hello! Please enter your Worker ID')
        st.text_input('Worker ID', key='username_box')

        st.button('Next', key='next_button0', on_click=record_name)


def record_name():
    if not st.session_state.username_box:
        st.error('You must enter a valid Worker ID')
    else:
        st.session_state.username = st.session_state.username_box
        if "ws_sentences" not in st.session_state:
            gc = gspread.service_account_from_dict(st.secrets["credentials"])
            sh = gc.open("short_translation_mine_translations")
            st.session_state.ws_sentences = sh.worksheet("qualification_spanish_sentences")

        if "ws_answers" not in st.session_state:
            gc = gspread.service_account_from_dict(st.secrets["credentials"])
            sh = gc.open("short_translation_mine_translations")
            st.session_state.ws_answers = sh.worksheet("qualification_spanish_answers")

        if "row" not in st.session_state:
            row_count = 0
            while True:
                row_count += 1
                row_values = st.session_state.ws_answers.row_values(row_count)
                if not any(row_values):
                    break

            place = 'A' + str(row_count)
            st.session_state.ws_answers.update(place, [st.session_state.username])
            st.session_state.row=row_count

        st.session_state.cur_page = 'experiment'


def init():
    st.set_page_config(layout="wide")
    with st.columns([1, 2, 1])[1]:
        st.title('Machine-Translation Evaluation')


    if 'cur_page' not in st.session_state:
        #st.session_state.cur_page = 'before'
        #st.session_state.cur_page = 'instructions'
        st.session_state.cur_page = 'sign_in'
        st.session_state.start_time = time.time()
        # st.session_state.samples_csv = load()



def load_page():
    if st.session_state.cur_page == 'before':
        before()
    if st.session_state.cur_page == 'sign_in':
        sign_in()
    elif st.session_state.cur_page == 'instructions':
        instructions_page()
    # elif st.session_state.cur_page == 'training':
    #     #training()
    elif st.session_state.cur_page == 'experiment':
        #experiment()
        qualification()
    elif st.session_state.cur_page == 'after':
        #after()
        #after_with_all_survey()
        #demographics()
        validated()
    elif st.session_state.cur_page == 'finish':
        with st.columns([1, 2, 1])[1]:
            st.write('Thank you for participating in the experiment!')
    else:
        st.error('Invalid page state')


if __name__ == '__main__':

    init()
    load_page()
