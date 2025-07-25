import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
import pyspark.sql.functions as F

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Load from S3
input_path = "s3://product-demand-forecast/raw/train.csv"
df = spark.read.option("header", True).csv(input_path)

# Drop nulls and convert date
df = df.dropna(subset=['date', 'store_nbr', 'item_nbr', 'unit_sales'])
df = df.withColumn("timestamp", F.to_date("date", "yyyy-MM-dd"))

# Create item_id and sanitize sales
df = df.withColumn("item_id", F.concat_ws("_", df["store_nbr"], df["item_nbr"]))
df = df.withColumn("target_value", F.when(F.col("unit_sales") < 0, 0).otherwise(F.col("unit_sales")))

# Select required fields
df_final = df.select("item_id", "timestamp", "target_value")

# Write to S3
output_path = "s3://product-demand-forecast/processed/forecast_input.csv"
df_final.write.mode("overwrite").option("header", True).csv(output_path)

job = glueContext.create_job(args['JOB_NAME'])
glueContext.commit()
