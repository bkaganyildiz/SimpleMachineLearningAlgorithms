# Project Title

Simple Machine Learning Algorithms

## Part1

Implementation of Analytical Linear Regression Implementation : TODO : find the weight matrix and RMS.


## Part2

Implementation of Iterative Linear Regression Implementation : TODO : find the weight matrix and RMS without using any matrix libraries and Linear Regression Methodology.

```
𝑤𝑗=𝑤𝑗−𝜇𝜕𝐸(Ɗ)/𝜕𝑤𝑗
```
## Part3 

Implementation of Weighted k-NN Classifier : that takes a data file as before, the value for 𝑘 for a k-NN predictor, and the
attribute values of a query of interest, and computes and prints a weighted real valued answer for
the query.

### Prerequisites

Numpy has been used you can install numpy using 

```
pip install -r requirements.txt
```

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Sample Invocation for Par1 : 

```
python AnalyticalSolver.py <filename>
```

Sample Invocation for Par2 : 

```
python IterativeSolver.py <filename> <𝜇> <continuation condition(minimum change in rms error)>
```
Sample Invocation for Par3 : 

```
python WeightedKNNSolver.py <filename> <kNN's k> <i> <L1> <L2> <L3> .... <Li>
```



## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


