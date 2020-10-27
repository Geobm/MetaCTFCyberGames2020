
#  Crypto Stands For Cryptography
### Problem description
Welcome to the crypto team! We help consult in a variety of areas around the security department, helping to make sure our company is using proper encryption, data storage, and data transfer mechanisms.

The data security team said they currently use something called Base64 to "encrypt" data. They want to know if that's a secure way to store sensitive data, and provided a sample of data:

`TWV0YUNURntiYXNlNjRfZW5jMGRpbmdfaXNfbjB0X3RoZV9zYW1lX2FzX2VuY3J5cHRpMG4hfQ==`

Is it secure? Can you crack it?

## Steps I followed to find the flag

This was one of the easiest ones, since the problem provides the base64 string, I could just search an online website to decode the string, but I wanted to do a script. `base64` python's  module helped me to solve this problem. So, I coded a short script that can decode base64 strings. 

I found `b64decode()` function very usefull. In addition, I tried with other base64 strings and it worked. Simply, by running the script, the flag can be printed.

![Image](https://res.cloudinary.com/dxbnpu2rx/image/upload/v1603844046/Screenshot_from_2020-10-27_13-12-42_ymmqhf.png)

The flag is, **MetaCTF{base64_enc0ding_is_n0t_the_same_as_encrypti0n!}** so, we earned 100 points.
