from pyspark.sql import SparkSession
from pyspark.sql.functions import col, isnan, when, count, mean, stddev, min, max
from pyspark.sql.types import FloatType

spark = SparkSession.builder.appName("DoubanAnalysis").getOrCreate()

df = spark.read.option("header", "true").csv("s3a://[BUCKET]/douban_movies.csv")

def missing_stats(df):
    return df.select([count(when(isnan(c) | col(c).isNull(), c)).alias(c) for c in df.columns])

df_clean = df.fillna({"rating_score": 0.0, "genres": "未知"})

df_clean.createOrReplaceTempView("movies")
result = spark.sql("""
SELECT year, COUNT(*) AS cnt
FROM movies
GROUP BY year
ORDER BY year
""")
result.show(50)

spark.stop()