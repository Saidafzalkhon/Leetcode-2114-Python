sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
son = 0 
for i in sentences:
    s = list(i.split())
    if son<len(s):
        son = len(s)
print(son)