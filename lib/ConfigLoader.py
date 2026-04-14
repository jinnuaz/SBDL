import configparser
from pyspark import SparkConf

def get_config(env):
    config = configparser.ConfigParser()
    config.read("conf/sbdl.conf")
    conf = {}
    for (key, value) in config.items(env):
        conf[key] = value
    return conf

def get_spark_conf(env):
    spark_conf = SparkConf()
    # This initializes a new SparkConf object.
    # This is a specialized dictionary-like object that Spark uses to understand
    # settings like memory allocation, the app name, or the number of cores to use.
    config = configparser.ConfigParser()
    # This creates an instance of Python's built-in configparser.
    # This library is designed to read files that look like Windows INI files,
    # which are organized into [sections] with key=value pairs.
    config.read("conf/spark.conf")
    for (key, value) in config.items(env):
        spark_conf.set(key, value)
    # For every setting found in that section, it applies it to the Spark configuration object.
    # For example, if your file has spark.app.name = MyCoolApp, it executes spark_conf.set("spark.app.name", "MyCoolApp").
    return spark_conf


def get_data_filter(env, data_filter):
    conf = get_config(env)
    return "true" if conf[data_filter] == "" else conf[data_filter]

# Example Scenario
# Imagine your conf/sbdl.conf looks like this:
#
# Ini, TOML
# [DEV]
# customer_filter = region = 'NY'
#
# [PROD]
# customer_filter =
# If you run get_data_filter("DEV", "customer_filter"):
#
# It finds "region = 'NY'".
#
# The code uses this in a query: df.filter("region = 'NY'").
#
# If you run get_data_filter("PROD", "customer_filter"):
#
# It finds an empty string "".
#
# The function returns "true".
#
# The code uses this in a query: df.filter("true") (which returns all records).