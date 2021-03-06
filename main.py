from min_hash import *
import datetime
import random

def get_genome(filename):
    """
    return the name and genome as strings given the genome file name
    :param filename: the name of the file to grab the genome from
    :return: name is the name given at the top of the genome file, genome is the genome as a string
    """
    file_open = open(filename, "r")
    genome = ""
    name = ""
    for line in file_open:
        if line[0:1] == ">":
            name = line[1:].rstrip()
        else:
            genome = genome + line.rstrip()

    file_open.close()
    return name, genome

def get_reads(filename):
    """
    return an array of all of the reads
    :param filename: the name of the file to grab the reads from
    :return: array of the reads
    """
    file_open = open(filename, "r")
    read = ""
    name = ""
    reads = []

    for line in file_open:
        if line[0:1] == ">":
            if read != "":
                reads.append(read)
                read = ""
         #   name = line[1:].rstrip()
        else:
            read = read + line.rstrip()

    reads.append(read)
    file_open.close()
    print "# of reads:", len(reads)
    return reads

def mutate(genome, variation):
    """
    Mutate the given genome by the amount specified in the variation
    :param genome: the genome to be mutated
    :param variation: the percent amount that we want to mutate the genome by, up to 2 decimals
    :return: the mutated genome
    """
    return_genome = ""
    for i in range(0,len(genome)):
        if random.randint(1,10000) < variation*100:
            transform_num = random.randint(1,6)
            #First four represent a random mutation
            #Could also randomly select the same letter
            if transform_num == 1:
                return_genome = return_genome + "A"
            elif transform_num == 2:
                return_genome = return_genome + "C"
            elif transform_num == 3:
                return_genome = return_genome + "G"
            elif transform_num == 4:
                return_genome = return_genome + "T"
            #Choice five represents an insertion
            elif transform_num == 5:
                #Create a random insertion
                insert_num = random.randint(1,4)
                if insert_num == 1:
                    return_genome = return_genome + "A" + genome[i]
                elif insert_num == 2:
                    return_genome = return_genome + "C" + genome[i]
                elif insert_num == 3:
                    return_genome = return_genome + "G" + genome[i]
                elif insert_num == 4:
                    return_genome = return_genome + "T" + genome[i]
            #Choice six represents a deletion so nothing is added
            else:
                pass
        else:
            return_genome = return_genome + genome[i]

    return return_genome


def all_new_data():
    """
    This is the menu function for a user to create their own MinHash. Allows user to add genomes, and compare them
    """
    num_hashes = raw_input("Please enter your desired number of hash functions: ")
    shingle_size = raw_input("Please enter your desired shingle size: ")

    #Create a new MinHash according to the desired parameters
    user_hash = min_hash(int(num_hashes),int(shingle_size),1)

    while True:
        print ("-------------NEW HASH MENU--------------")
        print ("Please select an option and press enter")
        print ("0 to exit")
        print ("1 to add a new genome")
        print ("2 to compare two genomes")
        print ("3 to mutate and add an existing genome")
        print ("------------------------------------------")
        choice = raw_input("Your choice: ")

        if choice == "1":
            #Add a new genome to the created hash
            add_genome_with_temp_hash(user_hash)
        elif choice == "2":
            #Compare two of the genomes in the created hash
            compare_two_temp_genome(user_hash)
        elif choice == "3":
            #Compare two of the genomes in the created hash
            mutate_genome_with_temp_hash(user_hash)
        else:
            ans = raw_input("Exiting will delete all of the genomes you have added here. "
                            "Are you sure you want to continue (Y/N)?")
            if ans == "Y":
                print ("Exiting...")
                exit(0)





def set_up_precomputed_minhashes(filename):
    """
    return the name and genome as strings given the genome file name
    :param filename: the name of the file to grab the minhashes from
    :return: map of hashes
    """
    file_open = open(filename, "r")
    for line in file_open:
        index = line.find(":")
        name = line[0:index]
        temp_min_hash = []
        hashnums = line[index+2:]
        for num in hashnums.split():
            temp_min_hash.append(long(num))
        minhash_saved.articles[name] = temp_min_hash

    file_open.close()

def add_genome_defined_hash():
    """
    Function called to add a genome to the already defined MinHash
    """
    filename = raw_input("File Name and Directory (Including extension): ")
    name, genome = get_genome(filename)
    print "Min Hashing given genome: " + name
    minhash_saved.add_article(name, genome)
    print "Adding hash to our hash numbers file"
    minhash_tosave = minhash_saved.articles[name]

    writestring = name + ": "
    for num in minhash_tosave:
        writestring = writestring + str(num) + " "
    #Delete the last space
    writestring = writestring[:-1]
    file_open = open(saved_hash_filename, "a")
    file_open.write(writestring + "\n")
    file_open.close()

