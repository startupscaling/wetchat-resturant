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
        Translate the texts (from english 