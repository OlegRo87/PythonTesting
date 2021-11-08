#
#
#
# ItemsInCart = 0
# if ItemsInCart !=2:
#     raise Exception("Products Cart count not matching")



# try except not fail test failed one
try:
    with open('filelog.txt', 'r') as reader:
        reader.read()
except:
    print('some how i reached this block because there us failure in try block')

# try except not fail test the correct one
try:
    with open('test.txt', 'r') as reader:
        reader.read()
except:
    print('some how i reached this block because there us failure in try block')

# try except not fail test the fail one with python builtin error
try:
    with open('filelog.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)


try:
    with open('filelog.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)
finally:  # no meter if fail or passed finally will do it task(shutdown)
    print('print no meter what happened')

# # without try block
# with open('filelog.txt', 'r') as reader:
#     reader.read()
