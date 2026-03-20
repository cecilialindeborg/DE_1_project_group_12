# DE_1_project_group_12

Data Engineering I (1TD169) Group 12 - Reddit Data Analysis with PySpark

## Project Overview

This project implements a data engineering pipeline using PySpark to analyze Reddit data. It extracts data from HDFS, performs ETL operations, and identifies the most frequent words in the top 10 most active subreddits.

### Key Features

- **ETL Pipeline**: Extracts JSON data from HDFS, cleans text (lowercasing, punctuation removal), and filters out stopwords.
- **Data Analysis**: Identifies the top 10 subreddits by post count and calculates the top 3 most frequent words for each.
- **Scalable Processing**: Built on PySpark to handle large-scale datasets across a Spark cluster.

## Project Structure

```text
.
├── data/                   # Sample data for local testing
├── docs/                   # Documentation and contribution guides
├── notebooks/              # Jupyter notebooks for analysis and benchmarking
├── scripts/                # Shell scripts for running jobs
│   └── run_benchmarks.sh   # Main execution script for Spark jobs
└── src/                    # Source code
    ├── analysis_job.py     # Main analysis logic and Spark session
    ├── config.py           # Configuration, HDFS paths, and stopword lists
    └── etl_job.py          # ETL functions (extract and transform)
```

## Setup & Configuration

The project is configured to run on a Spark cluster. Key configurations can be found in `src/config.py`, including:

- `HDFS_DATA_PATH`: Path to the Reddit dataset in HDFS.
- `STOPWORDS`: List of words to be excluded from the analysis.
- `SCHEMA`: Spark schema for the Reddit data.

## Usage

### Prerequisites

- Apache Spark 3.5.1
- Hadoop/HDFS environment
- Python 3 with `pyspark` and `stop-words` libraries

### Running the Analysis

To execute the Spark job and perform the analysis:

```bash
./scripts/run_benchmarks.sh
```

_Note: Ensure you are running this from within the repository root and have access to the Spark master URL specified in the script (`spark://192.168.2.25:7077`)._

## Results

The results are displayed in the console, showing the top 3 words and their frequencies for each of the top 10 subreddits. Benchmarking results and visualizations can be found in the `notebooks/` directory.
