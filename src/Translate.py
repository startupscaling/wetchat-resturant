import boto3
import os

from nltk.translate.bleu_score import sentence_bleu
from dotenv import load_dotenv
from google.cloud import translate_v2 as translate


cl