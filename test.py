
var1 = 'dog'
var2 = 'cat'
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

print("The levenshtien distance is ", var3+var4+var5)
