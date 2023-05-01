#string is not mutable
s="hello world"
#print(s[1]=d)
#bulit function
t=s.upper()
print(t)
m=s.lower()
print(m)
d=s.title()
print(d)
#strip function
y="   hello world   "
print(y)
r=y.strip()
print(r)
p=y.rstrip()
print(p)
b=y.lstrip()
print(b)
#split function
e="#hello#world"
k=e.split("#")
print(k)
u="mynamehs"
f=u.split("n")
print(f)
#count and find
g=s.count("o")
print(g)
v=s.find("l")
print(v)
#replace
j=s.replace("h","m")
print(j)
#escape sequence
#\n newline
#\t tab
print("Hello\nworld")
print("Hello\tworld")
print("this is a backslash:\\")
#\' single quote
#\\" double qoute
name="Ram"
live="heart"
print(f"{name} live in our{live}")