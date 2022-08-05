dict={1:'xyz',2:'abc'}
print(dict)
l1=list(dict)
print(l1)
def disp(**d):
    print(d["a"]+" "+d['b']+" "+d["c"])

disp(a="xyz",
    b="8",
    c="ldh")