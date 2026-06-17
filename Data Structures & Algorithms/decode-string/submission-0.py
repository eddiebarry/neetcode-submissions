class Solution:
    def decodeString(self, s: str) -> str:
        self.s = s
        return self.decode_idx(0, len(s)-1)

    def decode_idx(self, l, r):
        ans = ''

        while l <= r:
            if self.s[l].isalpha():
                ans += self.s[l]
                l+=1
            else:
                num = 0
                while self.s[l].isnumeric():
                    num*=10
                    num+= int(self.s[l])
                    l+=1
                
                if self.s[l] == '[':
                    br = -1

                temp_l = l+1
                while br != 0:
                    if self.s[temp_l]=='[':
                        br-=1
                    if self.s[temp_l]==']':
                        br+=1
                    
                    if br == 0:
                        ans += num *self.decode_idx(l+1, temp_l-1)
                        l = temp_l+1
                        break

                    temp_l+=1
        
        return ans
                    

        