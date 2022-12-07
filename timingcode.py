#timing code
import time
import timeit
def func_01(n):
    return [str(num) for num in range(n)]
func_01(10)

def func_02(n):
    return list(map(str,range(n)))
func_02(10)

#current time before
start_time = time.time()
#run code
result = func_01(1000000)
#current time after running code
end_time = time.time()
#elapsed time
elapsed_time = end_time - start_time
print(f'{elapsed_time}')


#current time before
start_time = time.time()
#run code
result = func_02(1000000)
#current time after running code
end_time = time.time()
#elapsed time
elapsed_time = end_time - start_time
print(f'{elapsed_time}')

#statement e setup em formato string
statement_01 = '''
func_01(100)
'''
setup_01 = '''
def func_01(n):
    return [str(num) for num in range(n)]
'''
timeit.timeit(statement_01,setup_01,number=100000)

statement_02 = '''
func_02(100)
'''
setup_02 = '''
def func_02(n):
    return list(map(str,range(n)))
'''
timeit.timeit(statement_02,setup_02,number=100000)


'''
%%timeit # so funciona no jupyter notebook
func_01(100)
%%timeit
func_02(100)
'''