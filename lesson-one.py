from mimetypes import init


x = "programmer" #x = x is globale
def foo():
    x = "xxxx" #x is local
    print("hello mehdi"+ " " +  x)

foo()
## out of function

print(x)


#-------------------------------------------------------------------#


def myfunc():
    global x
    x = "python"
    print(x)
    
myfunc()
print(x)

#-----------------------------------------------#
x = "awesome"
def bar():
    global x
    x = "fantastic"
bar()

print("python is " + x )


#------------------------------------------------#
# bin()
# abs()
# alter()
# if
# in
# is
# bool
# True
# False
# enumerate()
# zip()
# id()
# type()
# print()
# vars()
# round()
# range()
# all()
# any()
# __import__()
# tuple()
# open()
# set()
# setattr()
# slice()
# str()
# float()
# format()
# filter()
# super()
# locals()

# git init
# git add .
# git commit -m "explanation"
# git push origin master


# mahdy.mohseni09022587508@gmail.com
# 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