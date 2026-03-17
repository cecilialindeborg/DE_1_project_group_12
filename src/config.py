from pyspark.sql.types import StructType, StructField, StringType
from stop_words import get_stop_words

HDFS_DATA_PATH = "hdfs://192.168.2.25:9000/user/ubuntu/data/reddit_data.json"

STOPWORDS = get_stop_words("en")

SCHEMA = StructType(
    [
        StructField("content", StringType(), True),
        StructField("subreddit", StringType(), True),
    ]
)
