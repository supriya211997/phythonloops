# iteration over a list
print ("list iteration")
t = ["bajaj","auto","limited"]
for i in t:
	print(i)
#iteration over a  tuple (immutable)
print ("\n tuple iteration")
t = ("bajaj","auto","limied")
for i in t:
	print(i)
#iteration over a dictionary
print("\n dictionary iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 456
for i in d:
    print("%s %d" %(i, d[i]))
