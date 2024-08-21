import os
from dotenv import load_dotenv 
_ = load_dotenv() 


AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_REGION_NAME = "us-east-1"



ARTIFACTS_DIR: str = 'artifacts'



# data ingestion related constant 
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_S3_DATA_NAME: str = "isd_data_mini.zip"
DATA_BUCKET_NAME = "yolov7-safety"



# data valiadation related constant 
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_STATUS_FILE = 'status.txt'
DATA_VALIDATION_ALL_REQUIRED_FILES = ["images", "labels", "classes.names", "train.txt", "val.txt"]