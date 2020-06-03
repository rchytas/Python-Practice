def anagramSolution2(s1,s2):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True
    while pos < len(s1) and matches:
        if alist1[pos]==alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches

print(anagramSolution2('abcde','edcba'))

def groupAnagrams():
    # Python3 code to demonstrate 
    # Grouping Anagrams 
    # using defaultdict() + sorted() + values() 
    from collections import defaultdict 
      
    # initializing list 
    test_list = ['lump', 'eat',  'me',  'tea', 'em', 'plum'] 
      
    # printing original list 
    print("The original list : " + str(test_list)) 
      
    # using defaultdict() + sorted() + values() 
    # Grouping Anagrams 
    temp = defaultdict(list) 
    for ele in test_list: 
        temp[str(sorted(ele))].append(ele) 
    res = list(temp.values()) 
    print(temp)
    print(type(temp.keys()))
      
    # print result 
    print("The grouped Anagrams : " + str(res)) 

groupAnagrams()