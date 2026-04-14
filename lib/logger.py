class Log4j(object):
    def __init__(self, spark):
        log4j = spark._jvm.org.apache.log4j
        self.logger = log4j.LogManager.getLogger("sbdl")

#         /*
#         spark._jvm
#         1. Python sends instruction
#         2. Through Py4J
#         3. JVM executes it using Spark
#         4. Result comes back
#         This is the gateway from Python → JVM
#         _jvm is provided by PySpark
#         Internally uses Py4J
#         Lets you access Java classes from Python
# #-----------------------------------------------------------------------
#         org.apache.log4j -This is pure Java package navigation
#        */

    def warn(self, message):
        self.logger.warn(message)

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)

    def debug(self, message):
        self.logger.debug(message)


