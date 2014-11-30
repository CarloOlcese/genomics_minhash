"""min hash data structure"""
import random
import sys
import hashlib

class min_hash():

    def __init__(self, num_hashes, shingle_size, step_size, hashes=None):
        """
        Constructor for creating a generic min_hash
        :param num_hashes: the number of hash functions to be used
        :param shingle_size: the size of each shingle to compare
        :param step_size: the number of steps we move ahead as we create shingles
        :param hashes: If we want to use precomputed hashes, this will be the hashnumbers
        """
        if hashes == None:
            #Store these values for our min_hash
            self.num_hashes = num_hashes
            self.shingle_size = shingle_size
            self.step_size = step_size
            #Create array of numbers used to hash
            self.hash_numbers = []
            #create the random numbers for our hashing function
            for i in range(0,self.num_hashes):
                self.hash_numbers.append(random.getrandbits(32))

            self.articles = {}
        else:
            #Store these values for our min_hash
            self.num_hashes = num_hashes
            self.shingle_size = shingle_size
            self.step_size = step_size
            #Use the passed array as our hash numbers
            self.hash_numbers = hashes
            self.articles = {}

    def add_article(self, name, text):
        self.articles[name] = []
        #Initialize every minhash number so we know it exists
        for i in range(0,self.num_hashes):
            self.articles[name].append(sys.maxint)

        #We are going to go through and get every shingle of a certain size
        #The reason why we are dividing by two is so that there is overlap among
        #the shingles. May want to change this to be changeable
        for i in range(0, len(text), self.step_size):
            #Make sure we are not going past the text
            if i+self.step_size > len(text):
                break
            shingle = text[i:i+self.shingle_size]
            original_hash_value = int(hashlib.md5(shingle).hexdigest(), 16) & 0xffffffff
            #Now that we have the shingle, lets calculate the minimum hash for all hashes
            for j in range(0,self.num_hashes):
                #We first hash the function and mask it with 32bits of 1's in order to get
                #The last 32 bits of the hash. Then we xor it with the random 32 bits we
                #Generated before. This creates our has number
                current_hash_num = original_hash_value ^ self.hash_numbers[j]

                #If our current hash is the lowest one, remember it
                if current_hash_num < self.articles[name][j]:
                    self.articles[name][j] = current_hash_num

    def get_similarity(self,article1,article2):
        sim_count = 0.0
        for i in range(0,self.num_hashes):
            if self.articles[article1][i] == self.articles[article2][i]:
                sim_count += 1

        return sim_count/self.num_hashes