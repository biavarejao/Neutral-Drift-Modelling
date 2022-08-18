# Neutral-Drift-Modelling
 # Packages Requirements
  In the python script are used the packages:
  - numpy 
  - matplotlib
  # Theoretical Basis, Goals and Methods
  The Moran Model consists on a stochastic model to simulate the evolution in a finite population. In my scripts I simulated a case of neutral evolution, in which the alleles A and B have the same fitness. In the model we assume a finite population with population size fixed (N), generations discrete, that means that they can overlap, a very low mutation rate, so no new mutants will appear in the simulations, and an assexual reproduction.\
  In each iteration one individual in the population will be randomly choose to reproduce. Then, one individual in the population will be randomly choose to be replaced by the first individual chosen. 
  My project intends to simulate stochastically a case of neutral genetic drift. My first script "moranmodel.py" simply simulate stochastically n times a neutral drift in a population with size N and an initial i amount of A individual in a maximum time of tmax. The script save in the subdirectory figs a graph of the frequency of the allele x time. My second script "fixationfrequency.py" simulate stochastically n times a neutral drift in a population with size N, in different amounts of i individuals (iter_i different initial conditions are simulated), in a maximum time of tmax. In the end, the script plots and save in the subdirectory figs a graph with the initial frequency of the A allele in the population x the rate of fixation of the allele A in the population (times that the A allele fixated / n). We consider a fixation case if within the tmax time, the A allele has reached 100% of frequency in the population. In the graph we also plot the expected result according to theory. 
  
# Project Structure
  
  ```
project/
     ├── py/
*    │   └── figs/
*    ├── gitignore/
*    └── README.md
```
The py folder contains my scripts in the Python language and the figs subfolder. The figs subfolder contains the figures generated by my scripts

  
  
