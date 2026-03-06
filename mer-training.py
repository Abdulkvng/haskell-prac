"""
WORK SAMPLE: RECURSIVE OBJECT FLATTENING

-------------------------------------------------------------------------------
PART 1: THE EXERCISE
-------------------------------------------------------------------------------
Learning Objective: 
Master the recursive traversal of nested data structures and key-path construction 
(Depth-First Search) for data transformation tasks.

Instructions:
Write a function `flatten_map` that takes a nested dictionary and converts it 
into a single-level dictionary. Nested keys should be joined by a dot (`.`).

Constraints:
- Assume keys are always strings.
- Values can be integers, strings, or other dictionaries.
- Handle empty dictionaries gracefully.

Input Example:
{
  "user": {
    "name": "Alex",
    "address": { "city": "San Francisco" }
  },
  "active": true
}

Expected Output:
{
  "user.name": "Alex",
  "user.address.city": "San Francisco",
  "active": true
}

-------------------------------------------------------------------------------
PART 2: (Why this is effective)
-------------------------------------------------------------------------------
This exercise helps you learn better by keeping things simple. It lets you focus 
on just one idea - recursion - by using it to flatten a map. You don't have to 
worry about building a whole program, so you can pay attention to how the function 
calls stack up and how data gets collected.

The clear rules about what goes in and what comes out let you check your work 
right away. You can see if you understand it correctly by looking at real results (printed). 
This emulates a real life situation and what you may actually do at work. The skill of turning tree-like data 
into a flat list is super useful in fintech jobs. You'll use it when you're 
working with complicated JSON files, handling data from APIs, and organizing 
analytics information.
"""

import unittest
import json

# -----------------------------------------------------------------------------
# PART 3: THE REFERENCE SOLUTION
# -----------------------------------------------------------------------------

def flatten_map(data: dict, parent_key: str = '', sep: str = '.') -> dict:
    """
    Recursively flattens a nested dictionary.
     
    Args:
        data: The dictionary to flatten.
        parent_key: The prefix for the current recursion level.
        sep: The separator used to join keys.
        
    Returns:
        A flattened dictionary with dot-notation keys.
    """
    "The code gefines the function with its inputs and documentation,"
    " then creates an empty dictionary to store the final results."
    result = {}
    # Hint: data.items() returns key-value pairs in the dictionary
    for k, v in data.items():
        # Construct the new composite key
        new_key = # ENTER CODE HERE 
        
        # isInstance hecks if the value is a dictionary
        if isinstance(v, dict):
            # Recursion step: Flatten the nested dict and merge results
            # ENTER CODE HERE
        else:
            # Hint: Base case
            #ENTER CODE HERE
            
    return result


# -----------------------------------------------------------------------------
# PART 4: VERIFICATION (TEST SUITE)
# -----------------------------------------------------------------------------
class TestFlattenMap(unittest.TestCase):

    def setUp(self):
        # This runs before every test to add a separator
        print("-" * 60)

    def test_standard_nesting(self):
        print("TEST 1: Standard Nesting")
        input_data = {
            "user": {
                "name": "Alex",
                "address": { "city": "San Francisco", "zip": 94107 }
            },
            "active": True
        }
        
        # Run Code
        actual = flatten_map(input_data)
        
        # Verify
        expected = {
            "user.name": "Alex",
            "user.address.city": "San Francisco", 
            "user.address.zip": 94107, 
            "active": True
        }
        
        # Show output
        print(f"Output: {json.dumps(actual, sort_keys=True)}")
        self.assertEqual(actual, expected)
        print("✅ RESULT: PASSED")

    def test_already_flat(self):
        print("TEST 2: Already Flat Dictionary")
        input_data = {"a": 1, "b": 2}
        
        actual = flatten_map(input_data)
        
        print(f"Output: {actual}")
        self.assertEqual(actual, {"a": 1, "b": 2})
        print("✅ RESULT: PASSED")

    def test_empty_dictionary(self):
        print("TEST 3: Empty Dictionary")
        
        actual = flatten_map({})
        
        print(f"Output: {actual}")
        self.assertEqual(actual, {})
        print("✅ RESULT: PASSED")

    def test_custom_separator(self):
        print("TEST 4: Custom Separator (underscore)")
        input_data = {"a": {"b": {"c": "deep"}}}
        
        actual = flatten_map(input_data, sep='_')
        
        print(f"Output: {actual}")
        self.assertEqual(actual, {"a_b_c": "deep"})
        print("✅ RESULT: PASSED")

if __name__ == '__main__':
    # verbosity=0 hides the default '....' so our custom prints stand out
    unittest.main(verbosity=0)


# answer
    # result = {}
    
    # for k, v in data.items():
    #     # Construct the new composite key
    #     new_key = f"{parent_key}{sep}{k}" if parent_key else k
        
    #     if isinstance(v, dict):
    #         # Recursion step: Flatten the nested dict and merge results
    #         result.update(flatten_map(v, new_key, sep=sep))
    #     else:
    #         # Base case: Value is a leaf node, assign directly
    #         result[new_key] = v
            
    # return result