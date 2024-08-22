import os,sys
import yaml
from safety.utils.main_utils import read_yaml_file
from six.moves import urllib
from safety.logger import logging
from safety.exception import SDException
from safety.constant.training_pipeline import *
from safety.entity.config_entity import ModelTrainerConfig
from safety.entity.artifact_entity import ModelTrainerArtifact


class ModelTrainer:
    def __init__(
        self,
        model_trainer_config: ModelTrainerConfig,
    ):
        self.model_trainer_config = model_trainer_config


    def initiate_model_trainer(self,) -> ModelTrainerArtifact:
        logging.info("Entered initiate_model_trainer method of ModelTrainer class")
        try: 
            if os.path.exists(self.model_trainer_config.trained_model):
                # logging.info("export.zip file found, using it instead of training the model")
                logging.info("export.zip/best.pt file found, using it instead of training the model")
                # Unzipping export.zip
                # os.makedirs("trained_model", exist_ok=True)
                os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)
                os.system(f"cp {self.model_trainer_config.trained_model}/best.pt {self.model_trainer_config.model_trainer_dir}/")
                trained_model_file_path = os.path.join("trained_model", "best.pt")
                if not os.path.exists(trained_model_file_path):
                    raise FileNotFoundError(f"Model file best.pt not found in export.zip")
                model_trainer_artifact = ModelTrainerArtifact(
                    trained_model_file_path=trained_model_file_path,
                )
            else:
                logging.info("No export.zip file found, proceeding with model training")
                
                logging.info("Unzipping data")
                os.system(f"unzip {DATA_INGESTION_S3_DATA_NAME}")
                os.system(f"rm {DATA_INGESTION_S3_DATA_NAME}")
                #Prepare image path in txt file
                train_img_path = os.path.join(os.getcwd(),"images","train")
                val_img_path = os.path.join(os.getcwd(),"images","val")

                #Training images
                with open('train.txt', "a+") as f:
                    img_list = os.listdir(train_img_path)
                    for img in img_list:
                        f.write(os.path.join(train_img_path,img+'\n'))
                    print("Done Training images")


                # Validation Image
                with open('val.txt', "a+") as f:
                    img_list = os.listdir(val_img_path)
                    for img in img_list:
                        f.write(os.path.join(val_img_path,img+'\n'))
                    print("Done Validation Image")

                # download COCO starting checkpoint
                url = self.model_trainer_config.weight_name
                file_name = os.path.basename(url)
                urllib.request.urlretrieve(url, os.path.join("yolov7", file_name))

                #training
                os.system("git clone https://github.com/WongKinYiu/yolov7.git")
                os.system(f"cd yolov7 && python train.py --batch {self.model_trainer_config.batch_size} --cfg cfg/training/custom_yolov7.yaml --epochs {self.model_trainer_config.no_epochs} --data data/custom.yaml --weights 'yolov7.pt'")
                os.system("cp yolov7/runs/train/exp/weights/best.pt yolov7/")
                os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)
                os.system(f"cp yolov7/runs/train/exp/weights/best.pt {self.model_trainer_config.model_trainer_dir}/")
                os.system("rm -rf yolov7/runs")
                os.system("rm -rf images")
                os.system("rm -rf labels")
                os.system("rm -rf classes.names")
                os.system("rm -rf train.txt")
                os.system("rm -rf val.txt")
                os.system("rm -rf train.cache")
                os.system("rm -rf val.cache")

                model_trainer_artifact = ModelTrainerArtifact(
                    trained_model_file_path="yolov7/best.pt",
                )

            logging.info("Exited initiate_model_trainer method of ModelTrainer class")
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")


            return model_trainer_artifact
        except Exception as e:
            raise SDException(e, sys)