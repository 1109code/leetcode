class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # 중복을 제거하고 정렬해 순환
        for char in sorted(set(s)):
            # 가장 빠른 char의 인덱스부터를 suffix
            suffix = s[s.index(char):]
            # set과 suffix가 일치하면
            if set(s) == set(suffix):
                # 해당 cahr와 suffix에서 해당 문자를 제거한 suffix를 재귀로 다시 탐색
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        # 모두 순회하고 나오면 없을땐 그냥 반환
        return ''