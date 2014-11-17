from min_hash import *
import datetime
import random

def get_genome(filename):
    file_open = open(filename, "r")
    genome = ""
    name = ""
    for line in file_open:
        if line[0:1] == ">":
            name = line[1:]
        else:
            genome = genome + line.rstrip()

    file_open.close()
    return name, genome

def mutate(filename, variation):
    """
    Mutate the given genome by the amount specified in the variation
    :param filename: the name of the file of the genome to be mutated
    :param variation: the percent amount that we want to mutate the genome by, up to 2 decimals
    :return: the mutated genome
    """
    #Get the given genome
    name, genome = get_genome(filename)
    return_genome = ""
    for i in range(0,len(genome)):
        if random.randint(1,10000) < variation*100:
            transform_num = random.randint(1,4)
            if transform_num == 1:
                return_genome = return_genome + "A"
            elif transform_num == 2:
                return_genome = return_genome + "C"
            elif transform_num == 3:
                return_genome = return_genome + "G"
            else:
                return_genome = return_genome + "T"
        else:
            return_genome = return_genome + genome[i]

    return return_genome


#Get our first genome
name, genome = get_genome("test_genomes/Escherichia coli SE15.fasta")
name2, genome2 = get_genome("test_genomes/Sulfolobus islandicus LAL14.fasta")
#mutated_genome = mutate("test_genomes/Escherichia coli SE15.fasta", .1)

#Uses create our minimum hash structure
hash = min_hash(200,20,1)

print "Begin at:"
print datetime.datetime.now().time()
hash.add_article("article1", genome)
print "article 1 at"
print datetime.datetime.now().time()
hash.add_article("article2", genome2)
print "article 2 at"
print datetime.datetime.now().time()
print hash.get_similarity("article1","article2")
