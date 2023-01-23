class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        len_strs=len(strs) #length of array
        word_len=len(strs[0]) #len of the word (rows essentialy)
        count=0 #the number of columns thats needs to be deleted
        flag=False #exit point for loops if not leters of not sorted it gets activated 
        for i in range(word_len):
            for j in range(1,len_strs):
                if strs[j-1][i]>strs[j][i]: #if not sorted this condtion staisfies
                    count+=1 #this colm is to be deleted
                    flag=True
                    break  # exits the for j loop
            if flag: #remains false then carry on
                continue
        return count

