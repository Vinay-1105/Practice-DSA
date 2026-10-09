class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        #idhar hum decrement karte hai columnNumber ko 1 se for 1-based indexing
        #then hum remainder find karte hai, jisse hume curr pos of letter pata lagta hai
        #fir usse remainder ko uppercase mai convert karte hai
        #aur fir ans mai usse capital letter ko pehle add karte hai
        #aur columnNumber ko update karte hai
        ans=""
        while columnNumber>0:
            columnNumber = columnNumber-1
            ans=chr((columnNumber%26)+ord("A"))+ans
            columnNumber//=26
        return ans