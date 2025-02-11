class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        s = []
        for i in tokens:
            if i not in "+-*/":
                s.append(int(i))
            else:
                n2 = s.pop()
                n1 = s.pop()
                if i == "+":
                    s.append(n1+n2)
                elif i == "-":
                    s.append(n1-n2)
                elif i == "/":
                    s.append(int(float(n1)/n2))
                else:
                    s.append(n1*n2)
        return s.pop()


        
