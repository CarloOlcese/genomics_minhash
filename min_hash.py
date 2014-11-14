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
            shingle_index = random.randint(1,len(text)-self.shingle_size-1)
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

hash = min_hash(10,50,5)
hash.add_article("article1", "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).")
hash.add_article("article2", "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).")
hash.add_article("article3", "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.")
#THere I am putting the numbers into a set so we can do set stuff
a = set(hash.articles["article1"])
b = set(hash.articles["article2"])
c = set(hash.articles["article3"])

#This is printing the intersection of the two sets
print a.intersection(b)
print a.intersection(c)
print b.intersection(c)