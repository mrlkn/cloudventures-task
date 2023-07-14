# Abstract Factory Pattern Implementation for Cloudventures Task

This project provides an implementation of the Abstract Factory pattern for creating Data Access Objects (DAOs).

## Overview

- **BaseDAO**: An abstract base class that defines the interface for all DAOs. It includes a single abstract method `get_number()` that takes a configuration dictionary and returns an integer or float.
- **BigQueryDAO**, **MongoDBDAO**, **MySQLDAO**: These classes extend `BaseDAO`, providing concrete implementations for BigQuery, MongoDB, and MySQL databases respectively. The `get_number()` method in these classes returns dummy values for demonstration purposes.
- **AbstractFactory**: A class that maintains a registry of DAO classes. The registry associates string identifiers with DAO classes. The `register()` method allows new DAOs to be registered, and the `get_dao()` method returns an instance of a DAO based on the provided identifier.

## Usage

```python
AbstractFactory.register("bigquery", BigQueryDAO)
AbstractFactory.register("mongodb", MongoDBDAO)
AbstractFactory.register("mysql", MySQLDAO)

query_runner_name = "bigquery"
query_options = {
    "sql_statemant": "select count(*) as the_number from `orders`",
    "return_value": "the_number"
}

query_runner = AbstractFactory.get_dao(query_runner_name)
result = query_runner.get_number(query_options)
```

## Expanding the factory

```python
class NewDBDAO(BaseDAO):
    def get_number(self, configuration: Dict) -> int:
        # provide concrete implementation here
        pass

# Register the new DAO with the factory
AbstractFactory.register("new_db", NewDBDAO)
```
