#!/bin/bash
~/spark-3.5.1-bin-hadoop3/bin/spark-submit \
  --master spark://192.168.2.25:7077 \
  --conf spark.executor.memory=512m \
  --conf spark.driver.memory=512m \
  --conf spark.cores.max=2 \
  --conf spark.pyspark.python=/usr/bin/python3 \
  --conf spark.pyspark.driver.python=/usr/bin/python3 \
  --py-files ../src/config.py,../src/etl_job.py \
  ../src/analysis_job.py
