
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

class Sentiment:
    """
    A class used to give solution to the first task of the homework.
    
    ...
    
    Attributes
    ----------
    rawdata : str
        string that contains the name of the file where the data is.
    
    Methods