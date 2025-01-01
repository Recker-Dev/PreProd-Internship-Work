# NLP with Hugging Face Transformers

This project demonstrates the capabilities of the Hugging Face Transformers library for various Natural Language Processing (NLP) tasks, including sentiment analysis, text generation, question answering, and text summarization. It showcases how to use pre-trained models to analyze and generate text, answer questions based on context, and summarize textual information.

## Project Setup

1. **Create a Conda Environment:**

```bash
conda create --name nlp_env -y
```

2. **Activate the Environment:**

```bash
conda activate nlp_env
```

3. **Requirements and pip modules**

- Python 3.10 or higher
- Install necessary libraries:

```bash
pip install -r requirements.txt
```

## Using the Project

1. **Open the Jupyter Notebook:**

   Launch Jupyter Notebook or Google Colab and open the `huggingFace_transformers_introduction.ipynb` notebook file (or the name of your notebook file).

2. **Execute the Code Cells:**

   Run the code cells in the notebook sequentially to observe the different NLP tasks in action.

**Models Used:**

- `distilbert/distilbert-base-uncased-finetuned-sst-2-english` (Sentiment Analysis)
- `openai-community/gpt2` (Text Generation)
- `deepset/roberta-base-squad2` (Question Answering)
- `cnicu/t5-small-booksum` (Text Summarization)

**Problem Statements Solved:**

- Determining the sentiment expressed in a given text.
- Generating creative text based on a provided prompt, mimicking the style of Shakespeare's writing.
- Extracting answers to questions from a given context.
- Summarizing a lengthy text into a concise and informative summary.

<br><br>

# Sentiment Analysis on Yelp Reviews

This project demonstrates how to perform sentiment analysis on Yelp reviews using a pre-trained BERT model. It scrapes reviews from a Yelp page, processes them, and predicts an overall outlet rating based on the sentiment scores of individual reviews.

## Using the Project

1. **Open the Jupyter Notebook:**

   Launch Jupyter Notebook or Google Colab and open the `huggingFace_RealWorldApplication_ReviewSentimentAnalysis.ipynb` notebook file (or the name of your notebook file).

2. **Execute the Code Cells:**

   Run the code cells in the notebook sequentially to observe the different NLP tasks in action.

## How it Works

1. **Data Extraction:** Scrapes reviews from the specified Yelp page using `requests` and `BeautifulSoup`.
2. **Model Loading:** Loads a pre-trained sentiment analysis model (`nlptown/bert-base-multilingual-uncased-sentiment`) from Hugging Face's `transformers` library.
3. **Sentiment Scoring:** Processes each review using the model to obtain a sentiment score between 1 (Very negative) and 5 (Very positive).
4. **Rating Prediction:** Calculates the average sentiment score to predict an overall outlet rating.
5. **Comparison:** Compares the predicted rating with the actual Yelp rating to assess the model's accuracy.

## Usage

1. **Update Yelp URL:** Modify the URL in the code to target the desired Yelp page.
2. **Adjust Class ID:** If the website's structure changes, you might need to update the class ID used for scraping. Refer to the provided video for guidance.
3. **Run the Notebook:** Execute the code cells in the Google Colab notebook to perform sentiment analysis and obtain the predicted rating.

## Disclaimer

- This project is for educational and demonstration purposes only.
- Always adhere to Yelp's terms of service and robots.txt when scraping data.
- The accuracy of the predicted rating may vary depending on the quality and quantity of reviews.

## Folder Structure

```
root/
├── Code/
│   ├── tutorial-video/
│   │   └── How to scrap reviews IRT.mp4
│   └── huggingFace_RealWorldApplication_ReviewSentimentAnalysis.ipynb
│   └── huggingFace_transformers_introduction.ipynb
├── prompts.md
├── README.md
└── requirements.txt
```
