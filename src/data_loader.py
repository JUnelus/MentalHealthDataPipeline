import os
import pandas as pd

# Paths to your CSV files
data_files = {
    "mental_illnesses_prevalence": "C:/Users/big_j/PycharmProjects/MentalHealthDataPipeline/data/1- mental-illnesses-prevalence.csv",
    "burden_disease_mental_illness": "C:/Users/big_j/PycharmProjects/MentalHealthDataPipeline/data/2- burden-disease-from-each-mental-illness.csv",
    "major_depression_population": "C:/Users/big_j/PycharmProjects/MentalHealthDataPipeline/data/3- adult-population-covered-in-primary-data-on-the-prevalence-of-major-depression.csv",
    "mental_illnesses_population": "C:/Users/big_j/PycharmProjects/MentalHealthDataPipeline/data/4- adult-population-covered-in-primary-data-on-the-prevalence-of-mental-illnesses.csv",
    "anxiety_disorders_treatment_gap": "C:/Users/big_j/PycharmProjects/MentalHealthDataPipeline/data/5- anxiety-disorders-treatment-gap.csv",
    "depressive_symptoms_us_population": "C:/Users/big_j/PycharmProjects/MentalHealthDataPipeline/data/6- depressive-symptoms-across-us-population.csv",
    "countries_mental_illness_primary_data": "C:/Users/big_j/PycharmProjects/MentalHealthDataPipeline/data/7- number-of-countries-with-primary-data-on-prevalence-of-mental-illnesses-in-the-global-burden-of-disease-study.csv"
}


def load_data():
    """Load and return all the CSV files as pandas DataFrames."""
    dataframes = {}
    for key, file_path in data_files.items():
        try:
            df = pd.read_csv(file_path)
            dataframes[key] = df
            print(f"Loaded {key} successfully.")
        except Exception as e:
            print(f"Error loading {key}: {e}")

    return dataframes


def save_local_csv(df, filename):
    """Save the dataframe locally as CSV."""
    # Ensure the directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df.to_csv(filename, index=False)
    print(f"Saved {filename} locally.")


# Example of how to load and handle the data
if __name__ == "__main__":
    data = load_data()
    for key, df in data.items():
        save_local_csv(df, f"data/{key}.csv")
