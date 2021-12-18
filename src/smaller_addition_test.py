from smaller_addition_code import smaller_addition
import unittest

class SmallerAdditionTest(unittest.TestCase):
    def test_1(self):
        input = [1,2,3,3,3,3,4,5,6,6]
        resultado = smaller_addition([1,2,3,3,3,3,4,5,6,6])
        print(f'\ninput: {input}')
        print(f'output: {resultado}')
        self.assertEqual(resultado, 6)

    def test_2(self):
        input = [0,7,1,-10,2,-4,-1,3,-2,10,-2,-6,-9,9, 1,10,3,-2,0,9,6,-5,10,-10,-2,-5,-5,7,-6,-10,2, 2,-5,-3,8,0,3,4,-2,-9,-8,-1,-5,-9,-3,-10,7,-3,-9,4,0,1,0,-9,-8,6,-5,1,-6,-1,0,9,-10,-9,-4,5,5,5,-1, -9,1,-7,-5,-4,0,7,-7,0,6,7,8,-2,0,-6,-6,-2,2,5,0,-4,6,-6,10,-8,-5,-5,7,0,7,-9]
        resultado = smaller_addition([0,7,1,-10,2,-4,-1,3,-2,10,-2,-6,-9,9, 1,10,3,-2,0,9,6,-5,10,-10,-2,-5,-5,7,-6,-10,2, 2,-5,-3,8,0,3,4,-2,-9,-8,-1,-5,-9,-3,-10,7,-3,-9,4,0,1,0,-9,-8,6,-5,1,-6,-1,0,9,-10,-9,-4,5,5,5,-1, -9,1,-7,-5,-4,0,7,-7,0,6,7,8,-2,0,-6,-6,-2,2,5,0,-4,6,-6,10,-8,-5,-5,7,0,7,-9])
        print(f'\ninput: {input}')
        print(f'output: {resultado}')
        self.assertEqual(resultado, 7)

if __name__ == '__main__':
    print("Running tests...")
    unittest.main()