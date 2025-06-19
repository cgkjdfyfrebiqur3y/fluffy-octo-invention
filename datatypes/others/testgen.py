import inspect
import ast
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Type, Union
import unittest
import random
import string
import datetime
from decimal import Decimal

class TestGenerator:
    """Generate unit tests for Python modules."""
    
    def __init__(self, root_path: Union[str, Path]):
        self.root_path = Path(root_path)
        
    def generate_test_file(self, module_path: Union[str, Path]) -> str:
        """Generate test file content for a module."""
        module_path = Path(module_path)
        with open(module_path, 'r') as f:
            module_content = f.read()
            
        module = ast.parse(module_content)
        
        test_lines = [
            "import unittest",
            f"from {module_path.stem} import *",
            "from typing import Any, Dict, List, Optional, Union",
            "from decimal import Decimal",
            "import datetime",
            "",
            f"class Test{module_path.stem.title()}(unittest.TestCase):",
            "    \"\"\"Test cases for {module_path.stem} module.\"\"\"",
            "",
            "    def setUp(self):",
            "        \"\"\"Set up test fixtures.\"\"\"",
            "        pass",
            ""
        ]
        
        for node in module.body:
            if isinstance(node, ast.ClassDef):
                test_lines.extend(self._generate_class_tests(node))
            elif isinstance(node, ast.FunctionDef):
                test_lines.extend(self._generate_function_tests(node))
                
        test_lines.extend([
            "",
            "if __name__ == '__main__':",
            "    unittest.main()"
        ])
        
        return '\n'.join(test_lines)
    
    def _generate_class_tests(self, node: ast.ClassDef) -> List[str]:
        """Generate test methods for a class."""
        lines = []
        
        # Test class instantiation
        lines.extend([
            f"    def test_{node.name.lower()}_instantiation(self):",
            f"        \"\"\"Test {node.name} instantiation.\"\"\"",
            f"        instance = {node.name}()",
            f"        self.assertIsInstance(instance, {node.name})",
            ""
        ])
        
        # Test methods
        for item in node.body:
            if isinstance(item, ast.FunctionDef):
                if not item.name.startswith('_'):
                    lines.extend(self._generate_method_tests(node.name, item))
                    
        return lines
    
    def _generate_method_tests(self, class_name: str, node: ast.FunctionDef) -> List[str]:
        """Generate test methods for a class method."""
        lines = []
        
        params = []
        for arg in node.args.args:
            if arg.arg != 'self':
                params.append(self._generate_test_value(arg))
                
        param_str = ', '.join(params)
        
        lines.extend([
            f"    def test_{class_name.lower()}_{node.name}(self):",
            f"        \"\"\"Test {class_name}.{node.name} method.\"\"\"",
            f"        instance = {class_name}()",
            f"        result = instance.{node.name}({param_str})",
            "        # Add assertions based on expected behavior",
            ""
        ])
        
        return lines
    
    def _generate_function_tests(self, node: ast.FunctionDef) -> List[str]:
        """Generate test methods for a function."""
        lines = []
        
        params = [self._generate_test_value(arg) for arg in node.args.args]
        param_str = ', '.join(params)
        
        lines.extend([
            f"    def test_{node.name}(self):",
            f"        \"\"\"Test {node.name} function.\"\"\"",
            f"        result = {node.name}({param_str})",
            "        # Add assertions based on expected behavior",
            ""
        ])
        
        return lines
    
    def _generate_test_value(self, arg: ast.arg) -> str:
        """Generate test value based on parameter type annotation."""
        if arg.annotation:
            if isinstance(arg.annotation, ast.Name):
                return self._get_default_value(arg.annotation.id)
            elif isinstance(arg.annotation, ast.Subscript):
                return self._get_default_container_value(arg.annotation)
        return "None"
    
    def _get_default_value(self, type_name: str) -> str:
        """Get default test value for a type."""
        defaults = {
            'str': '"test"',
            'int': '42',
            'float': '3.14',
            'bool': 'True',
            'bytes': 'b"test"',
            'Decimal': 'Decimal("1.23")',
            'datetime': 'datetime.datetime.now()',
            'date': 'datetime.date.today()',
        }
        return defaults.get(type_name, 'None')
    
    def _get_default_container_value(self, node: ast.Subscript) -> str:
        """Get default test value for container types."""
        if isinstance(node.value, ast.Name):
            base = node.value.id
            if base == 'List':
                return '[]'
            elif base == 'Dict':
                return '{}'
            elif base == 'Set':
                return 'set()'
            elif base == 'Optional':
                return 'None'
            elif base == 'Union':
                return self._get_default_value('str')
        return 'None'
    
    def generate_project_tests(self) -> None:
        """Generate test files for all modules in the project."""
        for py_file in self.root_path.rglob('*.py'):
            if not any(part.startswith('_') for part in py_file.parts):
                try:
                    test_content = self.generate_test_file(py_file)
                    test_path = py_file.parent / f"test_{py_file.name}"
                    test_path.write_text(test_content)
                except Exception as e:
                    print(f"Error generating tests for {py_file}: {str(e)}")

class DataGenerator:
    """Generate test data for different types."""
    
    @staticmethod
    def random_string(length: int = 10) -> str:
        """Generate random string."""
        return ''.join(random.choices(string.ascii_letters, k=length))
    
    @staticmethod
    def random_int(min_val: int = -1000, max_val: int = 1000) -> int:
        """Generate random integer."""
        return random.randint(min_val, max_val)
    
    @staticmethod
    def random_float(min_val: float = -1000.0, max_val: float = 1000.0) -> float:
        """Generate random float."""
        return random.uniform(min_val, max_val)
    
    @staticmethod
    def random_decimal(min_val: float = -1000.0, max_val: float = 1000.0) -> Decimal:
        """Generate random Decimal."""
        return Decimal(str(random.uniform(min_val, max_val)))
    
    @staticmethod
    def random_datetime(
        start: datetime.datetime = datetime.datetime(2000, 1, 1),
        end: datetime.datetime = datetime.datetime(2030, 12, 31)
    ) -> datetime.datetime:
        """Generate random datetime."""
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = random.randrange(int_delta)
        return start + datetime.timedelta(seconds=random_second)
    
    @staticmethod
    def random_bytes(length: int = 10) -> bytes:
        """Generate random bytes."""
        return bytes(random.getrandbits(8) for _ in range(length))
    
    @staticmethod
    def random_list(
        length: int = 5,
        value_type: Type = str,
        **kwargs: Any
    ) -> List[Any]:
        """Generate random list."""
        generators = {
            str: DataGenerator.random_string,
            int: DataGenerator.random_int,
            float: DataGenerator.random_float,
            Decimal: DataGenerator.random_decimal,
            datetime.datetime: DataGenerator.random_datetime,
            bytes: DataGenerator.random_bytes
        }
        generator = generators.get(value_type, DataGenerator.random_string)
        return [generator(**kwargs) for _ in range(length)]
    
    @staticmethod
    def random_dict(
        length: int = 5,
        key_type: Type = str,
        value_type: Type = str,
        **kwargs: Any
    ) -> Dict[Any, Any]:
        """Generate random dictionary."""
        keys = DataGenerator.random_list(length, key_type, **kwargs)
        values = DataGenerator.random_list(length, value_type, **kwargs)
        return dict(zip(keys, values))
