strs = ["act","pots","tops","cat","stop","hat"]



def groupAnagrams(strs):
    # Create a dictionary
    anagrams = {}

    for i in strs:
        # concatinate letters making them 1 word
        letters=''.join(sorted(i))

        # Check if the word is a key in the dictionary
        if letters in anagrams:
            # If it is, add the word to the list of values
            anagrams[letters].append(i)

        else:
            # Else make a new key with that word
            anagrams[letters] =[i]
        
    # Return list of the values in the dictionary
    return list(anagrams.values())

        

print(groupAnagrams(strs))



