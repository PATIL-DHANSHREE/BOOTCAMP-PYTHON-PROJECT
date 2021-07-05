#1) WRITE A PROGRAM IN PYTHON TO GENERATE MD5 OF STRING DATA.

print("DISPLAY HERE GENERATED MD5 OF STRING DATA")
print("")
import hashlib
print(hashlib.md5(b"HELLO WORLD").hexdigest())
print(hashlib.md5("HELLO WORLD".encode('utf-8')).hexdigest())

#2) WRITE A PROGRAM IN PYTHON TO GENERATE HASHES OF STRING DATA USING 3 ALGORITHMS FROM HASHLIB.

print("HASHLIB ALGORITHMS")
print("")
import hashlib
print(hashlib.algorithms_available)
