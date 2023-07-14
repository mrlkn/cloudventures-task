from typing import Dict, Union

from dao.base_dao import BaseDAO


class BigQueryDAO(BaseDAO):
    """
    A Data Access Object (DAO) class for BigQuery databases.
    """

    def get_number(self, configuration: Dict) -> int:
        """
        Dummy db query

        Args:
            configuration (Dict): The configuration for the query. In this example, it's not used.

        Returns:
            int: dummy 3
        """
        return 3
