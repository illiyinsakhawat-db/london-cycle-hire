def test_spark_works(spark):
    df = spark.createDataFrame([(1, "a"), (2, "b")], ["id", "letter"])
    assert df.count() == 2