def add_mutated_genome_defined_hash():
    """
    Function called to mutate a genome and add it to the already defined MinHash
    """
    print "The genome you give here will be mutated before being MinHashed"
    filename = raw_input("File Name and Directory (Including extension): ")
    name, genome = get_genome(filename)
    rate = raw_input("Mutation rate percentage (up to 2 decimals): ")

    #Mutate the genome selected
    mutated_genome = mutate(genome, float(rate))
    print "Genome mutated successfully, now adding to minhash"
    minhash_saved.add_article(name + " Mutated " + str(rate) + "%", mutated_genome)
    print "Adding hash to our hash numbers file"
    minhash_tosave = minhash_saved.articles[name + " Mutated " + str(rate) + "%"]

    writestring = name + " Mutated " + str(rate) + "%" + ": "
    for num in minhash_tosave:
        writestring = writestring + str(num) + " "
    #Delete the last space
    writestring = writestring[:-1]
    file_open = open(saved_hash_filename, "a")
    file_open.write(writestring + "\n")
    file_open.close()

def add_genome_with_temp_hash(user_hash):
    """
    Function to add a new genome to a temporary MinHash
    :param user_hash: the MinHash to add the genome to
    """
    filename = raw_input("File Name and Directory (Including extension): ")
    name, genome = get_genome(filename)
    print "Min Hashing given genome: " + name
    user_hash.add_article(name, genome)
    print "Min Hashing complete!"

def mutate_genome_with_temp_hash(user_hash):
    """
    Function to mutate a new genome to a temporary MinHash
    :param user_hash: the MinHash to add the mutated genome to
    """
    filename = raw_input("File Name and Directory (Including extension): ")
    name, genome = get_genome(filename)
    rate = raw_input("Mutation rate percentage (up to 2 decimals): ")
    #Mutate the genome selected
    mutated_genome = mutate(genome, float(rate))
    print "Genome mutated successfully, now adding to minhash"
    user_hash.add_article(name + " Mutated " + str(rate) + "%", mutated_genome)
    print "Min Hashing complete!"

def compare_two_genome_defined_hash():
    """
    Function called to compare two of the genomes in our pre-defined MinHash
    """
    print "Here are the genomes we have to compare"
    name_arr = []
    i = 0
    for key in minhash_saved.articles.keys():
        name_arr.append(key)
        print str(i) + ") " + key
        i += 1

    first_choice = raw_input("First Selection (Number): ")
    second_choice = raw_input("Second Selection (Number): ")
    percent = 100*minhash_saved.get_similarity(name_arr[int(first_choice)], name_arr[int(second_choice)])
    print "Comparing the genomes - "
    print name_arr[int(first_choice)]
    print name_arr[int(second_choice)]
    print "Similarity: " + str(percent) + "%"

def compare_two_temp_genome(user_hash):
    """
    Function to compare two genomes from a temporary MinHash
    :param user_hash: the MinHash to compare from
    """
    print "Here are the genomes you added to compare"
    name_arr = []
    i = 0
    for key in user_hash.articles.keys():
        name_arr.append(key)
        print str(i) + ") " + key
        i += 1

    first_choice = raw_input("First Selection (Number): ")
    second_choice = raw_input("Second Selection (Number): ")
    percent = 100*user_hash.get_similarity(name_arr[int(first_choice)], name_arr[int(second_choice)])
    print "Comparing the genomes - "
    print name_arr[int(first_choice)]
    print name_arr[int(second_choice)]
    print "Similarity: " + str(percent) + "%"

def run_defined_hash():
    """
    Main Function to run for the pre-defined MinHash
    """
    ############################################
    #Menu stuff
    print "We currently have hashes for: "
    for key in minhash_saved.articles.keys():
        print key

    print ("-------------SAVED HASH MENU--------------")
    print ("Please select an option and press enter")
    print ("0 to exit")
    print ("1 to add a new genome")
    print ("2 to compare two genomes")
    print ("3 to add a mutated genome")
    print ("------------------------------------------")
    choice = raw_input("Your choice: ")

    if choice == "1":
        #Add a new genome to our hashnums.txt
        add_genome_defined_hash()
    elif choice == "2":
        #Compare two of the genomes we have
        compare_two_genome_defined_hash()
    elif choice == "3":
        add_mutated_genome_defined_hash()
    else:
        print ("Exiting...")
        exit(0)
    ##############################################


