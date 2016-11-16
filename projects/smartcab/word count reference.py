"""Count words."""

def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    
    # TODO: Count the number of occurences of each word in s
    words = s.split()
    words_occurance = {}
    for word in words:
      if word in words_occurance.keys(): words_occurance [word] += 1
      else: words_occurance[word]= 1
    # print words_occurance
    
    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    words_list = sorted (words_occurance.keys())  #first sorting alphabetcally. Made a seprate list of words where they are sorted alphabetically
    # print words_list
    words_ordered_list = sorted (words_list, key= words_occurance.get, reverse=True) # sorted the alphabetically sorted list by values of same in the dict using function words_occurance.get
    # print words_ordered_list
    # TODO: Return the top n words as a list of tuples (<word>, <count>)

    top_n=[]
    for word in words_ordered_list:
      if words_ordered_list.index(word)>=n: break
      tuple = (word, words_occurance[word]) # adding the sorted word list along with their values to tuple
      top_n.append(tuple) 
    return top_n


def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)
    print count_words("this is a sample to see how counting of words work in this sample. This should do the counting to prove that counting of words work", 3)


if __name__ == '__main__':
    test_run()
