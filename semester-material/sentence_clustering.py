import pandas as pd
import sys
import sklearn
import math

from util.preprocessor import Preprocessor
from util.word_counter import WordCounter
from sklearn.cluster   import KMeans
from util.distance     import euclideanDistance

import os

# Print current working directory
print("Current working directory:", os.getcwd())

# List files in the current directory
print("Files in current directory:", os.listdir())


def termWeightFN(s, counter, sCount, TYPE):
  sentencesWithWord = lambda w: filter(lambda sd: counter.isWordIn(sd, w), counter.sentenceDict)

  booL = lambda w: 1 if counter.isWordIn(s, w) else 0
  tF   = lambda w: counter.fetchSentenceWordCount(s, w) if counter.isWordIn(s, w) else 0
  idF  = lambda w: math.log( float(sCount) / len(sentencesWithWord(w)) ) if counter.isWordIn(s, w) else 0
  tFIdf= lambda w: tF(w) * idF(w)

  # BOOL
  if TYPE == 1:
    return (booL)

  # TF
  elif TYPE == 2:
    return (tF)

  # IDF
  elif TYPE == 3:
    return (idF)

  # TF-IDF
  elif TYPE == 4:
    return (tFIdf)

def normalizeFeatures(features):
  normalized = []
  for f in features:
    normalized.append(list(map(lambda ft: float(ft) / max(f) if max(f) > 0 else 0, f)))
  return normalized


def buildFeatures(preprocessed, counter, TYPE):
  vocabulary = counter.vocabulary()

  print("Size of vocabulary:", len(vocabulary))
  print("Content of vocabulary:", vocabulary)

  features = []

  for s in range(preprocessed.sCount):
    sFeatures = map(termWeightFN(s, counter, preprocessed.sCount, TYPE), vocabulary)
    sFeatures = list(sFeatures)  # Convert map object to list
    features.append(sFeatures)

  print("Size of features array:", len(features))
  print("Content of features array:", features)

  return normalizeFeatures(features)


def sentenceSelect(kmeans, preprocessed, features):
  summary = []

  for i in set(kmeans.labels_):
    sentencesInCluster = [s for s in range(preprocessed.sCount) if kmeans.labels_[s] == i]

    sortedByClosenessToCentroid = sorted(sentencesInCluster, key=lambda s: euclideanDistance(kmeans.cluster_centers_[i], features[s]))

    summary.append(sortedByClosenessToCentroid[0])

  return summary


def generateSummary(data, NGRAMS, CLUSTERS, TYPE):
  summaries = []

  for text in data:
    p = Preprocessor(text, NGRAMS).parse()
    counter = WordCounter(p.sCount).count(p.processed)
    features = buildFeatures(p, counter, TYPE)

    print("Size of features array:", len(features))
    print("Content of features array:", features)

    kmeans = KMeans(n_clusters=CLUSTERS,
                    init="k-means++",
                    random_state=500,
                    tol=1e-10,
                    copy_x=True)

    print("Size of data array:", len(data))

    kmeans.fit(features)

    summary = sentenceSelect(kmeans, p, features)
    summaries.append([p.sentences[s] for s in sorted(summary)])

  return summaries


if __name__ == "__main__":
    try:
        data = pd.read_csv("Tamil wiki-data.csv")["Text"].tolist()
    except FileNotFoundError:
        print("Error: Tamil wiki-data.csv not found.")
        sys.exit(1)

    NGRAMS = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    CLUSTERS = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    TYPE = int(sys.argv[3]) if len(sys.argv) > 3 else 1

    summaries = generateSummary(data, NGRAMS, CLUSTERS, TYPE)

    # Print summaries for debugging
    for summary in summaries:
        print(summary)

    # Write summaries to a CSV file
    summaries_df = pd.DataFrame({"Summary": summaries})
    summaries_df.to_csv("ClusterSummary.csv", index=False)
