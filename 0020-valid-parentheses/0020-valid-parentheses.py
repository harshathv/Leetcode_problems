class Solution:
    def isValid(self, s: str) -> bool:
        st:list[str]=[]
        for ch in s:
            if ch=='(' or ch=="{" or ch=="[":
                st.append(ch)
                continue
            if len(st)==0:
                return False
            top_stack=st[-1]
            if ch==")" and top_stack!="(":
                return False
            if ch=="}" and top_stack!="{":
                return False
            if ch=="]" and top_stack!="[":
                return False
            st.pop()
        return len(st)==0

        