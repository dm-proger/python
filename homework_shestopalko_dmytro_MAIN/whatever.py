# def function():
#     k = 0
#     for i in range(10):
#         for j in range(3):
#             k = k + i
#         print(i)
#     print(k)
#
# function()
# I can not understand this code! сума потрійних сум

x = 10
for i in [1,2,3,4,5]:
    if i % 2 == 0:
        break
    x -= i
else:
    x = 10
print(x)
