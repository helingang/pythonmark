# spark
- linux下使用pyspary运行py文件
    - ` ./bin/pyspark --master local[4] --py-files code.py`
- Spark
    1. 初始化Spark
        使用sc.parallelize,你可以把Python list,NumPy array或者Pandas Series,Pandas DataFrame转成Spark RDD
        ```
        import pyspark
        from pyspark import SparkContext
        from pyspark import SparkConf
        conf=SparkConf().setAppName("miniProject").setMaster("local[*]")
        sc=SparkContext.getOrCreate(conf)

        # conf = (SparkConf().setMaster("local").setAppName("My app").set("spark.executor.memory", "1g"))
        # sc = SparkContext(conf = conf)
        ```
    2. 读取数据
        ```
        rdd = sc.parallelize([('a',7),('a',2),('b',2)])
        rdd2 = sc.parallelize([('a',2),('d',1),('b',1)])
        rdd3 = sc.parallelize(range(100))
        rdd4 = sc.parallelize([("a",["x","y","z"]), ("b",["p", "r"])])
        textFile = sc.textFile("http://ml8.julyedu.com:8901/jxy8/jxy/run/5.Helingang/kejian/week4/spark/text*")
        textFile2 = sc.wholeTextFiles("/my/directory/")
        [textFile wholeTextFiles 的区别](https://www.cnblogs.com/jagel-95/p/9766254.html)
        ```
    3. 检索Rdd信息
        ```
        rdd.getNumPartitions() List the number of partitions(分区)
        rdd.count() Count RDD instances 3
        rdd.countByKey() # 根据key统计个数,返回字典
        rdd.countByValue()
        rdd.collectAsMap() # 返回字典,只存在唯一个key,如果key相同则后面的value覆盖前面的
        rdd3.sum()
        sc.parallelize([]).isEmpty()

        # 了解
        rdd3.max()
        rdd3.min()
        rdd3.mean()
        rdd3.stdev()
        rdd3.variance()
        rdd3.histogram(3)
        rdd3.stats()
        ```
    4. 应用方法
        ```
        rdd.map(lambda x: x+(x[1],x[0])).collect()
        # map和foreach的区别: foreach只做操作
        # rdd.foreach(g)

        rdd5 = rdd.flatMap(lambda x: x+(x[1],x[0])) # 解开成一个列表
        rdd5.collect()
        rdd4.flatMapValues(lambda x: x).collect() # 拆解value分别与key组成新的k-v
        ```
    5. 选择和展示数据
        ```
        Getting
        >>> rdd.collect()
        >>> rdd.take(2)
        >>> rdd.first()
        >>> rdd.top(2)
        Sampling
        >>> rdd3.sample(False, 0.15, 81).collect()
        Filtering
        >>> rdd.filter(lambda x: "a" in x).collect()
        >>> rdd5.distinct().collect() # 去重
        >>> rdd.keys().collect() # 获取keys的列表
        ```
    6. Reshaping Data
        ```
        Reducing
        >>> rdd.reduceByKey(lambda x,y : x+y).collect() # 相同的key,每一行的value两两操作
        from operator import add
        rdd.reduceByKey(add).collect() # 相同的key,统计count数量
        >>> rdd.reduce(lambda a, b: a + b) # 每一行两两操作

        Grouping by
        >>> rdd3.groupBy(lambda x: x % 2).mapValues(list).collect()
        >>> rdd.groupByKey().mapValues(list).collect()

        Aggregating
        >>> seqOp = (lambda x,y: (x[0]+y,x[1]+1))
        >>> combOp = (lambda x,y:(x[0]+y[0],x[1]+y[1]))
        ```
    7. sort操作
        ```
        rdd2.sortBy(lambda x: x[1]).collect() # 通过值排序
        rdd2.sortByKey().collect() # 通过key排序
        ```
    8. Repartitioning重新分区
        ```
        rdd.repartition(4) # 重新分区成4个
        rdd.coalesce(1)
        ```
    9. 保存
        ```
        rdd.saveAsTextFile("rdd.txt")
        rdd.saveAsHadoopFile("hdfs://namenodehost/parent/child",
        'org.apache.hadoop.mapred.TextOutputFormat')
        ```
    10. 停止Spark
        ```
        sc.stop()
        ```
    11. 执行文件
        ```
        spark-submit --master yarn --deploy-mode client 123.py /sxy-new/5642214/input/* /sxy-new/5642214/output/5
        ```
