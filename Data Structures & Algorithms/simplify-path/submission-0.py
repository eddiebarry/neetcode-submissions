class Solution:
    def simplifyPath(self, path: str) -> str:
        
        q = []

        for ch in path.split('/'):
            if ch == '.' or ch == '':
                continue
            if ch == '..':
                if q: 
                    q.pop()
            else:
                q.append(ch)
        
        return '/' +'/'.join([ch for ch in q]) if q else '/'
