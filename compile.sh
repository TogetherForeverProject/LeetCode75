#!/usr/bin/bash

if [ $# -eq 0 ]; then
    echo "Usage: $0 <problem number>"
    exit 1
fi

problem_number=$1
python_script="problem${problem_number}.py"
test_script="test/test_problem${problem_number}.py"

if [ ! -f "$python_script" ]; then
    echo "Error: $python_script not found."
    exit 1
fi

echo "Running test for problem ${problem_number}"
echo "=========================="
python -B -m pytest -p no:cacheprovider "${test_script}"

echo "Compiling problem ${problem_number}"
echo "==========================="
# Execute the Python script with the -B option
python -B "$python_script"
