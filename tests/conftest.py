import os
import sys
import pytest
from pyspark.sql import SparkSession


os.environ.setdefault("PYSPARK_PYTHON", sys.executable)
os.environ.setdefault("PYSPARK_DRIVER_PYTHON", sys.executable)


@pytest.fixture(scope="session")
def spark():
    session = (
        SparkSession.builder.master("local[*]")
        .appName("pytest-pyspark-local-testing")
        .config("spark.sql.shuffle.partitions", "1")
        .config("spark.ui.enabled", "false")
        .config("spark.sql.session.timeZone", "Europe/London")
        .getOrCreate()
    )
    yield session
    session.stop()