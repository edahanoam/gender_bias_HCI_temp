import sys
import pandas as pd

from transformers import pipeline



def get_translation(df,translator):
    translations=[]
    for row in df.itertuples():
        cur_translation = translator(row.sentence_text)
        print(cur_translation)
        translations.append(cur_translation)

    df['model_translations'] = translations
    return df



if __name__ == '__main__':

    print("yay")
    source_lang = "en"
    target_lang = "he"

    file_path = sys.argv[1]
    data = pd.read_csv(file_path)
    checkpoint ='Helsinki-NLP/opus-mt-en-he'


    translator = pipeline("translation_en_to_he", model=checkpoint,  max_length=400)
    new_data =get_translation(data,translator)
    new_data.to_csv('new_mine.csv', index=False)
