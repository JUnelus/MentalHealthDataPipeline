from src.data_loader import load_data, save_local_csv
from src.s3_uploader import upload_to_s3
import os
from dotenv import load_dotenv
import sys

# Add /app to the Python path
sys.path.append('/app')

# Load environment variables from .env file
load_dotenv()

def main():
    # Load Kaggle data
    data = load_data()

    if data:
        # Loop through all the datasets, save locally and upload to S3
        for key, df in data.items():
            local_file = f"data/{key}.csv"
            save_local_csv(df, local_file)

            # Upload to AWS S3
            bucket_name = os.getenv('AWS_S3_BUCKET_NAME')
            upload_to_s3(local_file, bucket_name)
    else:
        print("No data to upload.")


if __name__ == "__main__":
    main()
