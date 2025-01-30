#Nahallah Champagne

def gcd(a: int, b: int) -> int:
    
    if b == 0:
        #print ("a:", a)
        #print ("b:", b)
        return a
    else:
        print("a % b:", a % b)
        return gcd(b, a % b)

    #(54, 24)
    #a % b = 6
    #gcd (24, 6)
    #a % b = 0
    #gcd (24, 0)

# Test cases
print(gcd(54, 24))  # Expected output: 6

    #(54, 24)
    #a % b = 6
    #gcd (24, 6)
    #a % b = 0
    #gcd (24, 0)

print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1

#(54, 24)
    #a % b = 6
    #gcd (24, 6)
    #a % b = 0
    #gcd (24, 0)
