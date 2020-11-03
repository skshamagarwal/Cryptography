# Checks - No. is prime or not
def isPrime(n):
	if (n <= 1):
		return False
	for i in range(2, n):
		if (n % i == 0):
			return False
	return True


# Picks a Public key
def publicKey(q, p, fi):
    x = max(q, p)
    while True:
        x += 1
        if isPrime(x):
            return x
        else:
            pass


# Calculates Private key
def privateKey(e, fi):
    d = 0.1
    k = 0
    while True:
        if d == int(d):
            return int(d)
        d = (1 + k*fi)/e
        k += 1


# Encrypting Message
def encryption(message, e, n):
    C = []
    for i in message:
        C.append((ord(i)**e) % n)
    return C


# Decrypting Message
def decryption(C, d, n):
    P = ''
    for i in C:
        P = P + (chr((i**d) % n))
    return P


# DRIVER CODE
message = input("Enter message: ")
p, q = map(int,input("Enter two prime numbers space separated (p q) :- ").split())

while not(isPrime(p)) or not(isPrime(q)):
    print("\nOne of the given input is not a prime number")
    p, q = map(int, input("Re-Enter two prime numbers space separated (p q) :- ").split())


n = p*q
fi = (p-1)*(q-1)
e = publicKey(q, p, fi)
d = privateKey(e, fi)

enc_msg = encryption(message, e, n)
dec_msg = decryption(enc_msg, d, n)

print(f"\nPublic key (e) = {e}\nPrivate key (d) = {d}")
print(f"Encrypted Message (P) = {enc_msg}")

ans = input ('\nDo you want to decrypt the above message(Y/N): ')
if ans == 'Y' or ans == 'y':
    print(f"Decrypted Message (C) = {dec_msg}")

print("\nThank You")