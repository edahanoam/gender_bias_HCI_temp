import pandas as pd
import sys

def balanced_sample(file_path, k):
    # Load the data from a CSV file
    data = pd.read_csv(file_path)
    print(data.columns)

    # Check if 'stereotype' and 'predicted_gender' columns exist
    if 'stereotype' not in data.columns or 'predicted gender' not in data.columns:
        raise ValueError("The required columns are not in the dataframe.")

    # Group the data by 'stereotype' and 'predicted_gender' and sample from each group
    grouped = data.groupby(['stereotype', 'predicted gender'])
    samples = grouped.apply(lambda x: x.sample(min(len(x), k//len(grouped)), replace=False) if len(x) > k//len(grouped) else x)

    samples = samples.reset_index(drop=True)

    return samples

if __name__ == '__main__':
    # Usage example
    # Usage example
    file_path = sys.argv[1]
    num_of_sample = int(sys.argv[2])
    sampled_data = balanced_sample(file_path, num_of_sample)
    sampled_data.to_csv('mine.csv', index=False)
