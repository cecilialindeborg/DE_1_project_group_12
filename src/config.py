from pyspark.sql.types import StructType, StructField, StringType
from stop_words import get_stop_words

HDFS_DATA_PATH = "hdfs://130.238.28.63:9000/user/ubuntu/data/reddit_sample.json"

STOPWORDS = get_stop_words("en")

SCHEMA = StructType(
    [
        StructField("content", StringType(), True),
        StructField("subreddit", StringType(), True),
    ]
)
