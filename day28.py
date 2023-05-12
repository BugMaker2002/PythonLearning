from pyspark import SparkConf, SparkContext
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
sc = SparkContext(conf=conf)
my_list = [1, 2, 3, 4]
rdd = sc.parallelize(my_list)
print(rdd.collect())
sc.stop()
