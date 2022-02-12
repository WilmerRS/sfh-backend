from smaller_addition_code import smaller_addition

def test_1():
    input = [1,2,3,3,3,3,4,5,6,6]
    resultado = smaller_addition([1,2,3,3,3,3,4,5,6,6])
    print(f'\nInput: {input}')
    print(f'Output: {resultado}')

def test_2():
    input = [0,7,1,-10,2,-4,-1,3,-2,10,-2,-6,-9,9, 1,10,3,-2,0,9,6,-5,10,-10,-2,-5,-5,7,-6,-10,2, 2,-5,-3,8,0,3,4,-2,-9,-8,-1,-5,-9,-3,-10,7,-3,-9,4,0,1,0,-9,-8,6,-5,1,-6,-1,0,9,-10,-9,-4,5,5,5,-1, -9,1,-7,-5,-4,0,7,-7,0,6,7,8,-2,0,-6,-6,-2,2,5,0,-4,6,-6,10,-8,-5,-5,7,0,7,-9]
    resultado = smaller_addition([0,7,1,-10,2,-4,-1,3,-2,10,-2,-6,-9,9,1,10,3,-2,0,9,6,-5,10,-10,-2,-5,-5,7,-6,-10,2,2,-5,-3,8,0,3,4,-2,-9,-8,-1,-5,-9,-3,-10,7,-3,-9,4,0,1,0,-9,-8,6,-5,1,-6,-1,0,9,-10,-9,-4,5,5,5,-1,-9,1,-7,-5,-4,0,7,-7,0,6,7,8,-2,0,-6,-6,-2,2,5,0,-4,6,-6,10,-8,-5,-5,7,0,7,-9])
    print(f'\nInput: {input}')
    print(f'Output: {resultado}')


def test_3():
    input = [0,7,1,-10,2,-4,-1,3,-2,10,-2,-6,-9,9, 1,10,3,-2,0,9,6,-5,10,-10,-2,-5,-5,7,-6,-10,2, 2,-5,-3,8,0,3,4,-2,-9,-8,-1,-5,-9,-3,-10,7,-3,-9,4,0,1,0,-9,-8,6,-5,1,-6,-1,0,9,-10,-9,-4,5,5,5,-1, -9,1,-7,-5,-4,0,7,-7,0,6,7,8,-2,0,-6,-6,-2,2,5,0,-4,6,-6,10,-8,-5,-5,7,0,7,-9]
    resultado = smaller_addition([4,10,0,-2,10,-3,-9,0,6,10,6,10,-5,10,7,-10,-9,1,-2,-8,-10,9,-4,-9,5,1,-4,-10,2,-8,1,10,9,-1,0,4,9,7,9,7,-1,5,3,0,2,-7,4,0,7,0,-5,-6,-1,0,4,10,-2,-6,0,9,5,-5,-10,0,-7,-3,-6,5,7,-4,0,4,5,9,-4,4,1,10,1,-4,4,-4,9,-10,-10,-5,9,-3,4,0,3,-4,-1,2,-1,-5,10,7,-2,-4])
    print(f'\nInput: {input}')
    print(f'Output: {resultado}')


test_1()
test_2()
test_3()