#Saw an anime with a mantis shrimp so im gonna build something abous mantis shrimps.
#idk I feel like practicing writing a binary search. Ill search for the index of a mantis shrimps punch strength





target = 15 #mantis shrimp punch strength is 1500 N
pStr = [3, 5, 7, 8, 9, 10, 12, 13, 15] #Newtons per strike *100
l, r = 0, len(pStr) - 1
ind = 0
while l <= r:
    m = (l + r)//2
    if target == pStr[m]:
        ind = m
        break
    elif target > pStr[m]:
        l = m + 1
    elif target <= pStr[m]:
        r = m - 1

print(ind)

