import unittest

class TestFlattenMap(unittest.TestCase):

    def test_standard_nesting(self):
        """Test the standard example case."""
        input_data = {
            "user": {
                "name": "Alex",
                "address": {
                    "city": "SF",
                    "zip": 94107
                }
            },
            "active": true
        }
        expected = {
            "user.name": "Alex",
            "user.address.city": "SF",
            "user.address.zip": 94107,
            "active": True
        }
        self.assertEqual(flatten_map(input_data), expected)

    def test_already_flat(self):
        """Test a dictionary that requires no changes."""
        input_data = {"a": 1, "b": 2}
        expected = {"a": 1, "b": 2}
        self.assertEqual(flatten_map(input_data), expected)

    def test_empty_dictionary(self):
        """Test handling of an empty dictionary."""
        input_data = {}
        expected = {}
        self.assertEqual(flatten_map(input_data), expected)

    def test_nested_empty_dict(self):
        """Test that an empty nested dict is preserved as a leaf node."""
        # Note: Depending on requirements, this might be excluded or included. 
        # Here we treat it as a leaf value.
        input_data = {"a": 1, "b": {}}
        expected = {"a": 1, "b": {}}
        self.assertEqual(flatten_map(input_data), expected)
        
    def test_custom_separator(self):
        """Test that the separator can be changed."""
        input_data = {"a": {"b": 1}}
        expected = {"a_b": 1}
        self.assertEqual(flatten_map(input_data, sep='_'), expected)

# Boilerplate to run the tests
if __name__ == '__main__':
    unittest.main()