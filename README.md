# Neutral-Drift-Modelling
 # Packages Requirements\
  In the python script are used the packages:
  - numpy 
  - matplotlib
  # Theoretical Basis\
  The Moran Model consists on a stochastic model to simulate the evolution in a finite population. In my scripts I simulated a case of neutral evolution, in which the alleles A and B have the same fitness. In the model we assume a finite population with population size fixed (N), generations discrete, that means that they can overlap, a very low mutation rate, so no new mutants will appear in the simulations, and an assexual reproduction.\
  In each iteraction one individual in the population will be randomly choose to reproduce. Then, one individual in the population will be randomly choose to be replaced by the first individual chosen. Assuming the amount of i individuals with the A allele and N-i with the B allele, we can conclude that the probability that an A individual replaces a B, will be:
  \[ P_{i,i+1} = \frac{i}{N}\times\frac{N-i}{N} \]
  The probability that
  
  
