import sys, random

class SimpleMarkovGenerator(object):

    def read_files(self, filenames):
        """Given a list of files, make chains from them."""

        filenames = sys.argv[1]
        input_text = open(filenames)
        self.open_file = input_text


    def make_chains(self):
        """Takes input text as string; returns dictionary of markov chains."""

        words = []
        for line in self.open_file:
            words.extend(line.split())
        markov_dict = {}

        for i in range(len(words)-1):
            markov_key = (words[i], words[i+1])
            markov_dict[markov_key] = []
        for i in range(len(words)-1):
            markov_key = (words[i], words[i+1])
            try: 
                markov_dict[markov_key].append(words[i+2])
            except IndexError:
                pass

        self.markov_dict = markov_dict

        return markov_dict


    def make_text(self):
        """Takes dictionary of markov chains; returns random text."""
        first_bigram = random.choice(self.markov_dict.keys())
        w1, w2 = first_bigram
        markov_text_as_list = []

        for i in range(len(self.markov_dict.keys())):
            markov_text_as_list.append(w1)
            try:
                w1, w2 = w2, random.choice(self.markov_dict[w1,w2])
            except IndexError:
                break

        return " ".join(markov_text_as_list)

# test1= SimpleMarkovGenerator()

# test1.make_chains("green-eggs.txt")

# print test1.make_text()

if __name__ == "__main__":

    # we should get list of filenames from sys.argv
    filenames = sys.argv[1]
    print filenames
    # we should make an instance of the class
    markov_inst = SimpleMarkovGenerator()
    # we should call the read_files method with the list of filenames
    markov_inst.read_files(filenames)
    # we should call the make_text method 5x
    markov_inst.make_chains()
    print markov_inst.make_text()
    print markov_inst.make_text()
    print markov_inst.make_text()
    print markov_inst.make_text()
    print markov_inst.make_text()
