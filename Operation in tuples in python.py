tup = (1,2,3)
print(type(tup),tup)
tup = (1,2)
print(type(tup),tup)
tup = (1)#python didn't know this is tuples
print(type(tup),tup)
tup = (1,)#comma should be include inorder to make it's tuples
print(type(tup),tup)
tuple1 = (1,2,"jeevan",True)
tuple2 = (3.0,8,0,"code")
print(tuple1),print(tuple2)
a = ((1,2),(3,4),"jeevan")#tuples inside tuples can be possible
print(a)
m = ("kenish","jeevan")
print(m if m==m else 'No')
#we can only do indexing and counting but while slicing a new tuple form no changes in first one
#slicing is possible but slicing result new tuple 
tup2 = tuple1[1:3]#tup2 and tuple2 are completely different varables
print(tup2)
print(tuple2[0:])
#we can change tuple indirectly by converting it into list and then changing it and then again converting it into tuple
##Convering tuple into list by indirectly changing its elements
countries = ("Nepal","india","china",1,2,3)
world = list(countries)#countries is in world variable but in list form
world.pop(3)#removing 3 indexing elements
world.append("USA")#adding new element in list
world[2] = "pakistan"#changing 2 indexing element
world.remove("Nepal")#removing element by name
world.insert(4,6)#inserting new element in 4 indexing not removing  any elements in 4 indexing 
countries = tuple(world)#converting list into tuple by changing its elements
# print(countries)
##Merge we can merge two tuples into one tuple by using + operator
add = (1,2,2,0,0,1,0,9,5) 
sub = ("jeevan","kenish")
mul = (2,6,8)
merge = add + mul#we can merge two tuples by using + operator only
# print(merge)
# print(add.index(0,3,8))#indxing




                    