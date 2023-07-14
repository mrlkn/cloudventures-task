from typing import Type, Dict

from dao.base_dao import BaseDAO


class AbstractFactory:
    """
    A factory class for creating Data Access Objects (DAOs). The factory uses a registry
    to map database types to their corresponding DAO classes.

    Attributes:
        registry (dict): A dictionary that maps database types (str) to DAO classes.
    """
    registry: Dict[str, Type[BaseDAO]] = {}

    @classmethod
    def register(cls, database_type: str, dao: Type[BaseDAO]) -> None:
        """
        Registers a DAO class for a specific database type in the registry.

        Args:
            database_type (str): The type of the database. This will be used as the key in the registry.
            dao (BaseDAO subclass): The DAO class that handles the database type. It should be a subclass of BaseDAO.
        """
        cls.registry[database_type] = dao

    @classmethod
    def get_dao(cls, database_type: str) -> BaseDAO:
        """
        Returns an instance of the DAO class for the specific database type.

        Args:
            database_type (str): The type of the database.

        Returns:
            BaseDAO: An instance of the DAO class corresponding to the database type.

        Raises:
            ValueError: If no DAO class is registered for the given database type.
        """
        dao_class = cls.registry.get(database_type)
        if not dao_class:
            raise ValueError(f"No DAO registered for {database_type}")
        return dao_class()
