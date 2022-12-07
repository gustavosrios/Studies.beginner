def mean(num_list):
    return sum(num_list) / len(num_list)
def add_five(num_list):
    return [n + 5 for n in num_list]

if __name__ == '__main__':
    print('Testing mean function')
    n_list = [10,10,10,10,10]
    correct_mean = 10
    assert(mean(n_list) == correct_mean)
    print(f'Base Number list:{n_list}, Correct Mean:{correct_mean}')
    addfive_list = [15,15,15,15,15]
    print('Testing add_five function')
    assert(add_five(n_list) == addfive_list)
    print('All tests successuful.')