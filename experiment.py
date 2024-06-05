
import streamlit as st
from experiment_helper import display_single_example, save_annotation
import csv



def csv_to_format():
    data_array = []

    # Open the CSV file containing your data
    with open('your_dataset.csv', newline='', encoding='utf-8') as csvfile:
        # Create a CSV reader object
        reader = csv.DictReader(csvfile)

        # Loop through rows in the CSV file
        for row in reader:
            # Each row is a dictionary with keys as column headers
            # Append a new dictionary to the list with the required keys
            data_array.append({
                'input': row['input_column_name'],
                'output': row['output_column_name'],
                'gold': row['gold_column_name']
            })


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
