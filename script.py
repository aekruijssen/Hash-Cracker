"""
aekruijssen

IMPORTANT:
    
    To test, you must input the name of the hashes file when prompted
    
    This program utilizes the itertools, hashlib, and timeit libraries
        itertools is used for the password generation
        hashlib is used to find the hashes
        timeit is used to find the time it took to crack each password
    
    Also, passwords greater than 3 characters in length will take too 
    long to be checked, though their hashes have been checked outside of
    the password generator algorithm this program uses, and worked
"""

import itertools, hashlib, timeit
pwfile = input("Enter hashes path")
try: pwfile = open(pwfile, "r")
except: print ("\nFile not found"), quit()
start_time = timeit.default_timer()
for count in [1,2,3]:
    guesses = [''.join(i) for i in itertools.product('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*', repeat=count)]
    for guess in guesses: 
       pwfile.seek(0)
       for password in pwfile:
           if (password.__contains__(hashlib.md5(guess.encode()).hexdigest())): print (guess + "     %d" % (timeit.default_timer() - start_time))
pwfile.close()
