def first_function():
    print("sss")

first_function()
def paramater(a) :
    if(a == 0):
        print('dmmm 0 ')
    else:
        print("not 0 ")
def functionreturn(a):
   print("cascs")
   return a
paramater(0)
ok = functionreturn("casckjas")
print("print ok" , ok)
def giaithua(number):
    if ( number < 2):
        return number
    else:
        return giaithua(number-1) * number
result  = giaithua(17)
print('resutl ' , result)
# def buffersort(array):
#     for(item in array):

x = lambda a , b : a* b
resultLambda  = x(9 , 8)
print resultLambda
y = lambda a, b, c, d : a * b  *c /d


