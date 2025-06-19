"""A pickler for the Data Types."""
import pickle
import ast
from typing import Any

class BaseDataTypesPickler:
    """Serializes data into a pickled representation string."""
    
    def __init__(self, value: Any) -> None:
        """Initialize pickler with a value to serialize.
        
        Args:
            value: The value to pickle. Can be any serializable Python object.
        """
        self.unpickled_value = value

    def __pickle(self, data: Any) -> bytes:
        """Internal method to pickle data safely.
        
        Args:
            data: The data to pickle.
            
        Returns:
            bytes: The pickled representation.
        """
        representation = repr(data)
        return pickle.dumps(representation)

    def get_pickled_value(self) -> bytes:
        """Get the pickled representation of the stored value.
        
        Returns:
            bytes: The pickled representation.
        """
        return BaseDataTypesPickler.__pickle(self,self.unpickled_value)
    

class BaseDataTypesUnpickler:
    """Deserializes data from a pickled representation string."""
    
    def __init__(self, value: bytes) -> None:
        """Initialize unpickler with pickled data.
        
        Args:
            value: The pickled data to deserialize.
        """
        self.pickled_value = value

    def __unpickle(self, data: bytes) -> Any:
        """Internal method to safely unpickle data.
        
        Args:
            data: The pickled data to deserialize.
            
        Returns:
            Any: The unpickled value.
        """
        try:
            # First unpickle the repr string
            repr_str = pickle.loads(data)
            # Then safely evaluate the repr string
            return ast.literal_eval(repr_str)
        except (pickle.UnpicklingError, ValueError, SyntaxError) as e:
            raise ValueError(f"Failed to unpickle data: {str(e)}")

    def get_unpickled_value(self) -> Any:
        """Get the unpickled value.
        
        Returns:
            Any: The deserialized value.
            
        Raises:
            ValueError: If the data cannot be safely unpickled.
        """
        return self.__unpickle(self.pickled_value)

