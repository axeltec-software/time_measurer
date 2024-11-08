# TimeMeasurer

It is a simple python module which helps to measure execution time of a function
or a piece of python code.

## Installing
1. Clone this repository to your computer
2. Add this repository to your `PYTHONPATH`: `export PYTHONPATH=/path/to/time_measurer:$PYTHONPATH`
3. Use it

## Usage
You can measure this module by the following way:
```python
import time_measurer
# Some your code

# Measure execution time of one function:
with time_measurer.ScopeMeasurer("My benchmark function"):
    my_benchmark_function(...)

# Measure execution time of a piece of code:
with time_measurer.ScopeMeasurer("My loop"):
    for k, v in my_dict.items():
        # some logic here

# Print measured times after all measurements:
time_measurer.PrintTimers()
```
