class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0 
        
        wordset = set(wordList)
        
        wordlen = len(beginWord)
        step = 1
        
        q =deque()
        q.append((beginWord,step))
        if beginWord in wordset:
            wordset.remove(beginWord)
            
        chance = 0
        while q:
            # print(q)
            x, step = q.popleft()
            
            if x == endWord:
                chance = 1
                break
            
            for char in 'abcdefghijklmnopqrstuvwxyz':
                for i in range(wordlen):
                    word = x[:i]+char+x[i+1:]
                    # print(word)
                    if word in wordset:
                        q.append((word,step+1))
                        wordset.remove(word)
        
        if chance == 0:
            return 0
        else:
            return step
                    
        
        