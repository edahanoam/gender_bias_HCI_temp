

import streamlit as st
from experiment_helper import display_single_example, save_annotation


def load_all_training_data():
    st.session_state.training_sample_index = 0
    st.session_state.show_feedback = False
    sample_1 = {'input': 'I am a student', 'output': 'אני תלמידה', 'gold': 'אני תלמיד'}
    return [sample_1]


def next_page():
    st.session_state.cur_page = 'experiment'


def next_sample():
    save_annotation()
    st.session_state.training_sample_index += 1
    st.session_state.correct = None
    st.session_state.show_feedback = False


def toggle_feedback():
    user_translation = st.session_state.training_translation
    if user_translation == st.session_state.training_data[st.session_state.training_sample_index]['gold']:
        st.session_state.correct = 1
    else:
        st.session_state.correct = 0
    st.session_state.show_feedback = True


def show_feedback():
    if st.session_state.correct == 1:
        st.success("You translation is correct!")
    else:
        st.error("You translation is incorrect!")
    current_sample = st.session_state.training_data[st.session_state.training_sample_index]
    st.markdown(f"Original sentence: {current_sample['input']}")
    st.markdown(f"Model's suggested translation: {current_sample['output']}")
    st.markdown(f"Your translation: {st.session_state.training_translation}")
    st.markdown(f"Gold translation: {current_sample['gold']}")
    st.button('Next sample', key='next_button4', on_click=next_sample)


def training():
    if 'training_data' not in st.session_state:
        st.session_state.training_data = load_all_training_data()
    if st.session_state.show_feedback:
        show_feedback()
    else:
        if st.session_state.training_sample_index >= len(st.session_state.training_data):
            st.write('Training is over!')
            st.button('Start testing', key='next_button3', on_click=next_page)
        else:
            current_sample = st.session_state.training_data[st.session_state.training_sample_index]
            display_single_example(current_sample, toggle_feedback)


