import boto3
import json
import os


def load_aws_config():
    with open("config/aws_config.json") as f:
        return json.load(f)


def upload_to_s3(file_path):
    try:
        config = load_aws_config()

        s3 = boto3.client(
            "s3",
            aws_access_key_id=config["aws_access_key"],
            aws_secret_access_key=config["aws_secret_key"],
            region_name=config["region"]
        )

        file_name = os.path.basename(file_path)

        s3.upload_file(
            file_path,
            config["bucket_name"],
            file_name
        )

        print(f"{file_name} uploaded to AWS S3 successfully")

    except Exception as e:
        raise Exception(f"S3 Upload Error: {e}")