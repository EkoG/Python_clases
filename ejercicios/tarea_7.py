import unittest

# Función a probar
def remove_duplicates(input_list):
    # Agregar codigo aquí
    pass
    

class TestRemoveDuplicates(unittest.TestCase):

    def test_remove_duplicates_with_duplicates(self):
        input_list = [1, 2, 2, 3, 4, 4, 5]
        expected_output = [1, 2, 3, 4, 5]
        result = remove_duplicates(input_list)
        self.assertCountEqual(result, expected_output)

    def test_remove_duplicates_without_duplicates(self):
        input_list = [1, 2, 3, 4, 5]
        expected_output = [1, 2, 3, 4, 5]
        result = remove_duplicates(input_list)
        self.assertCountEqual(result, expected_output)

    def test_remove_duplicates_empty_list(self):
        input_list = []
        expected_output = []
        result = remove_duplicates(input_list)
        self.assertEqual(result, expected_output)

    def test_remove_duplicates_single_element(self):
        input_list = [1]
        expected_output = [1]
        result = remove_duplicates(input_list)
        self.assertEqual(result, expected_output)

    def test_remove_duplicates_all_duplicates(self):
        input_list = [1, 1, 1, 1]
        expected_output = [1]
        result = remove_duplicates(input_list)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()