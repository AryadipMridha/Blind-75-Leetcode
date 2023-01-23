class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split(" ") #splits s by the spaces , each words bcoms element

        if len (pattern)!= len(words):
            return False
        charToWord={}   # charecter maps to words set
        wordToChar={}    #words maps to charecter
        
        for charecter , word in zip(pattern,words):     #zip is itr tool for running two loops simultaneously
            if charecter in charToWord and charToWord[charecter]!=word:     #means if charecter is already mapped to different words and not the new word we are looking at 
                return False
            if word in wordToChar and wordToChar[word]!=charecter:      #means if word is already mapped to different charecter and not the new charecter we are looking at 
                return False
            charToWord[charecter]=word #if its a new charecter which hasnt been mapped then map it to new word
            wordToChar[word]=charecter #if its a new word which hasnt been mapped then map it to new charecter
        return True
