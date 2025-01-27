#include "Setup.h"
#include "Algorithms.h"




template<typename Func, typename ...Args>
vector<double> get_T_OF_N(Func algorithm,Args&&... args) 
{
    return nullptr;
}

/*
Returns a dictionary with the following values :
the total runtime for all tests
the logarithmic plateau of run - times during the tests(the ratio of the current runtime to the previous runtime)
the average runtime of all tests

Mathematical Model : 
Let M Be the number of lines inside the dominant loop with value 7
Mathematical: log_2(range_of_input) * (F(n) + C*M) + CM/2
log base 2 of the range of input multiplied by 
     C*M: the constant taken of the dominant loop 
     F(n): the time taken by the tested function
Plus the constant taken by the lines outside the dominant loop M/2
*/
template<typename Func>
AlgorithmAnalysis analyze_algorithm(Func algorithm, double multiplier, double range_of_input, int time_limit)
{
    map<string, vector<double>> graphs;
    vector<double> MpN_values;

    double prev_time = get_algo_time<int(__cdecl*)(int), int>(algorithm, 1);
    double prev_time_log_value = 0;
    double cur_time_log_value = 0;
    double cur_time_log_plateau = 0;
    double delta_time_log_values = 0;
    double cur_time_diff_log_slope = 0;
    double cur_time_log_slope = 0;
    long int inp = multiplier; // start from input size multiplier
     
    
    // Main analysis loop
    while (inp < range_of_input) {
        // Measure current runtime and output
        double cur_time = get_algo_time<int(__cdecl*)(int), int>(algorithm, inp);
      
        if (cur_time/1000 > time_limit)break;
        // Calculate logarithmic values
        cur_time_log_value = log_value(multiplier, cur_time);
        graphs["time logarithmic values (log_m(T(m^n)))"].push_back(cur_time_log_value);

        // Calculate logarithmic plateau
        cur_time_log_plateau = log_plateua(cur_time, prev_time);
        graphs["time log plateaus (log_m(T(m^n))/log_m(m^n/m))"].push_back(cur_time_log_plateau);

        // Calculate slope of log line
        cur_time_log_slope = log_value(inp, cur_time);
        graphs["time log slopes (log_m(T(m^n)))"].push_back(cur_time_log_slope);

        // Calculate differentiation of logarithmic steps
        delta_time_log_values = cur_time_log_value - prev_time_log_value;
        double delta_inp = inp - ((inp - 1) / multiplier); 
        cur_time_diff_log_slope = delta_time_log_values / delta_inp;

        // Add predicted tight bound to data graphs
        graphs["delta of log values"].push_back(delta_time_log_values);
        graphs["diffrentiation of log values d/dx log_m(T(m^n))/log_m(T(m^n/m))"].push_back(cur_time_diff_log_slope);

        // Update previous values
        graphs["time values T(m^n)"].push_back(cur_time);
        prev_time = cur_time;
        prev_time_log_value = cur_time_log_value;

        // Update input size
        MpN_values.push_back(inp);
        inp = ceil(inp * multiplier);
    }

    // Calculate predicted complexity
    double predicted_Upper_Bound = cur_time_log_plateau != 0 ? round(log_value(multiplier, cur_time_log_plateau)) : 0;
    double predicted_Tight_Bound = round(delta_time_log_values);
    double predicted_Lower_Bound = round(avg(graphs["diffrentiation of log values d/dx log_m(T(m^n))/log_m(T(m^n/m))"]));

    // Prepare return structure
    AlgorithmAnalysis result;
    result.last_time_log_slope = cur_time_log_slope;
    result.last_time_log_plateau = cur_time_log_plateau;
    result.predicted_Upper_Bound= predicted_Upper_Bound;
    result.predicted_Tight_Bound = predicted_Tight_Bound;
    result.predicted_Lower_Bound = predicted_Lower_Bound;
    result.N_values = std::move(MpN_values);
    result.graphs = std::move(graphs);

    return result;
}



void print_results(AlgorithmAnalysis analysis_result) 
{
	cout << "Predicted Upper Bound: " << analysis_result.predicted_Upper_Bound << endl << "Predicted Tight Bound: " << analysis_result.predicted_Tight_Bound << endl << "Predicted Lower Bound: " << analysis_result.predicted_Lower_Bound;
}


int main() {
	cout << "Enter the function number you want to analyze <1-3> inclusive (indicates the actualt timecomplexity of the test function): ";
	int func_num;
	cin >> func_num;

	cout << "Enter the range of input: ";
	double range_of_input;
	cin >> range_of_input;

	cout << "Enter the time limit: ";
	int time_limit;
	cin >> time_limit;

	cout << "Enter the multiplier: ";
	double multiplier;
	cin >> multiplier;

    AlgorithmAnalysis result = analyze_algorithm(get_func<int(__cdecl*)(int) >(func_num - 1), multiplier, range_of_input, time_limit); // make the time function parallel
	print_results(result);

	system("pause>0");
}
//TODO
// MODIFY LINE 43 TO TAKE ANY KIND OF FUNCTION POINTER ( look REAL TIME C++ BOOK for reference )