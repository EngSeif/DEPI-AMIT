
def word_count(sentence, is_case_sensitive):
    """
        word_count - count number of occurance of each word in a sentence
        
        parameters :
            - sentence : string input
            - is_case_sensitive : count wth case sensitivity in mind or not
        
        return :
             a dictionary where keys are the words in the 
             sentence and values are the counts of how 
             many times each word appears
    """
    
    if is_case_sensitive:
        return count_case_sensitive(sentence)
    else:
        return count_no_case_sensitive(sentence)
        

def count_case_sensitive(sentence):
    """
         count_case_sensitive - count number of occurance of each word in 
                                a sentence with maintaining case sensitivity
                                
        parameters :
            - sentence : string input
            - word_list : sentence split into list
            
        return :
            a dictionary where keys are the words in the 
            sentence and values are the counts of how 
            many times each word appears
    """
    word_list = sentence.split()
    word_dict = dict()
    for word in word_list:
        word_dict[word] = 0
        for i in range(len(sentence)):
            if sentence[i: i + len(word)] == word:
                word_dict[word] += 1
    return word_dict
                
def count_no_case_sensitive(sentence):
    """
         count_no_case_sensitive - count number of occurance of each word in 
                                a sentence with no mantaining for case sensitivity
                                
        parameters :
            - sentence : string input
            - word_list : sentence split into list
            
        return :
            a dictionary where keys are the words in the 
            sentence and values are the counts of how 
            many times each word appears
    """
    
    # make a unique list of words
    word_list = list(set(sentence.lower().split()))
    
    word_dict = dict()
    for word in word_list:
        if word_dict.get(word.lower(), None) == None:
            word_dict[word.lower()] = 0
        for i in range(len(sentence)):
            # Using lower() Method to ignore case sensitivity
            if sentence[i: i + len(word)].lower() == word.lower():
                word_dict[word.lower()] += 1
    return word_dict