[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Detection Of News Written By The ChatGPT Through Authorship Attribution Performed By A Bidirectional LSTM Model

## Table of Content

1. [Overview](#overview)
2. [Research summary](#summary)
3. [Repository structure](#structure)
4. [License](#license)
5. [Authorship and Contact](#contact)

---

## Overview <a name="overview"></a>

This repository contains the code used in the research that produced the article [link]().

## Research summary <a name="summary"></a>

<div style="text-align: justify">

The large language based-model chatbot ChatGPT gained a lot of popularity since its launch and has been used in a wide range of situations. This research centers around a particular situation, when the ChatGPT is used to produce news that will be consumed by the population, causing the facilitation in the production of fake news, spread of misinformation and lack of trust in news sources. Aware of these problems, this research aims to build an artificial intelligence model capable of performing authorship attribution on news articles, identifying the ones written by the ChatGPT. To achieve this goal, a dataset containing equal amounts of human and ChatGPT written news was assembled and different natural processing language techniques were used to extract features from it that were used to train, validate and test three models built with different techniques. The best performance was produced by the Bidirectional Long Short Term Memory (LSTM) Neural Network model, achiving 91.57% accuracy when tested against the data from the testing set.

## Directory structure <a name="structure"></a>

This directory is structured in 4 main folders that are listed and explained below:

- **classifiers**: This folder contains the code used to build, train and test the three modeles proposed in the article. Each model has its own code file with the name of the technique used in its construction as part of the code file name. Along with the code files, there is a folder containing three files with the best LSTM, ANN and XGBoost classifiers trained that can be used to load and test the models.

- **dataset**: This folder contains the data used to train, validate and test the proposed models. The subfolder `new_links` contains information about every news article scraped from the chosen news platforms. For each news site scraped there is a CSV file containing the collected news articles title, publishing date, origin site and acess link. The subfolder `news_pickles` contains the human and ChatGPT news used to assemble the dataset divided in three subsets (train, validation and test) and saved in the Python Pickle library format. Both human and ChatGPT have two files, the first storing the raw news text and the second storing the POS tag sequences extracted from each news article.

- **features**: This folder contains the featuers extracted from the news articles and the code used to extract them. The features were extracted from the already divided dataset (train, validation and test), therefore folder `extracted_featues` has a CSV file for each subset. The content of all three CSVs were also saved in a single pickle file named `processed_features`. It is important to address that the code present on the file `feature_extraction.ipynb` was set to load the news articles directly from the .txt files where they were locally stored that are not present in this repository. To facilitate data loading, the news were later saved on the .pickle files stored in the `dataset` folder from this repository.

- **scraping**: This folder contains the code used to perform web scraping on the chosen news sites. For each news site there is a custom scraper inside the `scrapers` folder. The file `pygooglenews_news.py` has the code used to gather the links that were later used by the scrapers to acess the news.

## **License** <a name="license"></a>

Distributed under the MIT License. See the `LICENSE` file for more information.

## **Authorship and Contact** <a name="contact"></a>

Amanda Ferrari Iaquinta - a.ferrari.iaquinta@gmail.com

Gustavo Voltani von Atzingen - gustavo.von.atzingen@gmail.com

</div>
