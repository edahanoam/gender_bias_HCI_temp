
import streamlit as st
from experiment_helper import display_single_example, save_annotation


def load_all_test_data():
    st.session_state.test_sample_index = 0
    sample_1 = {'input': 'I am a teacher', 'output': 'אני מורה', 'gold': 'אני מורה'}
    return [sample_1]


def next_page():
    st.session_state.cur_page = 'after'


def next_sample():
    st.session_state.test_sample_index += 1
    save_annotation()


def experiment():
    if 'test_data' not in st.session_state:
        st.session_state.test_data = load_all_test_data()
    if st.session_state.test_sample_index >= len(st.session_state.test_data):
        st.write('Testing is over!')
        st.button('Continue', key='next_button3', on_click=next_page)
    else:
        current_sample = st.session_state.test_data[st.session_state.test_sample_index]
        display_single_example(current_sample, next_sample)
