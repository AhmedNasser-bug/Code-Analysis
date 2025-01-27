from setup import*

# ---------------------------------------------------------------- O(1) FUNCTIONS ---------------------------------------------------------------- #
def countNconstant(n:int) -> int:
    '''
    F(n) = 1
    '''
    return n

def countNconstant_func1(n:int) -> int:
    '''
    F(n) = 5000
    '''

    steps = 0
    for i in range(5000):
        steps += 1

    return steps

def countNconstant_func2(n:int) -> int:
    '''
    F(n) = 10^6
    '''

    steps = 0
    for i in range(10**6):
        steps += 1

    return steps

# ---------------------------------------------------------------- O(N) FUNCTIONS ---------------------------------------------------------------- #

def countN(n:int) -> int:
    '''
    F(n): n
    '''
    steps = 0
    for i in range(n):
        steps += 1

    return steps

def countN_func1(n:int)->int:
    '''
    F(n) = n + 10^6
    '''
    steps = 0
    for i in range(n):
        steps += 1

    steps += countNconstant_func2(n)

    return steps

def countN_func2(n:int) -> int:
    '''
    F(n) = 5000n 
    '''
    steps = 0
    for i in range(n):
       steps += countNconstant_func1(n)

    return steps

def countN_func3(n:int) -> int:
    '''
    F(n) = 5000n + 10^6
    '''
    steps = 0
    for i in range(n):
        steps += countNconstant_func1(n)

    steps += countNconstant_func2(n)

    return steps


# ---------------------------------------------------------------- O(N^2) FUNCTIONS ---------------------------------------------------------------- #

def countNsquare(n:int)->int:
    '''
    F(n): n^2
    '''
    steps = 0
    for i in range(n):
        steps += countN(n)

    return steps


def countNsquare_func1(n:int)->int:
    '''
    F(n): n^2 + 5000n
    '''
    steps = 0
    
    steps += countNsquare(n)
    
    steps += countN_func3(n)
    
    return steps

def countNsquare_func2(n:int)->int:
    '''
    F(n): (5000n)^2
    '''

    steps = 0

    for i in range(n):
        steps += countN_func3(n)

    return steps

# ---------------------------------------------------------------- O(N^3) FUNCTIONS ---------------------------------------------------------------- #

def countNcubed(n:int) -> int:
    '''
    F(n): n^3
    '''
    steps = 0
    for i in range(n):
        steps += countNsquare(n)

    return steps






