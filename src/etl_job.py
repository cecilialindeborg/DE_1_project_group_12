from pyspark.sql.functions import col, lower, split, explode, regexp_replace
from config import HDFS_DATA_PATH, STOPWORDS, SCHEMA

def extract_data(spark):
    """
    Extract data from HDFS
    """
    # Read from HDFS
    df = spark.read.json("hdfs://192.168.2.25:9000/user/ubuntu/data/reddit_data.json")
    return df

def transform_data(df):
    """Apply cleaning, tokenization, and stopword filtering."""
    # Clean and Tokenize the 'content' column
    # Lowercase, remove punctuation, split by whitespace, and explode into separate rows
    words_df = df.withColumn(
        "clean_content", lower(regexp_replace(col("content"), r"[^\w\s]", ""))
    ).withColumn("word", explode(split(col("clean_content"), r"\s+")))

    # Filter out empty strings and stopwords
    clean_words_df = words_df.filter(
        (col("word") != "") & (~col("word").isin(STOPWORDS))
    )

    return clean_words_df
