import unittest
import copy

from diff import Diff
 
class BaseTestClass(unittest.TestCase):
    def test_TC1(self):
        '''
        Text example
        '''
        data = {'a' : {'a1' : 1, 'a2' : 2}, 'b' : {'b1': {'b11' : 1, 'b12' : 2}}}

        data_before = copy.deepcopy(data)

        data['a']['a1'] = 3
        data['b']['b1']['b11'] = 5
       
        try_result = {'a' : {'a1' : 3}, 'b' : {'b1': {'b11' : 5}}}
        result = Diff().diff_two_dict(data_before, data, {})

        self.assertEqual(try_result, result)
 
    def test_TC2(self):
        data = {'a': 1, 'b': 2}
        data_before = copy.deepcopy(data)

        data['b'] = 7

        try_result = {'b': 7}

        result = Diff().diff_two_dict(data_before, data, {})

        self.assertEqual(try_result, result)

    def test_TC3(self):
        data = {'a': 1, 'b': 2, 'c': {'c1': 3, 'c2': 5}}
        data_before = copy.deepcopy(data)

        data['a'] = 5
        data['c']['c2'] = 9

        try_result = {'a': 5, 'c': {'c2': 9}}

        result = Diff().diff_two_dict(data_before, data, {})

        self.assertEqual(try_result, result)

    def test_TC4(self):
        data = {'a' : 1, 'b' : {'b1': 2}, 'c': {'c1': {'c2': 3, 'c3': 5}}}
        data_before = copy.deepcopy(data)

        data['c']['c1']['c4'] = {'c5': 3}
        
        try_result = {'c': {'c1': {'c4': {'c5': 3}}}}

        result = Diff().diff_two_dict(data_before, data, {})

        self.assertEqual(try_result, result)

    def test_TC5(self):
        data = {'a' : {'a1' : 1, 'a2' : 2}, 'b' : {'b1': {'b11' : 1, 'b12' : 2}}, 'c': {'d': 4}}
        data_before = copy.deepcopy(data)

        data['a']['a2'] = 7
        del(data['b'])
        
        try_result = {'a': {'a2': 7}, 'b' : {'b1': {'b11' : 1, 'b12' : 2}}}
        result = Diff().diff_two_dict(data_before, data, {})

        self.assertEqual(try_result, result)

    def test_TC6(self):
        data = {'a' : {'a1': 1, 'a2': 3}, 'b': {'b1': 5, 'b2': {'b3': {'b4': 5}}}}
        data_before = copy.deepcopy(data)

        data['a']['a2'] = 7
        del(data['b']['b2'])
        
        try_result = {'a': {'a2': 7}, 'b' : {'b2': {'b3': {'b4': 5}}}}
        result = Diff().diff_two_dict(data_before, data, {})

        self.assertEqual(try_result, result)

    def test_TC7(self):
        data = {'a' : 1, 'b' : {'b1': 2}, 'c': {'c1': {'c2': 3, 'c3': 5}}}
        data_before = copy.deepcopy(data)

        data['d'] = {'d1': 3}
        del(data['c']['c1']['c2'])
        
        try_result = {'c': {'c1': {'c2': 3}}, 'd': {'d1': 3}}

        result = Diff().diff_two_dict(data_before, data, {})

        self.assertEqual(try_result, result)

    def test_TC8(self):
        data = {'a' : 1, 'b' : {'b1': 2}, 'c': {'c1': {'c2': 3, 'c3': {'c4': {'c5': {'c6': 6}}}}}}
        data_before = copy.deepcopy(data)

        data['c']['c1']['c2'] = {'e': 3}
        del(data['c']['c1']['c3']['c4']['c5'])
        
        try_result = {'c': {'c1': {'c2': {'e': 3}, 'c3': {'c4': {'c5': {'c6': 6}}}}}}

        result = Diff().diff_two_dict(data_before, data, {})

        self.assertEqual(try_result, result)

    def test_TC9(self):
        data = {'a': 1, 'b': 2, 'c': {'c1': 3, 'c2': 5}}
        data_before = copy.deepcopy(data)

        del(data['b'])
        del(data['c']['c2'])

        try_result = {'b': 2, 'c': {'c2': 5}}

        result = Diff().diff_two_dict(data_before, data, {})

        self.assertEqual(try_result, result)

    def test_TC10(self):
        with self.assertRaises(TypeError):
            Diff().diff_two_dict(5, {}, {})

    def test_TC11(self):
        try_result = {}

        result = Diff().diff_two_dict({}, {}, {})

        self.assertEqual(try_result, result)

    def test_TC12(self):
        data = {'a': 1, 'b': 2}
        data_before = copy.deepcopy(data)

        try_result = {}

        result = Diff().diff_two_dict(data_before, data, {})

        self.assertEqual(try_result, result)

    def test_TC13(self):
        data = {}
        data_before = copy.deepcopy(data)

        data['a'] = {'a1': {'a2': 3}}
        
        try_result = {'a': {'a1': {'a2': 3}}}

        result = Diff().diff_two_dict(data_before, data, {})

        self.assertEqual(try_result, result)

 
if __name__ == '__main__':
    unittest.main()
