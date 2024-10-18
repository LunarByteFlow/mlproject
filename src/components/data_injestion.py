# AIM: Read the data set from an externel data source
import os
import sys
from src.exception import CustomException, error_message_detail
from src.logger import logging
# from src.exception import CustomException
# from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass


# Ab humary pas jo is type ki information hoti hy k data kahan par or kahan se lakar save 
# krna hy wo data injestion class me rakhty hain humog
@dataclass
class DataInjestionConfig:
    train_data_path : str = os.path.join('artifacts','train.csv')
    test_data_path : str = os.path.join('artifacts','test.csv')
    raw_data_path : str = os.path.join('artifacts','raw.csv')


class DataInjestion:
    def __init__(self):
        self.injestion_config = DataInjestionConfig()

    def initiate_data_injestion(self):
        logging.info("Entered the data injestion method or component.")
        try:
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.injestion_config.train_data_path),exist_ok = True)
            df.to_csv(self.injestion_config.raw_data_path,index = False,header = False)
            logging.info("Train Test Split instantiated")
            train_set,test_set = train_test_split(df,test_size = 0.2, random_state = 42)
            train_set.to_csv(self.injestion_config.train_data_path,index = False,header = False)
            test_set.to_csv(self.injestion_config.test_data_path,index = False,header = False)
            logging.info("Injestion of the data is completed successfully")
            return(
                self.injestion_config.train_data_path,
                self.injestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)
        
           

if __name__ == '__main__':
    obj = DataInjestion()
    obj.initiate_data_injestion()