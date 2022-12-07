import useful_functions as uf
scores = []
while True:
    try:
        if len(scores) < 5:      
            input_scores = int(input('Type your five scores:'))
            scores.append(input_scores)
        else:
            break
    except:
        print('Must be a number!')
    finally:
        print(f'{input_scores} is the last number you choose')
print('Valid score numbers! Calculating...')
mean = uf.mean(scores)
deviant_mean = uf.add_five(scores)
new_mean = uf.mean(deviant_mean)
print(f'Scores:{scores}')
print("-----------------------------------------------------------")
print(f'Mean: {mean}, New Mean:{new_mean}')
print("-----------------------------------------------------------")
print(__name__)
print(uf.__name__)