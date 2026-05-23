import unittest
from utils import calculate_average, get_user_name


class TestCalculateAverage(unittest.TestCase):
    """Unit tests for the calculate_average function."""

    def test_average_of_positive_integers(self):
        """Test calculating average of positive integers."""
        result = calculate_average([10, 20, 30])
        self.assertEqual(result, 20.0)

    def test_average_of_floats(self):
        """Test calculating average of float numbers."""
        result = calculate_average([1.5, 2.5, 3.5])
        self.assertAlmostEqual(result, 2.5)

    def test_average_of_mixed_numbers(self):
        """Test calculating average of mixed int and float."""
        result = calculate_average([10, 20.5, 30])
        self.assertAlmostEqual(result, 20.166666666)

    def test_average_of_single_number(self):
        """Test calculating average of a single number."""
        result = calculate_average([42])
        self.assertEqual(result, 42.0)

    def test_average_of_negative_numbers(self):
        """Test calculating average of negative numbers."""
        result = calculate_average([-10, -20, -30])
        self.assertEqual(result, -20.0)

    def test_average_of_mixed_positive_and_negative(self):
        """Test calculating average of mixed positive and negative."""
        result = calculate_average([-10, 0, 10])
        self.assertEqual(result, 0.0)

    def test_average_of_empty_list(self):
        """Test calculating average of an empty list returns 0."""
        result = calculate_average([])
        self.assertEqual(result, 0)

    def test_average_with_zeros(self):
        """Test calculating average with zeros in the list."""
        result = calculate_average([0, 0, 0])
        self.assertEqual(result, 0.0)

    def test_average_with_large_numbers(self):
        """Test calculating average with large numbers."""
        result = calculate_average([1000000, 2000000, 3000000])
        self.assertEqual(result, 2000000.0)


class TestGetUserName(unittest.TestCase):
    """Unit tests for the get_user_name function."""

    def test_get_user_name_lowercase(self):
        """Test extracting and converting lowercase name to uppercase."""
        user = {"name": "john doe"}
        result = get_user_name(user)
        self.assertEqual(result, "JOHN DOE")

    def test_get_user_name_mixed_case(self):
        """Test extracting and converting mixed case name to uppercase."""
        user = {"name": "Jane Smith"}
        result = get_user_name(user)
        self.assertEqual(result, "JANE SMITH")

    def test_get_user_name_already_uppercase(self):
        """Test extracting name that is already uppercase."""
        user = {"name": "ALICE WONDERLAND"}
        result = get_user_name(user)
        self.assertEqual(result, "ALICE WONDERLAND")

    def test_get_user_name_with_special_characters(self):
        """Test extracting name with special characters."""
        user = {"name": "o'brien"}
        result = get_user_name(user)
        self.assertEqual(result, "O'BRIEN")

    def test_get_user_name_with_spaces(self):
        """Test extracting name with multiple spaces."""
        user = {"name": "jean claude van damme"}
        result = get_user_name(user)
        self.assertEqual(result, "JEAN CLAUDE VAN DAMME")

    def test_get_user_name_single_character(self):
        """Test extracting single character name."""
        user = {"name": "a"}
        result = get_user_name(user)
        self.assertEqual(result, "A")

    def test_get_user_name_with_empty_string(self):
        """Test extracting name when name field is empty string."""
        user = {"name": ""}
        result = get_user_name(user)
        self.assertEqual(result, "")

    def test_get_user_name_with_none_user(self):
        """Test with None user object."""
        result = get_user_name(None)
        self.assertEqual(result, "")

    def test_get_user_name_missing_name_field(self):
        """Test with user dict missing 'name' key."""
        user = {"email": "test@example.com"}
        result = get_user_name(user)
        self.assertEqual(result, "")

    def test_get_user_name_with_empty_dict(self):
        """Test with empty user dictionary."""
        user = {}
        result = get_user_name(user)
        self.assertEqual(result, "")

    def test_get_user_name_with_none_name_value(self):
        """Test with user dict where name value is None."""
        user = {"name": None}
        result = get_user_name(user)
        self.assertEqual(result, "")

    def test_get_user_name_with_whitespace_only(self):
        """Test with name containing only whitespace."""
        user = {"name": "   "}
        result = get_user_name(user)
        self.assertEqual(result, "   ")

    def test_get_user_name_with_numbers(self):
        """Test with name containing numbers."""
        user = {"name": "john 123 doe"}
        result = get_user_name(user)
        self.assertEqual(result, "JOHN 123 DOE")


if __name__ == "__main__":
    unittest.main()
