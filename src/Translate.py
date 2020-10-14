import boto3
import os

from nltk.translate.bleu_score import sentence_bleu
from dotenv import load_dotenv
from google.cloud import translate_v2 as translate


class Translate:
    
    """
    A class used to give solution to the third task of the homework.
    
    ...
    
    Attributes
    ----------
    lang1_data : str
        string that contains the name of the file where the data from the first
        language is.
        
    lang2_data : str
        string that contains the name of the file where the data from the second
        language is.
    
    Methods
    -------
    env_variables(env_file, env_json):
        Reads the data from the files and sets up the env variables.
    
    preprocess_data():
        Reads and preprocesses the data contained in the two files and assigns the 
        first NUM_LINES_TO_PROCESS of the file to a list.
    
    translate_bleu():
        Translate the texts (from english to spanish) using AWS Translate API 
        and Cloud Translation API and calculates the bleu scores of the translation 
        and the original text (spanish).
    """
    
    def __init__(self, lang1_data=None, lang2_data=None):
        
        """
        Constructs all the necessary attributes for the translate object.

        Parameters
        ----------
        lang1_data : str
            string that contains the name of the file where the data from the first
            language is.
        
        lang2_data : str
            string that contains the name of the file where the data from the first
            language is.
        """
        
        self.lang1_data = lang1_data
        self.lang2_data = lang2_data
        self.__aws_auth = {}
        self.lang1 = None
        self.lang2 = None
        
    def env_variables(self, env_file, env_json):
        
        """
        Reads the data from the files and sets up the env variables.
        
        Parameters
        ----------
        env_file : str
            string that contains the file where the AWS API keys are.
            
        env_json : str
            string that contains the file where the GCP API keys are.
            
        Returns
        -------
        None
        """
        
        load_dotenv(env_file)

        self.__aws_auth['access_key'] = os.getenv("AWS_ACCESS_KEY_ID")
        self.__aws_auth['secret_access_key'] = os.getenv("AWS_SECRET_ACCESS_KEY")
        self.__aws_auth['session_token'] = os.getenv("AWS_SESSION_TOKEN")
        self.__aws_auth['region'] = os.getenv("REGION_NAME")

        os.environ["GOOGLE_APPLICATIO