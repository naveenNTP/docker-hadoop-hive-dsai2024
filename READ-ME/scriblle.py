#refer later

from pyspark.sql import SparkSession

# Create a Spark session with Hadoop configuration
spark = SparkSession.builder \
    .appName("Spark HDFS Example") \
    .master("spark://spark-master:7077") \
    .config("spark.hadoop.fs.defaultFS", "hdfs://namenode:9000") \
    .config("spark.hadoop.io.compression.codecs", "org.apache.hadoop.io.compress.SnappyCodec") \
    .getOrCreate()

# HDFS path
hdfs_path = "/path/to/data"

# Write data to HDFS with compression
df = spark.createDataFrame([(1, "foo"), (2, "bar")], ["id", "value"])
df.write.option("compression", "snappy").csv(hdfs_path)

# Read data from HDFS
df_read = spark.read.csv(hdfs_path)

# Show the data
df_read.show()

# Stop the Spark session
spark.stop()
