import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame

# Get job parameters
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Load source data from S3
input_dyf = glueContext.create_dynamic_frame.from_options(
    format_options={"quoteChar": "\"", "withHeader": True, "separator": ","},
    connection_type="s3",
    format="csv",
    connection_options={"paths": ["s3://adith-product-demand-forecast/raw/train.csv"], "recurse": True},
    transformation_ctx="input_dyf"
)

# Clean and transform the data
import pyspark.sql.functions as F

df = input_dyf.toDF()

# Drop nulls in sales
df = df.na.drop(subset=["sales"])

# Create item_id = store_nbr + "_" + family
df = df.withColumn("item_id", F.concat_ws("_", F.col("store_nbr"), F.col("family")))

# Rename columns to match Forecast schema
df = df.withColumnRenamed("date", "timestamp").withColumnRenamed("sales", "target_value")

# Keep only needed columns
df = df.select("item_id", "timestamp", "target_value")

# Convert back to DynamicFrame
output_dyf = DynamicFrame.fromDF(df, glueContext, "output_dyf")

# Write to S3 output location
glueContext.write_dynamic_frame.from_options(
    frame=output_dyf,
    connection_type="s3",
    connection_options={"path": "s3://adith-product-demand-forecast/processed/"},
    format="csv",
    format_options={"withHeader": True}
)

# Commit the job
job.commit()
