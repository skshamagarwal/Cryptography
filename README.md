# RSA-Algorithm

### Reading these steps will help you to understand code better:

- Choose two different Large Random Numbers i.e. p and q
- Calculate RSA Modulus i.e. n = p*q
- Calculate phi/fi which is equal to (p-1)*(q-1)
- Choose e \(public key\) such that 1 $\lt$ e $\lt$ fi and e is co-prime to fi
- Calculate d \(private key\) with the help of formulae d = \(1 mod fi\)/e

To Encrypt Plain Text into Cypher Text, we used C = P^e mod n

To Decrypt  Cypher Text into Plain Text, we used P = C^d mod n