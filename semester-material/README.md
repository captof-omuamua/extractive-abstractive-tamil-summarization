# Tamil Text Summarization

### Extractive methods and Transformer-based abstractive experiments.

**Python · Tamil NLP · mBART · T5 · Extractive summarization**

An NLP project comparing extractive Tamil summarization methods and experimenting with pretrained sequence-to-sequence models. It includes clustering, sentence scoring/weighing, and mBART/T5 notebooks.

![Comparison of extractive summarization methods](showcase/extractive-comparison.jpg)

*ROUGE comparison of the three extractive methods.*

## What is included

- Frequency-based sentence extraction
- Sentence scoring, weighting, and clustering scripts
- mBART and T5 fine-tuning experiments
- ROUGE comparison and distribution figures

The repository includes 6 directly browsable source/notebook files and a [source archive](source.zip) containing 6 files with their package structure preserved. See [SOURCE_INDEX.md](SOURCE_INDEX.md) for its contents.

## Workflow

```mermaid
flowchart LR
    N0["Tamil text"]
    N1["Extraction or seq2seq model"]
    N2["Summary"]
    N3["Reference-based evaluation"]
    N0 --> N1 --> N2 --> N3
```

## Results

![Comparison of abstractive models](showcase/abstractive-comparison.jpg)

*mT5 scored highest of the three abstractive models on ROUGE-1, ROUGE-2 and ROUGE-L.*

## Explore / run

Open the notebooks and set the dataset and model paths before running. The Tamil XLSum archive remains local and is not redistributed. The scripts need the preprocessing libraries they import and a compatible Transformers version.

### Direct source files

- [mbart.ipynb](mbart.ipynb)
- [sentence_clustering.py](sentence_clustering.py)
- [sentence_scoring.py](sentence_scoring.py)
- [sentence_weighing.py](sentence_weighing.py)
- [tamil-text-summarization-extractive-approach.ipynb](tamil-text-summarization-extractive-approach.ipynb)
- [t5-fine-tuning.ipynb](t5-fine-tuning.ipynb)

## Notes

This Tamil project is separate from the later Malayalam summarization work. More details are in [SOURCE_NOTES.md](SOURCE_NOTES.md).
