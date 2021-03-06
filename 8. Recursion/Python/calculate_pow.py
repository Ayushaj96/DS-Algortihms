'''
input a, b and calculate a^b
method 1 : complexity o(b)
method 2 : complexity o(log b)
'''
# method 1
def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b-1)

# method 2
def fast_power(a, b):
    if b == 0:
        return 1
    
    small_ans = fast_power(a, b//2)
    small_ans *= small_ans              # P(x, n) = P(x, n/2) * P(x, n/2)

    if b & 1:                           # if n is odd then P(x, n/2) * P(x, n/2) * x
        return a * small_ans
    
    return small_ans

def main():
    a = 3
    b = 5
    print(power(a, b))
    print(fast_power(a, b))

main()