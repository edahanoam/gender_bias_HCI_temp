""" Usage:
    <file-name> --in=CSV_TRANSLATIONS --org=ORIGINAL_TEXT_COLUMN --trans=TRANSLATION_COLUMN --out=OUT_FILE [--debug]
"""

import pandas as pd
from docopt import docopt




def convert_csv_to_txt(inp_fn,original_text_column,translation_column,out_fn):
    # Load the CSV file
    df = pd.read_csv(inp_fn)

    # Create a new text file with sentences and translations
    with open(out_fn, 'w', encoding='utf-8') as f:
        for index, row in df.iterrows():
            # Write the original sentence and the translation separated by ' ||| '
            f.write(f"{row[original_text_column]} ||| {row[translation_column]}\n")


if __name__ == '__main__':
    print("check")
    # Parse command line arguments
    args = docopt(__doc__)
    inp_fn = args["--in"]
    original_text_column = args["--org"]
    translation_column = args["--trans"]
    out_fn = args["--out"]
    convert_csv_to_txt(inp_fn,original_text_column,translation_column,out_fn)