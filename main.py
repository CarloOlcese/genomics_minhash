from min_hash import *
import datetime

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

#Get our first genome
name, genome = get_genome("test_genomes/Escherichia coli SE15.fasta")

#Uses create our minimum hash structure
hash = min_hash(200,20,1)

print "Begin at:"
print datetime.datetime.now().time()
hash.add_article("article1", genome)
print "article 1 at"
print datetime.datetime.now().time()
hash.add_article("article2", genome)
print "article 2 at"
print datetime.datetime.now().time()
print hash.get_similarity("article1","article2")