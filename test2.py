import pylev

def distance(var1, var2):
    print("Doing levenstien distance for ", var1 , var2)
    print("Distance should be ", pylev.levenshtein(var1, var2))
    var3 = 0
    var4 = 0
    var5 = 0

    if var1[0] == var2[0]:
        var3 = var3 + 0
    else:
        var3 = var3 + 1
    if var1[1] == var2[1]:
        var4 = var4 + 0
    else:
        var4 = var4 + 1
    if var1[2] == var2[2]:
        var5 = var5 + 0
    else:
        var5 = var5 + 1
    
#    assert(pylev.levenshtein(var1, var2), (var3+var4+var5))
    print("Result is:", var3 + var4 + var5)


distance('dog', 'cat')
distance('bat', 'cat')
#distance('', 'bob')
#distance(None, 3)
distance('asdasd', '12321asd1')


# What data structure would be better to "compare" characters? ... How does the computer store characters

