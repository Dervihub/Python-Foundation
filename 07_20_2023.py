from os import system
system('cls')

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        return min(nums, key=nums.count)

    def containsDuplicate(self, nums: list[int]) -> bool:
        return True if len(set(nums)) != len(nums)  else False
    

    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        check = [False] * (len(s)) + [True]
        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                uzun = len(w)
                if i + uzun <= len(s) and s[i: uzun + i] == w:
                    check[i] = check[i + uzun]
                if check[i]:
                    break
        return check[0]
    

s = Solution()
print('\n\t\t1-misol')
print(s.singleNumber([1,2,3,1,3]))  #2
print(s.singleNumber([1]))          #1

print('\n\t\t2-misol')
print(s.containsDuplicate([1,2,4,2]))   #true
print(s.containsDuplicate([1,2,3]))     #false

print('\n\t\t3-misol')
print(s.wordBreak("appleandapple",["apple",'and'])) #true
print(s.wordBreak('abcd', ['a', 'abc', 'b', 'cd'])) #true
print(s.wordBreak("catsandog",["cats","dog","sand","and","cat"])) #false