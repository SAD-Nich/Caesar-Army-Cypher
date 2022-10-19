print("THis is Ceajser Cupher")
def cesar(x,y):
    x = x.upper()
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    k = ""
    for letter in x:
        if letter in a:
            letterfind = (a.find(letter)-y)%26
            k = k + a[letterfind]
        else:
            k = k + letter
    return k
print(cesar("Jupxarcqv jwm Yaxpajvvrwp",9))