from pyspark.sql.functions import mean, max, min, col, count
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.appName("ExerciseSpark")
    .getOrCreate()
)

# Ler os dados do enem 2019
rais = (
    spark
    .read
    .format("csv")
    .option("header", True)
    .option("inferSchema", True)
    .option("delimiter", ";")
    .load("s3://datalake-desafio-mod1/raw-data/")
)


(
    rais
    .write
    .mode("overwrite")
    .format("parquet")
    .save("s3://datalake-desafio-mod1/staging/")
)