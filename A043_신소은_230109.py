# LeetCode
# 14. Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=lambda x: len(x)) # 주어진 strs를 원소의 길이를 기준으로 오름차순 정렬
        # prefix의 최대의 길이는 strs 내에서 가장 짧은 원소의 길이와 같음

        if len(strs) == 0: # strs가 빈 list라면
            return ''
        else:
            for i in range(len(strs[0])): # 가장 짧은 원소의 길이만큼 반복 
                for j in range(1, len(strs)): # 나머지 원소의 개수만큼 반복
                    if strs[0][i] != strs[j][i]: # 첫 번째 원소의 i번째 글자가 j번째 원소의 i번째 글자와 다르면
                        return strs[0][:i] # 이전 글자까지 리턴 
            return strs[0] # 첫 번째 원소가 다른 원소들에 모두 포함되어 있다면 첫 번째 원소가 곧 prefix
        
