class Solution:
    def backspaceCompare(self, s ,t):
        def build(x):
            st = []
            for ch in x:
                if ch == '#':
                    if st:
                        st.pop()
                else:
                    st.append(ch)
            return st
        return build(s) == build(t)