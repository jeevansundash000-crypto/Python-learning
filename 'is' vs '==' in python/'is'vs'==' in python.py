# In python there is "is" keyboard which is used to find if any varibles suppose is none then we can write it as if a is none and if it is none then return True so we are going to find the difference betn is and == operator.
# So "is" used to compares exactly location of object in memory. While "==" compares the values.
# is and == boths are comparison operators.
a = 3
b = "3"
print(
    a is b
)  # exact location of object in memory means a and b are two different memory in named but is they contains the same ojects in memory here a contains 3 but b contains "3" which is and string so they boths have different ojects in their memory.
print(a == b)  # value
# boths are comparison operators that compares two values but boths compares differently
c = [1, 2, 3]
d = [1, 2, 3]
print(
    c is d
)  # False because although they contains the same elements in order then also python create them as a two separate list objects e.g c is obj1 while d is obj2#Think of it like two notebooks containing exactly the same notes. The notes are identical, but the notebooks themselves are different
print(c == d)  # True because they boths contains the same elements in order
# if we make diffent list having diffent index but have same element then also boths is and == gives false cause having same elements is not enough they boths have the same index

e = [2, 2, 2]
f = e
print(
    e is f
)  # here python does not create a new list instead f refers to the same list objects as e means e and f ==[2,2,2]
print(e == f)  # True as we know

q = [2, 3, 2]
w = q
w[0] = (
    200  # here w is[2,3,2] but in the place of 2 index w[0] index is 200 so w is [200,3,2] and q = w so q is also [200,3,2] therefore we modify the new list but they list are same list not different objects
)
print(q is w)  # So True
print(q == w)  # True we know

# Special use of is is checking None e.g
name = None
if name is None:
    print(
        "Value not exists"
    )  # None represents the absence of a value,and python has a single None object.
if name is not None:
    print(
        "Value exists"
    )  # here is not checks wheather two references point to different objects.