def add_reads_begin_hash():
    """
    Calculate and print the scores of the reads compared to each genome we have stored
    Counts the number of hits we have for each read->genome fingerprint comparison
    """
    filename = raw_input("File Name and Directory (Including extension): ")
    reads = get_reads(filename)
    #Create map for scoring
    genome_score = {}
    for genome in minhash_saved.articles.keys():
        genome_score[genome] = 0
    for read in reads:
        # Adding an article automatically overwirtes a previous one with the same name
        minhash_saved.add_article("read", read)
        for genome in minhash_saved.articles.keys():
            if genome != "read":
               if minhash_saved.get_similarity("read", genome) > 0:
                   genome_score[genome] += 1
    minhash_saved.delete_article("read")
    print "Genome Hits For Reads:"
    for genome in genome_score.keys():
        print genome + ": " + str(genome_score[genome])


def main():
    """
    Main Function Loop
    """
    while True:
        print ("-------------HOME MENU--------------")
        print ("Please select an option and press enter")
        print ("0 to exit")
        print ("1 to run with all new data")
        print ("2 to run with pre-selected hashes")
        print ("3 to run reads against stored hashes")
        print ("------------------------------------")
        choice = raw_input("Your choice: ")

        if choice == "1":
            #This doesnt do what I want it to do right now
            #It just runs the old code right now
            all_new_data()
        elif choice == "2":
            run_defined_hash()
        elif choice == "3":
            add_reads_begin_hash()
        elif choice == "0":
            print ("Exiting...")
            exit(0)

#Set up our globally stored information
#For the saved minhash
global saved_hash_filename
saved_hash_filename = "hashnums.txt"
#This is a predetermined MinHash Function
saved_hash = [100812221, 1012216673, 2724886533, 3713561295, 3704220460, 3112985602, 3655860748, 1023600249, 593097041, 2892599333, 1448004575, 3801471907, 368044835, 678078168, 3608322806, 3564805288, 674329378, 1067228399, 91608111, 540214929, 3765067669, 3219447150, 3148060934, 2135471616, 2401450681, 2987631727, 2835615844, 2389716441, 3491962627, 1421141602, 270318612, 2863616457, 2997764315, 1412478562, 1747777209, 2752703216, 2839552925, 1003621188, 523755966, 3572997441, 1703508918, 1902896465, 422771180, 3317716637, 842587289, 3428433996, 3457815678, 3181112400, 1228782229, 4214998960, 3675958758, 144359873, 3565183215, 3253427381, 3894931338, 950600950, 249604060, 2384294229, 930225442, 367269762, 1198125501, 3291608642, 3153982165, 2400338004, 66964370, 155429338, 3290360214, 474134523, 808674495, 1083398942, 3407470949, 3789194285, 691762897, 2228227507, 3914476907, 3769913061, 2222392774, 2934986323, 3227924490, 2290374904, 3279511850, 4264351692, 588602744, 2453336838, 3114729672, 3513648113, 3185955759, 3086181896, 1242702683, 1163981952, 1601502496, 713899053, 3384526484, 753403463, 4136310947, 2382078233, 2972629400, 2877763078, 608293111, 3590941424, 2641267673, 2422264801, 513079753, 2097596902, 1696332477, 1715325154, 1031255710, 1593472944, 762009352, 481480303, 2294120733, 509113695, 2950745956, 1825971936, 2571645712, 3346955169, 2508218675, 3229366270, 450231117, 3504245449, 1758391726, 735752981, 1665521780, 3615775971, 1806324574, 680529743, 2371294787, 3583746767, 2732175550, 3199396713, 3358603313, 531542364, 194517513, 3539896642, 3773063066, 722027652, 3680066373, 2818354049, 1285147905, 2740612483, 2012385358, 1081561511, 1122017246, 4154800764, 2044167219, 1287388873, 3213910162, 2038519516, 66096803, 1696030903, 318379715, 3962679749, 2021632220, 3421167384, 3036567640, 3998894496, 1683957540, 3541140008, 142295478, 673797322, 694855126, 2294602884, 89788257, 4025399103, 2355358098, 3068181027, 2846484503, 3142942959, 3982788037, 1451799361, 3646328872, 2395234189, 620232457, 2181240814, 283389245, 112295929, 2268606677, 3239811647, 2690901112, 1364321913, 2895838015, 2059900383, 1612278460, 1483647671, 4218599085, 2969627889, 3488451073, 3967562870, 3005423457, 2244684175, 1530580371, 2928809573, 3538802110, 1403072820, 2473640532, 282879791, 3691164018, 63180133, 3618998977, 1201812408]
global minhash_saved
minhash_saved = min_hash(200, 50, 1, saved_hash)
set_up_precomputed_minhashes(saved_hash_filename)
main()