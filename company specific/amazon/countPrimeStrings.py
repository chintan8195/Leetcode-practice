# https://forum.codebreakersacademy.com/t/amazon-oa2-countprimestrings/1013

def prime_sieve(n):
    is_prime = [True] * (n+1)
    is_prime[0], is_prime[1] = False, False
    for i in range(2, round(n**(0.5))):
        if is_prime[i]:
            for j in range(2, n // i  + 1):
                is_prime[i*j] = False
    return is_prime
def countPrimeStrings(inputString):
    MAX_PRIME = 10 ** 6
    primes = prime_sieve(MAX_PRIME)
    prime_strings = set()
    for i, is_prime in enumerate(primes):
        if is_prime:
            prime_strings.add(str(i))
    all_num_prime_strings = [0]
    for i in range(1, 1+len(inputString)):
        num_prime_strings = 0
        # Check sub problems from i to i-6
        for d in range(1, min(7, i)):
            if inputString[i-d:i] == '0':
                continue
            if inputString[i-d:i] in prime_strings:
                num_prime_strings += all_num_prime_strings[i-d]
        # check if entire substring is prime.  
        if i <= 6 and inputString[:i] in prime_strings:
            num_prime_strings += 1
        num_prime_strings %= 1000000007
        all_num_prime_strings.append(num_prime_strings)
    return all_num_prime_strings[-1]


""" 
Describe the problem statement in 2-3 sentences in English.
Describe your solution in 2-3 sentences in English.
Practice walking through the code.
Do 5 stack traces for each problem and write out the intermediate variables. Send them here in Slack.
What is the runtime of this function? And write an explanation for why that is the case.
What is the space complexity of this function? And write an explanation for why that is the case.

"""