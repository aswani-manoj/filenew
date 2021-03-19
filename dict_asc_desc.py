dic={'sree':20,'aru':20,'nandu':25}
l=list(dic.items())
l.sort()
d=dict(l)
print("the ascending order is:",d)
l=list(dic.items())
l.sort(reverse=True)
d=dict(l)
print("the descending order is:",d)
