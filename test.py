import apriori
import unittest


class AprioriTestCase(unittest.TestCase):
    def test_priimitives(self):
        primitives = set('12345')
        data = ['1,2, 4, 5', '2, 4,5', '4,5', '1, 2, 3']
        patterns = apriori.Apriori(data)
        self.assertEqual(primitives, patterns.primitives)

    def test_one_digits(self):
        data = ['1,2, 4, 5', '2, 4,5', '4,5', '1, 2, 3']
        result = {'1, 2': 2, '2, 4': 2, '4, 5': 3, '2, 4, 5': 2}
        patterns = apriori.Apriori(data)
        self.assertEqual(result, patterns)

    def test_few_digits(self):
        data = ['11,22, 44, 55', '22, 44,55', '44,55', '11, 22, 33']
        result = {'11, 22': 2, '22, 44': 2, '44, 55': 3, '22, 44, 55': 2}
        patterns = apriori.Apriori(data)
        self.assertEqual(result, patterns)


if __name__ == '__main__':
    unittest.main()
