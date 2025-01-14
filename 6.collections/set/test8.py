#update also inserts elements to the set
# but we are updating the set with a new set instead of single element

x = {10,20,40,50,3000,55,65}

print(x)
x.update({'abc','test',56,33})
print(x) # no order