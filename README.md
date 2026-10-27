# Extractive and Abstractive Text Summarization for Tamil

**Python · Tamil NLP · scikit-learn · mBART · mT5 · ROUGE evaluation**

Turns long Tamil documents into concise summaries using two approaches: three extractive methods that select the most important sentences, and fine-tuned Transformer models that write new summary text. Every method is scored against reference summaries with ROUGE.

## Results at a glance

| Extractive methods | Abstractive models |
| --- | --- |
| ![Comparison of extractive summarization methods](semester-material/showcase/extractive-comparison.jpg) | ![Comparison of abstractive models](semester-material/showcase/abstractive-comparison.jpg) |
| Sentence weighting scored highest on ROUGE-1 (about 0.52) and ROUGE-2; sentence clustering was best on ROUGE-L. | mT5 scored highest on all three measures: ROUGE-1 0.47, ROUGE-2 0.33, ROUGE-L 0.42. |

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
semester-material/        # mBART and T5 notebooks, standalone scripts
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

## More results

The [results gallery](Results/Images/) has summary-length distributions, word-frequency analysis, t-SNE plots of the clustering and weighting methods, and abstractive hyperparameter settings.

| Extractive experiments | Abstractive experiments |
| --- | --- |
| ![Extractive experiment results](Results/Images/extractive%20Results.jpeg) | ![Abstractive experiment results](Results/Images/Abstractive%20Results.jpeg) |

## Abstractive models and standalone scripts

The [semester-material](semester-material/README.md) folder holds the Transformer experiments and the extractive methods as standalone Python scripts:

- [mBART notebook](semester-material/mbart.ipynb)
- [T5 fine-tuning notebook](semester-material/t5-fine-tuning.ipynb)
- [Sentence scoring](semester-material/sentence_scoring.py), [sentence weighting](semester-material/sentence_weighing.py) and [sentence clustering](semester-material/sentence_clustering.py) scripts
- [Source inventory](semester-material/SOURCE_INDEX.md)

Datasets and trained weights are not stored in the repository; see the notebooks for the expected paths.
