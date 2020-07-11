
import json
import spacy
import random
import matplotlib.pyplot as plt
import warnings

from spacy.training import Example
from spacy.scorer import Scorer
from tqdm import tqdm

warnings.filterwarnings('ignore') #Used to avoid spacy's warnings that make the code difficult to read.

class NER:
    
    """
    A class used to give solution to the second task of the homework.
    
    ...
    
    Attributes
    ----------
    rawdata : str
        string that contains the name of the file where the data is.
    
    Methods
    -------
    read_ner_data():
        Reads the data from the file.
    
    preprocess_data():
        Puts the data in the Spacy training dataset way, which is:
        "{content: str, annotations: {(start, end, tag)}}"
    
    model_trainer():
        Trains the model using a blank spacy model and the training dataset,
        plots the training loss and saves the model to the same path.
        
    model_evaluation():
        Evaluates the model using the F1-Score, Recall and Precision for the
        entities (how well did the model tagged the content).
    
    """
    
    def __init__(self, rawdata=None):
        
        """
        Constructs all the necessary attributes for the ner object.

        Parameters
        ----------
        rawdata : str
            string that contains the name of the file where the data is.
        """
        