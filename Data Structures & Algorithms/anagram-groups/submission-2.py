class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def helper(string):
            arr=[0]*26
            for char in string:
                arr[ord(char)-ord('a')]+=1
            return arr
        grp=dict()
        for s in strs:
            has=str(helper(s))
            if has  not in grp:
                grp[has]=[s]
            else:
                grp[has].append(s)
        print(grp.values())
        return list(grp.values())

        