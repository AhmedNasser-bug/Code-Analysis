from setup import*
from Test_algorithms import*

def derivative(f, x, h, m):
    return (f(m, x + h)-f(m, x-h))/(2*h)

def log_value(base:Decimal, arg:Decimal) -> Decimal:
    '''
    Returns the logarithm of the given number to the given base.
    If the argument is zero, it returns zero.
    '''
    if arg and base != 1:
        return Decimal(log(arg, base))
    else:
        return 0

def log_plateua(y2:Decimal, y1:Decimal)->Decimal:
    '''
    Returns the logarithmic plateau of runtimes during the tests
    '''
    return Decimal(y2 / y1) if y1 else 0


def stress_test_steps_algo(algorithm, range_of_input:int, multiplier:float) -> dict:
    '''
    Takes a range on numbers as the range of inputs of the given algorithm \n
    Returns a dictionary with the following values:
      the total runtime for all tests\n
      the logarithmic plateau of run-times during the tests (the ratio of the current runtime to the previous runtime)\n
      the average runtime of all tests\n
    Mathematical Model: log_2(range_of_input) * (F(n) + C1 + C2 + C3)
    '''
    prev_time, prev_steps = get_algo_time_fast(algorithm, 1)
    prev_steps_log_value = 0
    inp = ceil(multiplier)# start from input size multiplier

    graphs = defaultdict(list)
    MpN_values = []


    # start the stress test
    while inp < range_of_input:
        # measure the runtime of the current algorithm with input size i
        cur_time, cur_steps = get_algo_time_fast(algorithm, inp) # F(m^n)
        
        # Calculate the logarithm of the current algorithm runtime function
        # ------------------------------------ C0
        cur_time_log_value = log_value(multiplier, cur_time) # log_m(T(m^n))
        graphs['time logarithmic values'].append(cur_time_log_value)

        # Calculate the logarithm of the current algorithm steps function
        # ------------------------------------ C1
        cur_steps_log_value = log_value(multiplier, cur_steps) # log_m(F(m^n))
        graphs['steps logarithmic values'].append(cur_steps_log_value)

        # Calculate the logarithmic plateau and slope of the runtimes
        # ------------------------------------ C2
        cur_steps_log_plateau = log_plateua(cur_steps, prev_steps) # log_m(F(m^n))/log_m(F(m^n/m))
        graphs['steps log plateaus'].append(cur_steps_log_plateau)

        # Calculate the slope of the log line of the runtime function
        # ------------------------------------ C3
        cur_steps_log_slope = log_value(inp, cur_steps) # log_m(F(m^n))
        graphs['steps log slopes'].append(cur_steps_log_slope)

        # Calculate the logarithmic plateau and slope of the runtimes
        # ------------------------------------ C4
        cur_time_log_plateau = log_plateua(cur_time, prev_time) # log_m(T(m^n))/log_m(T(m^n/m))
        graphs['time log plateaus'].append(cur_time_log_plateau)         

        # Calculate the slope of the log line of the runtime function
        # ------------------------------------ C5
        cur_time_log_slope = log_value(inp, cur_time) # log_m(T(m^n))
        graphs['time log slopes'].append(cur_time_log_slope)

        # Calculate the differentiation of the logarithmic steps function
        # ------------------------------------ C6
        delta_steps_log_values, delta_inp = Decimal(cur_steps_log_value - prev_steps_log_value), Decimal(inp - ((inp-1)/multiplier))
        cur_steps_diff_log_slope = Decimal(delta_steps_log_values/delta_inp)
        graphs['differentiation of log values'].append(delta_steps_log_values) # d(x)

        # ------------------------------------ C7
        print(f'''N: {inp},     Time: {cur_time}, \nSteps: {cur_steps},
            Steps log diff: {cur_steps_diff_log_slope},  Steps log slope: {cur_steps_log_slope},   Steps log value: {cur_steps_log_value}
            \nTime log value: {cur_time_log_value},   Time log slope: {cur_time_log_slope}\ndelta log values: {delta_steps_log_values}\n\n''' )

        # update the previous steps
        graphs['time values'].append(cur_time)
        graphs['steps values'].append(cur_steps)
        prev_steps = cur_steps
        prev_time = cur_time
        prev_steps_log_value = cur_steps_log_value

        # double the input_size
        MpN_values.append(inp)
        inp  = ceil(inp * multiplier)



    # approximate time complexity
    predicted_complexity_power = log(cur_steps_log_plateau, multiplier) if cur_steps_log_plateau else 0
    time_prediction = log(cur_time_log_plateau, multiplier) if cur_time_log_plateau else 0
    steps_prediction = log(cur_steps_log_plateau, multiplier)


    return {
            'last time log slope': cur_time_log_slope,
            'last time log plateau': cur_time_log_plateau,
            'last steps log slope': cur_steps_log_slope,
            'last steps log plateau': cur_steps_log_plateau,
            'predicted complexity power': predicted_complexity_power,
            'time prediction': time_prediction,
            'steps prediction': steps_prediction,
            'N_values': MpN_values,
            'graphs': graphs
           }


