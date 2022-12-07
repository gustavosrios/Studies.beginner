'''
def hello(name):
    print('Hello func has been activated!')
    def greet():
        return f'You are Welcome to the Hello function!'
    def deny():
        return f'Access denied.'
    print('Requesting access...')
    if name == 'Gustavo':
        return deny
    else:
        return greet
hello_func = hello('Gustavo')
#print(hello('Gustavo'))
print(hello_func())
def hola():
    def que_tal():
        return 'Hola que tal'
    return que_tal   # dont need () 
hola_func = hola()
def some_def_func():
    return f'hi from other func'
def other(some_def_func):
    print('Other code runs here')
    print(some_def_func())
other_func = other(some_def_func)
'''
def sum_func():
    return 10+20+30+40
def exp_func(sum_func):
    return f'{sum_func ** 2}'
one_func = sum_func
two_funcs = exp_func(sum_func)


def exp_func():
    x = sum_func()
    return  sum_func() ** 2
two_funcs = exp_func
#print(two_funcs())

def math_func(decorated_func):
    def sum_func():
        return 1 + decorated_func()
    return sum_func
def decorated_func():
    return 90*11111
func_math_decorator = math_func(decorated_func)
print(func_math_decorator())
@math_func
def decorated_func():
    return 90*10000
decorated_func()

#decorator
def new_decorator(func_needs_decorator):
    def wrap_func():
        print('Some extra code, before the func used as argument:')
        func_needs_decorator()  # recebe func_needs_decorator()
        print('Some extra code, after the func used as argument')
    return wrap_func
def func_needs_decorator():
    print('im being used as argument for the decorator')
nova_funcao_decorada = new_decorator(func_needs_decorator) #executa wrap_func com func_needs_decorator de argumento no meio
nova_funcao_decorada() 