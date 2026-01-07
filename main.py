'''
In this file we are going to read data about Telco customer churn
'''


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import logging
import warnings
warnings.filterwarnings('ignore')
import sys
from log_file import setup_logging
logger = setup_logging('main')
from Visualization import (
    Senior_gender_vs_churn,
    gender_vs_churn,
    churn_distribution,
    tenure_vs_churn,
    monthly_charges_vs_churn,
    internet_service_vs_gender,
    contract_vs_churn)



class CustomerChurn:
    def __init__(self,path):
        try:
            self.path = path
            self.df = pd.read_csv(self.path)
            logger.info(f'Data loaded Successfully')
            logger.info(f'we have : {self.df.shape[0]} Rows and {self.df.shape[1]} Columns')
            logger.info(f'\n {self.df.to_string()}')

        except Exception as e:
            error_type, error_msg, error_line = sys.exc_info()
            logger.info(f'error in line no :{error_line.tb_lineno}: due to {error_msg}')







if __name__ == "__main__":
    try:

        obj = CustomerChurn('WA_Fn-UseC_-Telco-Customer-Churn.csv')
        gender_vs_churn(obj.df)
        churn_distribution(obj.df)
        tenure_vs_churn(obj.df)
        monthly_charges_vs_churn(obj.df)
        Senior_gender_vs_churn(obj.df)
        internet_service_vs_gender(obj.df)
        contract_vs_churn(obj.df)

    except Exception as e:
        error_type, error_msg, error_line = sys.exc_info()
        logger.info(f'error in line no :{error_line.tb_lineno}: due to {error_msg}')