def stress_test_time_algo(algorithm, range_of_input:int, multiplier:float) -> dict:
    '''
    Takes a range on numbers as the range of inputs of the given algorithm \n
    Returns a dictionary with the following values:
      the total runtime for all tests\n
      the logarithmic plateau of run-times during the tests (the ratio of the current runtime to the previous runtime)\n
      the average runtime of all tests\n
    Mathematical Model: log_2(range_of_input) * (F(n) + C1 + C2 + C3)
    '''
    prev_time, output = get_algo_time_fast(algorithm, 1)
    prev_time_log_value = 0
    inp = ceil(multiplier)# start from input size multiplier

    graphs = defaultdict(list)
    MpN_values = []


    # start the stress test
    while inp < range_of_input:
        # measure the runtime of the current algorithm with input size i
        cur_time, cur_output = get_algo_time_fast(algorithm, inp) # F(m^n)
        
        # Calculate the logarithm of the current algorithm runtime function
        # ------------------------------------ C0
        cur_time_log_value = log_value(multiplier, cur_time) # log_m(T(m^n))
        graphs['time logarithmic values (log_m(T(m^n)))'].append(cur_time_log_value)

        # Calculate the logarithmic plateau and slope of the runtimes
        # ------------------------------------ C4
        cur_time_log_plateau = log_plateua(cur_time, prev_time) # log_m(T(m^n))/log_m(T(m^n/m))
        graphs['time log plateaus (log_m(T(m^n))/log_m(m^n/m))'].append(cur_time_log_plateau)         

        # Calculate the slope of the log line of the runtime function
        # ------------------------------------ C5
        cur_time_log_slope = log_value(inp, cur_time) # log_m(T(m^n))
        graphs['time log slopes (log_m(T(m^n)))'].append(cur_time_log_slope)

        # Calculate the differentiation of the logarithmic steps function
        # ------------------------------------ C6
        delta_steps_log_values, delta_inp = Decimal(cur_time_log_value - prev_time_log_value), Decimal(inp - ((inp-1)/multiplier))
        cur_steps_diff_log_slope = Decimal(delta_steps_log_values/delta_inp)
        graphs['delta of log values'].append(delta_steps_log_values) # d(x)
        graphs['diffrentiation of log values d/dx log_m(T(m^n))/log_m(T(m^n/m))'].append(cur_steps_diff_log_slope) # d/dx 

        # update the previous steps
        graphs['time values T(m^n)'].append(cur_time)
        prev_time = cur_time
        prev_time_log_value = cur_time_log_value

        # double the input_size
        MpN_values.append(inp)
        inp  = ceil(inp * multiplier)



    # approximate time complexity
    predicted_complexity_power = log(cur_time_log_plateau, multiplier) if cur_time_log_plateau else 0
    
    return {
            'last time log slope': cur_time_log_slope,
            'last time log plateau': cur_time_log_plateau,
            'predicted complexity power': predicted_complexity_power,
            'N_values': MpN_values,
            'graphs': graphs
           }



if __name__ == "__main__":

    range_input = int(input("Enter the range of numbers of the test: "))
    multiplier = float(input("Enter the multiplier for the input size: "))
    # Test the algorithm with a simple function and a range of input sizes
    result = stress_test_steps_algo(countN, range_input, multiplier)
    plot_against_input(result['N_values'], result['graphs'])
    print_test_results(result)
  
