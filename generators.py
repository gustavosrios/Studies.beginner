#generators
def create_cubes(n):
    result = []
    for x in range(0,n):
        result.append(x**3)
    return result
#create_cubes(10)  
for x in create_cubes(10):
    print(x)