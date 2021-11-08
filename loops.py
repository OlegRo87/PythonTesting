# k = 0
# for i in range(1, 6):
#     k = k + i
# print(k)
#
#
# for i in range(1, 10, 2):  # 2 = jump 1,3,5...
#     print(i)

# it = 10
#
# while it > 1:
#     if it == 3:
#         break
#     print(it)
#     it = it - 1
# print('loop done')

it = 10

while it > 1:
    if it == 9:
        it = it - 1
        continue
    if it == 3:
        break
    print(it)
    it = it - 1
print('loop done')