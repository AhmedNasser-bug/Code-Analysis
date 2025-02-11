# Summary
Measure Time complexity for any given single numeric parameter method using by measuring and proccessing the relation between input size and Time taken by a range on test cases 

# Technologies
1. Python.
2. matplotlib.
3. C++.

# How does it work
1. lets define a function **f(x)**.
2. Let the input multiply by a factor of **m** every iteration, thereby we measured **f(m^x)**, lets give it an alias **m(x)**.
3. lets get take the log of base **m** to **m(x)**, thereby we measured **log_m(m(x))** lets give it an alias of **l(x)**.
4. lets perform some simplification to the function **l(x)**, it expands to **log_m(f(m^x))**, giving you the log-log of **f(x)**.
5. Diffrentiating **l(x)** with a high enough input size returns the highest power present in **f(x)**.

# How to use main_engine.py:
1. choose the variation of the analysis function (steps/time)
2. choose the function to test / copy the function you want to use .
3. run the file.
4. choose the size of input and the multiplier used to calculate the time complexity.
5. wait for the results!

# How to use CPP_Code_Analysis:
1. Run "main.cpp"
2. choose the actual time complexity of the used function.
3. choose the multiplier used to calculate the time complexity and the input size.
4. wait for the results!
