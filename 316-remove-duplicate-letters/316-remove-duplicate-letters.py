class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # counter는 문자별 개수를 자동으로 카이팅
        counter, seen, stack = collections.Counter(s), set(), []
        
        # 입력된 문자열을 순회하며
        for char in s:
            # 해당하는 counter 개수 하나 감소
            counter[char] -= 1
            # 이미 처리한 문자열이면 넘어가고 다시 순환
            if char in seen:
                continue
            
            # 처음 제외를 위해 stack
            # 현재 문자가 스택에 쌓인 이전 문자보다 작은데 뒤에 있으면
            # 이전 문자를 stack과 seen 에서 제거 (뒤에서 다시 넣을 것 이므로)
            while stack and char < stack[-1] and counter[stack[-1]]  > 0:
                seen.remove(stack.pop())
            # 현재문자를 stack 과 seen에 넣기
            stack.append(char)
            seen.add(char)
            
        return ''.join(stack)