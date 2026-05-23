# utils.py Documentation

This module provides utility functions for common operations including mathematical calculations and user data manipulation.

## Functions

### `calculate_average(numbers: List[Union[int, float]]) -> float`

Calculate the average (mean) of a list of numbers.

Computes the arithmetic mean of all numbers in the provided list. If the list is empty, returns 0.

#### Parameters

- **numbers** (`List[Union[int, float]]`): A list of numeric values (integers or floats).

#### Returns

- **float**: The average of the numbers. Returns 0 if the list is empty.

#### Examples

```python
>>> calculate_average([10, 20, 30])
20.0

>>> calculate_average([])
0

>>> calculate_average([5.5, 10.5, 15.0])
10.333333...
```

#### Behavior

- Handles both integer and floating-point numbers
- Returns 0 for empty lists (no exception raised)
- Uses simple arithmetic to compute the mean

---

### `get_user_name(user: Optional[Dict[str, Any]]) -> str`

Extract and format the user's name from a user dictionary.

Retrieves the 'name' field from a user dictionary and returns it in uppercase. Returns an empty string if the user object is None or if the name field is missing or empty.

#### Parameters

- **user** (`Optional[Dict[str, Any]]`): A dictionary containing user information with a 'name' key. Can be None.

#### Returns

- **str**: The user's name in uppercase, or an empty string if the user is None or the name is missing/empty.

#### Examples

```python
>>> get_user_name({"name": "john doe"})
'JOHN DOE'

>>> get_user_name({"name": ""})
''

>>> get_user_name(None)
''

>>> get_user_name({"age": 30})  # name field missing
''
```

#### Behavior

- Converts the name to uppercase using `.upper()`
- Handles None user objects gracefully
- Handles missing 'name' keys in the user dictionary
- Handles empty strings by returning an empty string
- Safe for use with incomplete user data structures

---

## Type Hints

Both functions use Python type hints for better code clarity and IDE support:

- `List`: List type from the `typing` module
- `Union`: Allows multiple types (e.g., int or float)
- `Optional`: Indicates a value can be None
- `Dict`: Dictionary type with string keys and any value type
- `Any`: Any type from the `typing` module

## Import

To use these functions, import them from the utils module:

```python
from utils import calculate_average, get_user_name
```

Or import individual functions as needed:

```python
from utils import calculate_average
```