- SparkSession
    1. 初始化SparkSession
        ```
        from pyspark.sql import SparkSession
        spark = SparkSession.builder.appName("Python Spark SQL basic example").config("spark.some.config.option", "some-value").getOrCreate()
        ```
    2. 从Rdd中创建DataFrame
        ```
        from pyspark.sql.types import *
        Infer Schema
        >>> sc = spark.sparkContext
        >>> lines = sc.textFile("people.txt")
        >>> parts = lines.map(lambda l: l.split(","))
        >>> people = parts.map(lambda p: Row(name=p[0],age=int(p[1]
        >>> peopledf = spark.createDataFrame(people)
        Specify Schema
        >>> people = parts.map(lambda p: Row(name=p[0],age=int(p[1]
        >>> schemaString = "name age"
        >>> fields = [StructField(field_name, StringType(), True) for field_name in schemaString.split()]
        >>> schema = StructType(fields)
        >>> spark.createDataFrame(people, schema).show()
        ```
    3. *从路径文件中创建DataFrame*
        ```
        CSV
        >>> df = spark.read.csv('walmart_stock.csv', inferSchema=True, header=True)
        JSON
        >>> df = spark.read.json("customer.json")
        >>> df.show()
        >>> df2 = spark.read.load("people.json", format="json")
        Parquet files
        >>> df3 = spark.read.load("users.parquet")
        TXT files
        >>> df4 = spark.read.text("people.txt")
        ```

    4. 检查数据
        ```
        df.dtypes Return df column names and data types
        >>> df.show() Display the content of df
        >>> df.head() Return first n rows
        >>> df.first() Return first row
        >>> df.take(2) Return the first n rows
        >>> df.schema Return the schema of df
        >>> df.describe().show() Compute summary statistics >>> df.
        >>> df.count() Count the number of rows in df
        >>> df.distinct().count() Count the number of distinct rows
        >>> df.printSchema() Print the schema of df
        >>> df.explain() Print the (logical and physical) plans
        >>> df = df.dropDuplicates() # 去重
        ```
    5. Select Sql 
        ```
        from pyspark.sql import functions as F
        Select
        >>> df.select("firstName").show() Show all entries in first
        >>> df.select("firstName","lastName").show()
        >>> df.select("firstName","age",F.explode("phoneNumbers")
        .alias("contactInfo"))
        .select("contactInfo.type", "firstName", "age")
        .show()
        >>> df.select(df["firstName"],df["age"]+ 1)
        >>> df.select(df['age'] > 24).show()
        ```
    6. Select When and Like
        ```
        >>> df.select("firstName", 
        F.when(df.age > 30, 1) \ on age >30
        .otherwise(0)) \
        .show()
        >>> df[df.firstName.isin("Jane","Boris")] 
        .collect()
        ```
    7. Add column
        ```
        >>> df = df.withColumn('city',df.address.city) \
        .withColumn('postalCode',df.address.postalCode) \
        .withColumn('state',df.address.state) \
        .withColumn('streetAddress',df.address.streetAddress) \
        .withColumn('telePhoneNumber',
        explode(df.phoneNumber.number)) \
        .withColumn('telePhoneType',
        explode(df.phoneNumber.type))
        ```
    8. update column
        ```
        df = df.withColumnRenamed('telePhoneNumber', 'phoneNumber')
        ```
    9. remove column
        ```
        df = df.drop("address", "phoneNumber")
        df = df.drop(df.address).drop(df.phoneNumber)
        ```
    10. groupBy
        ```
        df.groupBy("age").count().show()
        ```
    11. filter
        ```
        df.filter(df["age"]>24).show()
        ```
    12. sort
        ```
        peopledf.sort(peopledf.age.desc()).collect()
        df.sort("age", ascending=False).collect()
        df.orderBy(["age","city"],ascending=[0,1]).collect()
        ```
    13. 填充数据
        ```
        df.na.fill(50).show()
        df.na.drop().show()
        df.na.replace(10, 20).show()
        ```
    14. 使用SQL语言
        ```
        >>> peopledf.createGlobalTempView("people")
        >>> df.createTempView("customer")
        >>> df.createOrReplaceTempView("customer")
        ```
        ```
        df5 = spark.sql("SELECT * FROM customer").show()
        >>> peopledf2 = spark.sql("SELECT * FROM global_temp.people.show()

        ```
    15. 输出
        ```
        >>> rdd1 = df.rdd
        >>> df.toJSON().first()
        >>> df.toPandas()
        ```
        ```
        >>> df.select("firstName", "city")\
        .write \
        .save("nameAndCity.parquet")
        >>> df.select("firstName", "age") \
        .write \
        .save("namesAndAges.json",format="json")
        ```


<!--     
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
        ``` -->
<!-- - SparkSession
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
        ``` -->