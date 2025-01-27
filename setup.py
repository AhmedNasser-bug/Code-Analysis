from time import *
#from timeit import*
from collections import defaultdict
from math import*
from decimal import*
from statistics import*
from matplotlib.pyplot import*
from time import *


def get_algo_time_fast(algorithm, *args, **kwargs):
    '''
    Measure the execution time of the algorithm for different inputs and return results in a tuple containing the time and the corresponding output
    '''
    start_time = time()
    test_output = algorithm(*args)
    end_time = time()
    
    return ((end_time - start_time) * pow(10, 3), test_output)
    

def print_test_results(results:dict):
    '''Print the test results'''
    print("Test Results:")
    for key, value in results.items():
        print(f"{key}: {value}")


def plot_against_input(N_values:list[int], graphs:dict, figsize:tuple = (20,10)):
    '''
    plot each list in the graph dictionary agains N values
    '''
    # Calculate required subplot layout
    n_metrics = len(graphs)
    n_cols = 4  # You can adjust this
    n_rows = (n_metrics + n_cols - 1) // n_cols  # Ceiling division

    fig, axes = subplots(n_rows, n_cols, figsize=figsize)
    fig.suptitle('Metrics vs N')

    # Convert axes to 2D array if it's 1D
    if n_rows == 1:
        axes = axes.reshape(1, -1)
    
    # Plot each metric
    for idx, (metric_name, metric_values) in enumerate(graphs.items()):
        row = idx // n_cols
        col = idx % n_cols
        
        axes[row, col].plot(N_values, metric_values, 'o-')
        axes[row, col].set_title(metric_name)
        axes[row, col].set_xlabel('N')
        axes[row, col].set_ylabel(metric_name)
        axes[row, col].grid(True)

    # Hide empty subplots
    for idx in range(len(graphs), n_rows * n_cols):
        row = idx // n_cols
        col = idx % n_cols
        axes[row, col].set_visible(False)
    
    tight_layout()
    show()