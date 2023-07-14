from dao.bigquery_dao import BigQueryDAO
from dao.mongo_dao import MongoDBDAO
from dao.mysql_dao import MySQLDAO
from database_factory.abstract_factory import AbstractFactory

AbstractFactory.register("mongodb", MongoDBDAO)
AbstractFactory.register("mysql", MySQLDAO)
AbstractFactory.register("bigquery", BigQueryDAO)

query_runner_name = "bigquery"
query_options = {
    "sql_statemant": "select count(*) as the_number from `orders`",
    "return_value": "the_number",
}

query_runner = AbstractFactory.get_dao(query_runner_name)
result = query_runner.get_number(query_options)

assert result == 3
