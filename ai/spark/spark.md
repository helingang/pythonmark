# spark
- Spark_Core
    1. 初始化Rdd法1
        使用sc.parallelize,你可以把Python list,NumPy array或者Pandas Series,Pandas DataFrame转成Spark RDD
        ```
        import pyspark
        from pyspark import SparkContext
        from pyspark import SparkConf
        conf=SparkConf().setAppName("miniProject").setMaster("local[*]")
        sc=SparkContext.getOrCreate(conf)
        # 在内存中初始化一个RDD
        rdd = sc.parallelize([1,2,3,4,5], 3) 
        rdd.getNumPartitions() # 查看有多少分区
        rdd.glom().collect() # 查看分区情况
        ```
    
    2. 初始化Rdd法2(从文件读取)
        ```
        rdd = sc.textFile("file:///root/data/text1.txt") # 从本地读取
        rdd = sc.textFile('/sxy-new/462906/xxx.json') # 从hdfs读取
        rdd.take(20)
        rdd.count
        ```
    3. 初始化Rdd(从SparkSql)
        1. 反射推断
            ```
            from pyspark.sql import Row

            sc = spark.sparkContext
            lines = sc.textFile("data/people.txt")
            parts = lines.map(lambda l: l.split(","))
            people = parts.map(lambda p: Row(name=p[0], age=int(p[1])))

            # Infer the schema, and register the DataFrame as a table.
            schemaPeople = spark.createDataFrame(people)
            schemaPeople.createOrReplaceTempView("people")

            teenagers = spark.sql("SELECT name FROM people WHERE age >= 13 AND age <= 19")
            ```
        2. 以编程方式制定schema
            ```
            from pyspark.sql.types import *

            sc = spark.sparkContext

            # Load a text file and convert each line to a Row.
            lines = sc.textFile("data/people.txt")
            parts = lines.map(lambda l: l.split(","))
            # Each line is converted to a tuple.
            people = parts.map(lambda p: (p[0], p[1].strip()))

            # The schema is encoded in a string.
            schemaString = "name age"

            fields = [StructField(field_name, StringType(), True) for field_name in schemaString.split()]
            schema = StructType(fields)

            # Apply the schema to the RDD.
            schemaPeople = spark.createDataFrame(people, schema)

            schemaPeople.createOrReplaceTempView("people")
        results = spark.sql("SELECT name FROM people")
        results.show()
            ```
    

    4. 常用transformation
        ```
        numbersRDD = sc.parallelize(range(1,10+1))
        print(numbersRDD.collect())

        # map
        squaresRDD = numbersRDD.map(lambda x: x**2)  # Square every number
        print(squaresRDD.collect())

        # filter
        filteredRDD = numbersRDD.filter(lambda x: x % 2 == 0)  # Only the evens
        print(filteredRDD.collect())

        # flatMap
        sentencesRDD = sc.parallelize(['Hello world', 'My name is Patrick', 'jI sDEW'])
        wordsRDD = sentencesRDD.flatMap(lambda sentence: sentence.split(" "))
        print(wordsRDD.collect()) # ['Hello', 'world', 'My', 'name', 'is', 'Patrick', 'jI', 'sDEW']

        # distinct 去重
        ```
    5. Rdd间的操作
        rdd1.union(rdd2): 所有rdd1和rdd2中的item组合
        rdd1.intersection(rdd2): rdd1 和 rdd2的交集
        rdd1.substract(rdd2): 所有在rdd1中但不在rdd2中的item(差集)
        rdd1.cartesian(rdd2): rdd1 和 rdd2中所有的元素笛卡尔乘积 *
    
    6. 常见的Action(出现时表明要执行定义的transform了)
        collect(): 计算所有的items并返回所有的结果到driver端，接着 collect()会以Python list的形式返回结果
        first(): 和上面是类似的，不过只返回第1个item
        take(n): 类似，但是返回n个item
        count(): 计算RDD中item的个数
        top(n): 返回头n个items，按照自然结果排序
        reduce(): 对RDD中的items做聚合
        saveAsTextFile()：方法接收一个路径，并将RDD 中的内容都输入到路径对应的文件中。
        foreach(): 做定制化的想做的操作
    
    7. 更加复杂的transform和action(处理键值对类型的数据)
        reduceByKey(): 对所有有着相同key的items执行reduce操作
        groupByKey(): 返回类似(key, listOfValues)元组的RDD，后面的value List 是同一个key下面的
        sortByKey(): 按照key排序
        countByKey(): 按照key去对item个数进行统计
        collectAsMap(): 和collect有些类似，但是返回的是k-v的字典
        ```
        rdd = sc.parallelize(["Hello hello", "Hello New York", "York says hello"])
        res_1 = (
            rdd
            .flatMap(lambda x:x.split(" "))
            .map(lambda x:x.lower())
            .map(lambda x: (x,1))
            .reduceByKey(lambda x,y:x+y)
        )
        res_1.collect()
        ```
- SparkSql
    1. 构建SparkSession
        ```
        from pyspark.sql import SparkSession

        spark = SparkSession \
            .builder \
            .appName("Python Spark SQL") \
            .config("spark.some.config.option", "some-value") \
            .getOrCreate()
        ```
    2. 创建DataFrames
        ```
        df = spark.read.json("file:////root/data/people.json")
        df.show()
        ```

    3. 创建临时表
        ```
        df.createOrReplaceTempView("people")
        ```
    4. 查看DataFrame信息
        ```
        df.show()
        ```
    5. 执行SQL请求(写法1)
        ```
        spark.sql("select * from people").collect()
        df.printSchema() # 查看表格式
        spark.sql("select count(1) from swimmersJSON")
        ```
    6. 执行SQL请求(写法2)
        ```
        df.select("id", "age").filter("age = 22").show()
        df.select("name", "eyeColor").filter("eyeColor like 'b%'").show()
        ```