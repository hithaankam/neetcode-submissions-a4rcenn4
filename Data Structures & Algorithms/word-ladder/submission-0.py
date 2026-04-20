class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = defaultdict(list)
        for word in wordList:
            split_word = [ch for ch in word]
            for i, ch in enumerate(word):
                split_word[i] = "*"
                rpr = "".join(split_word)
                adj[rpr].append(word)
                split_word[i] = ch
        #print(adj)
        queue = deque([])
        queue.append((beginWord, 1))
        visited = set()
        visited.add(beginWord)

        while queue:
            curr, cnt = queue.popleft()
            split_word = [ch for ch in curr]
            if curr == endWord:
                return cnt
            for i, ch in enumerate(curr):
                split_word[i] = "*"
                rpr = "".join(split_word)
                for nei in adj[rpr]:
                    if nei not in visited:
                        queue.append((nei, cnt + 1))
                        visited.add(nei)
                split_word[i] = ch
        return 0
