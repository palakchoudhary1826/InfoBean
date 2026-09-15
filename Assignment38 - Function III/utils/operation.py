def display():
    print("""
----------------------------------------
       NUMBER ANALYSIS SYSTEM
----------------------------------------

1. Check Perfect Number
2. Check Palindrome Number
3. Check Strong Number
4. Check Armstrong Number
5. Check Prime Number
6. Check Even or Odd
7. Find Factorial
8. Find Sum of Digits
9. Reverse a Number
10. Find Number of Digits
11. Check Automorphic Number
12. Check Neon Number
13. Check Spy Number
14. Check Harshad Number
15. Exit
          """)
    
def perfect_num(n):
    
    t=n
    i=1
    sum=0
    while i<n:
        if n%i==0:
            sum+=i
        i+=1
    
    if sum==t:
        return f"{t} Perfect Number"
    else:
        return f"{t} Not Perfect Number"
    
def palindrome_num(n):
    rev=0
    t=n
    while n>0:
        d=n%10
        rev=rev*10+d
        n//=10

    if rev==t:
        return f"{t} is palindrome"
    else:
        return f"{t} is not palindrome"

def Strong_num(n):
    t=n
    sum=0
    
    while n>0:
        d=n%10
        i=1
        p=1
        while i<=d:
            p*=i
            i+=1
        
        sum+=p
        n//=10

    if sum==t:
        return f"{t} is strong number"
    else:
        return f"{t} is not strong number"

def armstrong_num(n):
    t=n
    pow=len(str(n))
    sum=0

    while n>0:
        
        d=n%10
        sum+=(d**pow)
        n//=10

    if sum==t:
        return f"{t} is ArmStrong Number"
    else:
        return f"{t} is not ArmStrong Number"

def prime_num(n):

    if n<=1:
        return f"{n} is not prime number"
    else:
        prime=True
        for i in range(2,int((n**0.5)+1)):
            if n%i==0:
                prime=False
                break
        if prime:
            return f"{n} is prime "
        else:
            return f"{n} is non prime"

def check_even_odd(n):
    if n%2==0:
        return f"{n} is even"
    else:
        return f"{n} is odd"

def factorial(n):

    if n==1 or n==0:
        return 1

    return n*factorial(n-1) 

def sum_of_digit(n,sum):
    if n==0:
        return sum
    sum+=n%10
    return sum_of_digit(n//10,sum)

def reverse_num(n,rev):
    if n==0:
        return rev

    rev=rev*10+n%10
    return reverse_num(n//10,rev)  
    
def count_num(n,count):
    if n==0:
        return count
    count+=1
    return count_num(n//10,count)

def automorphic(n):
    sq=(n**2)
    last=sq%(10**len(str(n)))
    print(last)

    if last==n:
        return f"{n} is automorphic"
    else:
        return f"{n} is not automorphic" 
    
def neon_num(n):
    sq=n**2
    sum=0
    t=sq

    while sq>0:
        d=sq%10
        sum+=d
        sq//=10

    if sum==n:
        print(f"{n} is Neon Number")
    else:
        print(f"{n} is not Neon Number")


def spy_num(n):
        t=n
        p=1
        sum=0

        while n>0:
            d=n%10
            p*=d
            sum+=d
            n//=10
        
        if sum==p:
            print(f"{t} is spy number")
        else:
            print(f"{t} is not spy number")

        
    

def harsh_num(n):
    t=n
    sum=0

    while n>0:
        d=n%10
        sum+=d
        n//=10

    if t%sum==0:
        print(f"{t} is harshed Number")
    else:
        print(f"{t} is not harshad Number")
