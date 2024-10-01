# Method returns true if n is a Happy Number
def numSquareSum(n):
    num = 0
    while(n):
        digit = n % 10
        num = num + digit*digit
        n = n // 10
    return num

def isHappyNumber(n):
    st = set()
    while (1):
        n = numSquareSum(n)
        if (n == 1):
            return True
        if n in st:
            return False
        st.add(n)

# Print all Happy Numbers between 1 and 100
for i in range(1, 101):
    if isHappyNumber(i):
        print(i, end=" ")
