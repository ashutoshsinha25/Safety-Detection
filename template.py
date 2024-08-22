import os 
from pathlib import Path 
import logging 

logging.basicConfig(level=logging.INFO, format='[%(asctime)s: %(message)s:]')
project_name = "safety"

list_of_files=[
    'data/.gitkeep',
    "setup.py",
    'app.py',
    'requirements.txt',

    f'{project_name}/__init__.py',
    # project componenets
    f'{project_name}/components/__init__.py',
    f'{project_name}/components/data_ingestion.py',
    f'{project_name}/components/data_validation.py',
    f'{project_name}/components/model_trainer.py',
    f'{project_name}/components/model_pusher.py',
    # project configuration
    f'{project_name}/configuration/__init__.py',
    f'{project_name}/configuration/s3_operations.py',
    # project constants
    f'{project_name}/constant/__init__.py',
    f'{project_name}/constant/training_pipeline/__init__.py',
    f'{project_name}/constant/application.py',
    # project entity
    f'{project_name}/entity/__init__.py',
    f'{project_name}/entity/artifact_entity.py',
    f'{project_name}/entity/config_entity.py',
    # project pipeline 
    f'{project_name}/pipeline/__init__.py',
    f'{project_name}/pipeline/training_pipeline.py',
    # project utils 
    f'{project_name}/utils/__init__.py',
    f'{project_name}/utils/main_utils.py',
    # logger and exceptions
    f'{project_name}/exception/__init__.py',
    f'{project_name}/logger/__init__.py',
    'notebook/main.ipynb',
    'template/index.html',
    'flowchart/test.jpeg',
    "Dockerfile",
    '.dockerignore'
]


for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename = os.path.split(filepath)
    # for dir
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory: {filedir} for the file {filename}")
    # for files 
    if not os.path.exists(filename) or os.path.getsize(filename)==0:
        with open(filepath, 'w') as f:
            ...
            logging.info(f"creating empty file: {filename}")
    else:
        logging.info(f"{filename} already exist")