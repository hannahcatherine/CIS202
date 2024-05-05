
buying = input('do you want a muffin or a cupcake? ')
muffins = 10
cupcakes = 10

while buying != "0":
    if buying == "muffin" and muffins > 0:
        muffins = muffins -1
        if buying == "muffin" and muffins == 0:
            print ("There are no more muffins")
    if buying == "cupcake" and cupcakes >0:
        cupcakes = cupcakes -1
        if buying == "cupcake" and cupcakes == 0:
            print ("There are no more cupcakes")
    buying = input('do you want a muffin or a cupcake? ')
print ("muffins:", muffins, "cupcakes:", cupcakes)
