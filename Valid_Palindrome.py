class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        

        #setting only alphanumeric chars on a empty string
        str1=' '
        for i in s:
            if i.isalnum():
                str1=str1+i
            
        #striping the string out of its front and back trailing spacing
        check=str1.strip()

        #checking palindrome by neg indexing
        if check==check[::-1]:
            return  True
        else :
            return False

             
