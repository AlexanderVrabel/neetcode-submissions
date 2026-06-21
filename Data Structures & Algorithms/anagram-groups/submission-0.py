class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strsDict = {}
        for i in strs:
            sortedI = "".join(sorted(i))
            if sortedI in strsDict:
                strsDict[sortedI].append(i)
            else:
                strsDict[sortedI] = [i]
        
        return list(strsDict.values())