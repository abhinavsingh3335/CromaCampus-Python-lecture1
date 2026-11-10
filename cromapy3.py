"""
6- Logical Operator
AND = if both/all inputs are True, then output is True otherwise False.
print(10>5 and 20>7)    #T
print(10>4 and 20>60)   #F
print(10>50 and 20>70)  #F

OR = if both/all inputs are False,then output is False otherwise True.
print(10>5 or 20>7)     #T
print(10>4 or 20>60)    #T
print(10>50 or 20>70)   #F

NOT = not is also called the invertor.
        not operator will work only and only with one input.
        if input is True then output is False and vice-versa.
print(not 10>5)

print(10>5 and not(10>7 or 20>5))
#True and not(True)
#True and False
#False

a = 7
b = 5
print(a and b)  #5
print(b and a)  #7

a = 7
b = 0
print(a and b)  #0
print(b and a)  #0

7- Bitwise Operator: and -> &
    or -> |
    not -> ~
    &,|,~  -(x+1)

a = 22       #10110
b = 26       #11010
print(a&b)   #10010 =>18
print(a|b)   #11110 =>30

a = 6
print(~a)   #-(6+1) => 7
a = -4
print(~a)   #-(-4+1) = 3

 ^ XOR:
 0 0 = 0
 0 1 = 1
 1 0 = 1
 1 1 = 0

a = 7        #111
b = 5        #101
print(a^b)   #010 => 2

8- Shift Operator:
    (a)Right Shift Operator , (b)Left Shift Operator

Right shift Operator:
a = 25          #11001
print(a>>1)     #1100   =>12
print(a>>2)     #110    =>6
print(a>>3)     #11     =>13

Left shift Operator:
a = 7           #111
print(a<<1)     #1110 =>14
print(a<<2)     #28
print(a<<3)     #56

=========================================================== Assignment GUESS OUTPUT===================================================
#Q1:
a = 5
b = 10
print(a<b<20)
#A<B and b<20
#True & True
#True

#Q2:
x = True
y = False
print(x+y*x)
#1+0*1
#1+0
#1

#IMPORTANT:
PEMDAS
P = paranthesis ()
E = exponential **
M = multiplication *
D = Division /
A = Addition +
S = Substraction

#Q3
print(4**0**2)
#(4**0)**2)
#1**2
#1

#Q4
a = 12       #1100
b = 5        #0101
print(a^b)   #1001 =>9

#Q5:
print((3 and 0) or (0 and 3))
#0 or 0
#0

#Q6:
Print(256 is 256)   #True
print(257 is 257)   #True

#Q7:
a = 7
print(~a+1)
#(-(7+1)+1)
#(-8+1)     #-7

#Q8:
a = True
b = False
print((a or b) and not(a and b))
#((1 | 0) & not(1 & 0))
#(True & True)      #True

#Q9:
print(10>5==True)
#(10>5) and 5==True
#True and 5==1 (False)  #False

#Q10:
print(2+3*4**2//8%3)
#2+3*16//8%3
#2+48//8%3
#2+6%3
#2+0        #2

#Q11:
print(1<<2+1)
#1<<(2+1)
#1<<3
#8

Q12:
a = 3
b = 2
a* = b+1
print(a)
#a = a*(b+1)
#3*(2+1)
#3*3    #9

#Q13:
print(3 < 5 > 2 == 2)
#(3<5)&(5<2)&(2==2)
#True & True & True
#True

#Q14:
print(10 // 3 * 3 + 1 % 3)
#3*3 + 1%3
#9+1
#10

#Q15:
x = 10   #01010
y = 20   #10100
print(x & y | x ^ y)
#10&20 | 10^20
#0 | 30
#30

#Q16:
a = True
b = False
print(a & b or a ^ b)
#True & False | True ^ False
#False | True
#True

#Q17:
x = 8
print(x >> 1 << 2)
#(8>>1)<<2
#4<<2     #16

#Q18:
print(5+True*False+not False)
#5+0+1 #6

#Q19
print((not 0) * (False or 1 ))
#(1 * 1)
# 1

"""
#Q20:
print(4+3*2**2//2-1)
#4+3*4//2-1
#4+12//2-1
#4+6-1
#4+5          #9




