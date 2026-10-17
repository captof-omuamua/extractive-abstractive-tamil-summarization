# Extractive and Abstractive Text Summarization for Tamil

A natural language processing project exploring ways to turn long Tamil documents into concise summaries. The work covers text preparation, three extractive summarization methods, and visual comparisons of extractive and abstractive experiment results.

## Summarization methods

### Word frequency

Builds a word-frequency table and uses it to score sentences. Sentences above an average-score threshold are selected to form the summary.

### Sentence weighting

Ranks sentences using word occurrences across the document and a character-difference-based score. The highest-ranked sentences form the summary.

### Sentence clustering

Represents sentences with TF-IDF vectors and groups them using K-Means. A sentence close to each cluster centre is selected to capture different parts of the document.

## Features

- Tamil text loading, cleaning, and document preparation.
- Stopword filtering and sentence scoring.
- Three extractive summarization approaches in a Google Colab notebook.
- CSV exports of original text and generated summaries.
- Summary-length comparisons, word-frequency analysis, and t-SNE visualizations.
- Saved charts and result images from extractive and abstractive experiments.

## Tools used

Python, Google Colab, pandas, NumPy, NLTK, scikit-learn, Matplotlib, WordCloud, and rouge-score.

## Project structure

```text
extractive/
    extractive.ipynb       # Extractive summarization notebook
Results/
    Images/               # Experiment results and visualizations
README.md
```

## Getting started

1. Open [extractive/extractive.ipynb](extractive/extractive.ipynb) in Google Colab.
2. Install the required libraries in a notebook cell:

   ```python
   %pip install pandas numpy matplotlib nltk scikit-learn wordcloud rouge-score
   ```

3. Mount Google Drive when prompted.
4. Add your Tamil text files and Tamil stopword list to Drive, then update the input and output paths in the notebook to match your folders.
5. Run the data preparation cells, followed by the summarization method you want to explore.
6. For the comparison cells, make sure the saved CSV filenames and column names match the files being loaded.

The notebook uses these folders and files in Google Drive:

- `Colab Notebooks/extractiveData/train/train/` and `valid/valid/`: input text files.
- `Colab Notebooks/stopwords/TamilStopWords.txt`: Tamil stopwords.
- `Colab Notebooks/Tamil_wiki-data.csv`: prepared text dataset.
- `NLP_Results/` and `ClusteringResults/`: summary exports and comparison inputs.

Create your output folders before exporting results. The input dataset and stopword file are supplied separately.

The notebook downloads NLTK's `punkt` resource. If your NLTK version also requests `punkt_tab`, run:

```python
import nltk
nltk.download("punkt")
nltk.download("punkt_tab")
```

## Results

Explore the [results gallery](Results/Images/) for comparison charts, summary-length distributions, t-SNE plots, and abstractive experiment figures.

| Extractive experiments | Abstractive experiments |
| --- | --- |
| ![Extractive experiment results](Results/Images/extractive%20Results.jpeg) | ![Abstractive experiment results](Results/Images/Abstractive%20Results.jpeg) |

## Acknowledgments

Developed with guidance and support from **Sachin Kumar S** and the **Department of AI, Amrita Vishwa Vidyapeetham, Coimbatore**.
