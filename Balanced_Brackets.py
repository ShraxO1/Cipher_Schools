from collections import deque 
def checkbalance(string):
    stack=deque()
    for i in string:
    	if i=='{' or i=='(' or i=='[':
    	    stack.append(i)
    	else:
    	    if not stack:
    	        return 'NO'
    	    temp=stack.pop()
    	    if i==']' and temp=='[':
    	        continue
    	    elif i=='}' and temp=='{':
    	        continue
    	    elif i==')' and temp=='(':
    	        continue
    	    else:
    	        return 'NO'
    if stack:
        return 'NO'
    else:
        return 'YES'
s='[{()}]'
print(checkbalance(s))
    	    