class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            letters_s = {}
            letters_t = {}
            for letter in s:
                if letters_s.get(letter):
                    letters_s[letter]+=1
                else:
                    letters_s[letter] = 1
            
            for letter in t:
                if letters_t.get(letter):
                    letters_t[letter]+=1
                else:
                    letters_t[letter] = 1
        
            if letters_s == letters_t:
                return True
            else:
                return False