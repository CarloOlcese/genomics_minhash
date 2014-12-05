genomics_minhash
================

Implementing a min_hash with genomic data to do comparisons between genomes and reads from genomes.

To run:

enter: "python main.py" into command line
program will prompt you with a list of options

0: to exit
  use this option to close the program

---------------------------------------------------

1: to add a new genome
  this option will ask you for your desired shingle size and desired number of hash functions.
  it then creates an entirely new hash function for you to use.
  it prompts yo with a new menu
  
  0: to exit
    use this option to close the program
  
  1: to add a new genome
    this option will prompt you for a file containing a genome. We have some samples already stored in the project. To use one,     enter "test_genomes/*file_name*" 
    This function will add the file to your hash (takes about 5 mins with 200 hashes)
  
  2: to compare two genomes
    choose this option to see the similarity between two of the genomes you have added to your hash function

---------------------------------------------------

2: to run with pre-selected hashes
  this option allows you to compare new genomes with our already computed hashes, or our computed hashes to eachother

  0: to exit
    use this option to close the program
  
  1: to add a new genome
    this option will prompt you for a file containing a genome. We have some samples already stored in the project. To use one,     enter "test_genomes/*file_name*" 
    This function will add the file to our hash function and file
  
  2: to compare two genomes
    choose this option to see the similarity between two of the genomes in our stored hashes

---------------------------------------------------

3: to run reads against stored hashes
  use this to compare reads to all of the hashes we have stored
  enter your file (we have some stored in the project to test with. To use one, enter "reads/*file_name*"), and the hits are printed for each genome.
  
  
