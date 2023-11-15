# TODO решите задачу
import json
def task(filename) -> float:
    with open(filename, 'r') as file:
        data = json.load(file)
    product_sum = 0
    for item in data:
        score = item.get('score', 0)
        weight = item.get('weight', 0)
        product_sum += score * weight

    print(round(product_sum, 3))



task('input.json')
