infix = "a/b*c+c/d^4"
ranks = {"=":0,"-":0,"*":1,"/":1,"^":4}
stack=[]
postfix = ""

for token in infix:
    if token in ranks:
        if not stack:
            stack.append(token)
        else:
            while True:
                if ranks[stack[-1]]<ranks[token]:
                    stack.append(token)
                    break
                else:
                    postfix=postfix+stack.pop()
                if not stack:
                    stack.append(token)
                    break
    else:
        postfix=postfix+token
while stack:
    postfix=postfix+stack.pop()

print(postfix)




'''infix= "a*b+c/c*d^2"
ranks={"+":0,"-":0,"*":1,"/":1,"^":2}
stack=[]
postfix=""

for token in infix:
    if token in ranks:
        if not stack:
            stack.append(token)
        else:
            while True:
                if ranks[stack[-1]]<ranks[token]:
                    stack.append(token)
                    break
                else:
                    postfix=postfix+stack.pop()
                if not stack:
                    stack.append(token)
                    break
    else:
        postfix=postfix+token
while stack:
    postfix=postfix+stack.pop()
print(postfix)'''





'''infix="a+b*c/d^2"
ranks={"+":0,"-":0,"*":1,"/":1,"^":2}
stack=[]
postfix=""
for token in infix:
    if token in ranks:
        if not stack:
            stack.append(token)
        else:
            while True:
                if ranks[stack[-1]]<ranks[token]:
                    stack.append(token)
                    break
                else:
                    postfix= postfix+stack.pop()
                if not stack:
                    stack.append(token)
                    break
    else:
        postfix = postfix+token
while stack:
    postfix = postfix+stack.pop()
print(postfix)'''