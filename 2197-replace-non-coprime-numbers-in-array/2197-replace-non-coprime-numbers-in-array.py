class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack=[]
        for i in nums:
            while stack and math.gcd(stack[-1],i)>1:
                i=math.lcm(stack.pop(),i)
            stack.append(i)
        return stack
                

                        
        
