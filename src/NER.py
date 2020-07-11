
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