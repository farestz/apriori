import apriori
import unittest


class TestApriori(unittest.TestCase):
    def test_few_digits(self):
        data = ['11,22, 44, 55', '22, 44,55', '44,55', '11, 22, 33']
        result = {'11, 22': 2, '22, 44': 2, '44, 55': 3, '22, 44, 55': 2}
        primitives = {'11', '22', '33', '44', '55'}
        patterns = apriori.Apriori(data)
        self.assertEqual(patterns.primitives, primitives)
        self.assertEqual(patterns, result)

    def test_one_digits(self):
        data = ['1,2, 4, 5', '2, 4,5', '4,5', '1, 2, 3']
        result = {'1, 2': 2, '2, 4': 2, '4, 5': 3, '2, 4, 5': 2}
        primitives = set('12345')
        patterns = apriori.Apriori(data)
        self.assertEqual(patterns.primitives, primitives)
        self.assertEqual(patterns, result)


if __name__ == '__main__':
    unittest.main()
