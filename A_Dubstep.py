s=input()
s=s.split("WUB")
for i in s:
    if i=="":
        s.remove(i)
print(" ".join(s))