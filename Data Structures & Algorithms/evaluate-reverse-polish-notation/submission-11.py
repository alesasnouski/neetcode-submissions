class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        expr = "*/+-"
        st = []
        for t in tokens:
            if t in expr:
                print(f"{t} :: {st}")
                i1 = st.pop()
                i0 = st.pop()
                if t == "*":
                    st.append(i0 * i1)
                elif t == "/":
                    print(f"{i0}::::{i1}")
                    st.append(int(i0 / i1))
                elif t == "+":
                    st.append(i0 + i1)
                else:
                    st.append(i0 - i1)
            else:
                st.append(int(t))        

        return st[0]                    