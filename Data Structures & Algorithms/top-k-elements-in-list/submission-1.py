class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict={}
        for i in nums:
            dict[i]=dict.get(i,0)+1
        freq=[[] for _ in range(len(nums)+1)]
        for i,count in dict.items():
            freq[count].append(i)
        res = []
        for j in range(len(nums),0,-1):
            for n in freq[j]:
                res.append(n)
                if len(res)==k:
                    return res
      
      