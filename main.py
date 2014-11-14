from min_hash import *

def get_genome(filename):
    file_open = open(filename, "r")
    genome = ""
    name = ""
    for line in file_open:
        if line[0:1] == ">":
            name = line[1:]
        else:
            genome = genome + line.rstrip()

    return name, genome

#Create our min hash
hash = min_hash(100,500000,30)
#Get our first genome
name, genome = get_genome("test_genomes/Escherichia coli SE15.fasta")
#add to our hash
hash.add_article(name, genome)
hash.add_article(name + "1", genome)