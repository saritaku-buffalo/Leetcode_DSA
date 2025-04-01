from collections import defaultdict
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned):
        banned = set(word.lower() for word in banned)
        paragrapgh = re.sub(r'[!?\',;.]', " ", paragrapgh).lower()
        words = paragrapgh.split()
        word_count = defaultdict(int)
        for word in words:
            if word not in banned:
                word_count[word] += 1
        
        max_count = 0
        result = ""
        for word, count in word_count.items():
            if count > max_count:
                max_count = count
                result = word
        return result