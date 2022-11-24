class Solution:
    def removeDuplicateLetters(s):
        hash = {}
        visited = set()
        stack = []
        for i in range(len(s)):
            hash[s[i]] = i
        for i in range(len(s)):
            if len(stack) == 0:
                stack.append(s[i])
                visited.add(s[i])
            elif s[i] < stack[-1] and s[i] not in visited:
                while stack and stack[-1] > s[i] and hash[stack[-1]] > i:
                    a = stack.pop()
                    visited.remove(a)
                stack.append(s[i])
                visited.add(s[i])
            elif s[i] not in visited:
                visited.add(s[i])
                stack.append(s[i])
        return ''.join(stack)
                    
                
                