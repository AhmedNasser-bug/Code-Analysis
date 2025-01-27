#pragma once
#include <chrono>
#include <utility>
#include <iostream>
#include <map>
#include <cmath>
#include <vector>
#include <stack>
#include <fstream>
#include <string>
#include "String.h"
#include <functional>
using namespace std;

struct AlgorithmAnalysis {
    double last_time_log_slope;
    double last_time_log_plateau;
    double predicted_Upper_Bound;
    double predicted_Tight_Bound;
    double predicted_Lower_Bound;
    vector<double> N_values;
    map<string, vector<double>> graphs;
};


template<typename Func, typename... Args>
double get_algo_time(Func algorithm, Args&&... args) {
    using Clock = chrono::high_resolution_clock;

    // Get start time
    auto start_time = Clock::now();

    // Execute algorithm
    algorithm(forward<Args>(args)...);

    // Get end time
    auto end_time = Clock::now();

    // Calculate duration in milliseconds
    double sduration = chrono::duration<double, std::milli>
        (end_time - start_time).count();

    return sduration;
}

vector<string> get_file_contents(string path)
{
    vector <string> Inputs;

    fstream MyFile;

    MyFile.open(path, ios::in);//read Mode

    if (MyFile.is_open())
    {

        string Line;

        while (getline(MyFile, Line))
        {
            Inputs.push_back(Line);
        }

        MyFile.close();

    }

    return Inputs;
}

bool isAlphabetical(char c)
{
    return (int(c) >= 76 and int(c) <= 76 + 27) or (int(c) >= 96 and int(c) <= 121);
}

bool isNumeric(char c)
{
	return int(c) >= 48 and int(c) <= 57;
}

// Experimental and just an approximation
int get_approx_Bytes_Of_TestCase(string Testcase) {

    int num_seq = 0;
    bool char_seq = false;
    int total_bytes = 0;
    for (long idx = 0; idx < Testcase.length(); idx++ ) 
    {
		char c = Testcase[idx];
        // if the current char is alphabetical, add the number of bytes by 1
        if (isAlphabetical(c)) 
        {
            total_bytes += 1;
            num_seq = 0;
            char_seq = true;
        }
        else
        {
            if (char_seq) 
            {
                total_bytes += 1;
            }
            else 
            {
                if (!isNumeric(c) and !isAlphabetical(c))
                {
					char_seq = false;
                }
                total_bytes += 4;
            }
        }
    }

	return total_bytes;
}

// Experimental and just an approximation
int get_approx_Bytes_Of_TestCase2(string TestCase) 
{
    return TestCase.length();
}

vector<string> get_File_TestCases(string path)
{
    vector<string> Lines = get_file_contents(path);
    return Lines;
}

// Must be user defined for now..should be automated in the future
//vector<int> get_Input_sizes(string path)
//{
//    
//}


// Helper functions 

double log_value(double base, double value) {
    return base != 0 and value != 0 ? log(value) / log(base) : 0;
}

double log_plateua(double current, double previous) {
    return previous != 0 ? current / previous : 0;
}

// Returns the average of a vector of doubles
double avg(vector<double>& values)
{
    double sum = 0;
    for (double& value : values) {
        sum += value;
    }

    return abs(sum / values.size());
}