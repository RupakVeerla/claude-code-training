from typing import List, Union, Optional, Dict, Any


def calculate_average(numbers: List[Union[int, float]]) -> float:
    """Calculate the average (mean) of a list of numbers.

    Computes the arithmetic mean of all numbers in the provided list.
    If the list is empty, returns 0.

    Args:
        numbers (list): A list of numeric values (int or float).

    Returns:
        float: The average of the numbers. Returns 0 if the list is empty.

    Examples:
        >>> calculate_average([10, 20, 30])
        20.0
        >>> calculate_average([])
        0
    """
    if not numbers:
        return 0
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)


def get_user_name(user: Optional[Dict[str, Any]]) -> str:
    """Extract and format the user's name from a user dictionary.

    Retrieves the 'name' field from a user dictionary and returns it in
    uppercase. Returns an empty string if the user object is None or if
    the name field is missing or empty.

    Args:
        user (dict): A dictionary containing user information with a 'name' key.
                     Can be None.

    Returns:
        str: The user's name in uppercase, or an empty string if the user
             is None or the name is missing/empty.

    Examples:
        >>> get_user_name({"name": "john doe"})
        'JOHN DOE'
        >>> get_user_name({"name": ""})
        ''
        >>> get_user_name(None)
        ''
    """
    if not user:
        return ""
    name = user.get("name")
    if not name:
        return ""
    return name.upper()