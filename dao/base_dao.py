from typing import Dict, Union
import abc


class BaseDAO(abc.ABC):
    """
    The abstract base class for all Data Access Objects (DAOs).

    Dummy implementation of BaseDOA
    """

    @abc.abstractmethod
    def get_number(self, configuration: Dict) -> int:
        """
        Dummy db query

        Args:
            configuration (Dict): The configuration for the query.

        Returns:
            Union[int, float]: The number obtained from the query. The specific type
            (int or float) may depend on the implementation.

        Note: This method is abstract and must be implemented by subclasses.
        """
        pass
