from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import col, count, row_number
from etl_job import extract_data, transform_data

def run_analysis():
    spark = SparkSession.builder.appName("Reddit_Subreddit_Top_Words").getOrCreate()

    # Extraction
    df = extract_data(spark)

    # Core Analysis Logic
    # Find the Top 10 subreddits by post count
    top_subreddits_df = (
        df.groupBy("subreddit").count().orderBy(col("count").desc()).limit(10)
    )

    # Extract subreddit names for filtering
    top_10_list = [row["subreddit"] for row in top_subreddits_df.collect()]

    # Filter main DataFrame
    filtered_df = df.filter(col("subreddit").isin(top_10_list))

    # Transformation (Cleaning and Tokenization)
    clean_words_df = transform_data(filtered_df)

    # Aggregate: Count word frequencies per subreddit
    word_counts = clean_words_df.groupBy("subreddit", "word").agg(
        count("*").alias("frequency")
    )

    # Ranking: Top 3 words per subreddit using Window Function
    window_spec = Window.partitionBy("subreddit").orderBy(col("frequency").desc())
    ranked_words = word_counts.withColumn("rank", row_number().over(window_spec))

    # Final Result
    final_result = ranked_words.filter(col("rank") <= 3).orderBy("subreddit", "rank")
    final_result.show(30, truncate=False)

    spark.stop()

if __name__ == "__main__":
    run_analysis()
