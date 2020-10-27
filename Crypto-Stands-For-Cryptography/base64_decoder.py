import base64

b64_message = 'TWV0YUNURntiYXNlNjRfZW5jMGRpbmdfaXNfbjB0X3RoZV9zYW1lX2FzX2VuY3J5cHRpMG4hfQ=='
base64_bytes = b64_message.encode('ascii') #encode base64 to ascii
message_bytes = base64.b64decode(base64_bytes) # found this exceptional b64decode() python function 
message = message_bytes.decode('ascii')

print(message)
