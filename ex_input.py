a = int(input("input 1st unber : ")) #input함수 자료형은 문자열
b = int(input("input 2nd unber : "))
c = input("input operator(+ , *) : ")

#print(a + b)
#print("%d + %d = %d" %(a,b,a+b))
#print("1ast : %s + 2nd :%s = %s" %(a,b,a+b)) # %s는 자동으로 자료형에 맞게 출력

def add(a,b):
    return a+b
    
def multi(a,b):
    return a*b
    
if c == '+':
    result = add(a,b)
    print(result)
elif c == '*':
    result = multi(a,b)
    print(result)
else:
    pass
