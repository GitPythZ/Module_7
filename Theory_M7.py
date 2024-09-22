a = "hello"
print(ord("a"))
print(ord("h"))
chars = []
for char in a:
    chars.append(ord(char))
print(chars)
s = ""
for binary_code in chars:
    s += chr(binary_code)
print(s)
# for num in range(128):
#     print(chr(num))

print(hex(ord("h")))
bb = b"\x68"
print(type(bb))
print(bb.decode())
