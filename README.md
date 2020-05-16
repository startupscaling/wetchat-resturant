# NLP Module Project

This project was carried out to solve three specific tasks related to NLP.

## Description

The project has three classes that are used throughout the program, each of them has the purpose of solving the following tasks:
* <b>Sentiment Analysis for movie reviews</b>:
    For this task I selected the "distilbert-base-uncased-finetuned-sst-2-english" for running a sentiment analysis on a movie reviews dataset, then the output printed     to the terminal.
* <b>Training a NER Model for a medical purpose</b>:
    For this task a model from scratch using Spacy and the Medical NER dataset (https://www.kaggle.com/datasets/finalepoch/medical-ner), the training loss graph can be     viewed when running the program, also some metrics are used to evaluate the model.
    
    <p align="center"><img style="width: 500px; height: 400px;" src="loss_graph.jpg" alt="loss_graph"></p>
    
* <b>Obtaining the Bleu Score of translations (english to spanish) made by AWS and GCP Translation APIs</b>:
    For this task we will use the AWS and GCP