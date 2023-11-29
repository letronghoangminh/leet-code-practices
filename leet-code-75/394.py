class Solution:
    def decodeString(self, s: str) -> str:
        # stack_pointer = 0
        # stack = {}
        # result = ""
        
        # for i in range(len(s)):
        #   if s[i] == "[": 
        #     stack_pointer += 1
        #     stack[str(stack_pointer)]["constant"] = int(stack[str(stack_pointer)]["constant"])
        #   elif s[i] == "]":
        #     stack[str(stack_pointer)]["result"] = stack[str(stack_pointer)]["constant"] * stack[str(stack_pointer)]["chars"]
        #     stack_pointer -= 1
        #     if stack_pointer == 0:
        #       result += stack["1"]["chars"] * stack["1"]["constant"]
        #       stack.pop("1")
        #     else:
        #       print(stack)
        #       if stack[str(stack_pointer)].get("chars") is None: stack[str(stack_pointer)]["chars"] = ""
        #       stack[str(stack_pointer)]["chars"] += stack[str(stack_pointer + 1)]["result"]
        #       stack.pop(str(stack_pointer + 1))
        #   else:
        #     if s[i] >= "a" and s[i] <= "z":
        #       if stack_pointer == 0: result += s[i]
        #       elif stack[str(stack_pointer)].get("chars") is None: stack[str(stack_pointer)]["chars"] = str(s[i])
        #       else: stack[str(stack_pointer)]["chars"] += s[i]
        #     else:
        #       if stack.get(str(stack_pointer + 1)) is None:
        #         stack[str(stack_pointer + 1)] = {}
        #         stack[str(stack_pointer + 1)]["constant"] = str(s[i])
        #       else: 
        #         print(stack[str(stack_pointer + 1)]["constant"])
        #         print(s[i])
        #         print(stack)
        #         stack[str(stack_pointer + 1)]["constant"] += str(s[i])
          
        # return result
        
        stack = []
        res, num = "", 0
        
        for i in s:
          if i.isdigit():
            num = num * 10 + int(i)
          elif i == "[":
            stack.append(res)
            stack.append(num)
            res = ""
            num = 0
          elif i == "]":
            cnum = stack.pop()
            cres = stack.pop()
            res = cres + cnum * res
          else:
            res += i
        return res
        
print(Solution().decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))
          