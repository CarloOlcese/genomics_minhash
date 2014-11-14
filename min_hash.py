"""min hash data structure"""
import random
import sys
import hashlib

class min_hash():

    def __init__(self, num_hashes, num_shingles, shingle_size):
        #Store these values for our min_hash
        self.num_hashes = num_hashes
        self.num_shingles = num_shingles
        self.shingle_size = shingle_size
        #Create array of numbers used to hash
        self.hash_numbers = []
        #create the random numbers for our hashing function
        for i in range(0,self.num_hashes):
            self.hash_numbers.append(random.getrandbits(32))

        self.articles = {}

    def add_article(self, name, text):
        self.articles[name] = []

        for i in range(0,self.num_shingles):
            #Get a random number to pull the shingle from
            shingle_index = random.randint(0,len(text)-self.shingle_size-1)
            shingle = text[shingle_index:shingle_index+self.shingle_size]
            #Now that we have the shingle, lets calculate the minimum hash
            min_hashnum = sys.maxint
            for j in range(0,self.num_hashes):
                #We first hash the function and mask it with 32bits of 1's in order to get
                #The last 32 bits of the hash. Then we xor it with the random 32 bits we
                #Generated before. This creates our has number
                current_hash_num = (int(hashlib.md5(shingle).hexdigest(), 16) & 0xffffffff) ^ self.hash_numbers[j]

                #If our current hash is the lowest one, remember it
                if current_hash_num < min_hashnum:
                    min_hashnum = current_hash_num

            self.articles[name].append(min_hashnum)