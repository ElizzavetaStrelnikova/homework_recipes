'''
Задача N1
'''
recipes_dict = {}
with open('recipes.txt', 'r', encoding='utf-8') as f:
    i = 0

    for line in f.readlines():
        line = line.replace('\n', '')
        if i == 0:  # первая строка блока - название блюда
            key = line
            i += 1
        elif i == 1:  # кол-во ингредиентов
            ing_count = int(line)
            i += 1
        elif line == '':  # конец блока
            i = 0
        else:  # обработка ингредиента
            if key not in recipes_dict.keys():
                recipes_dict[key] = []
            # print(line.split(' | '))
            recipes_dict[key].append(
                {
                    'ingredient_name': line.split(' | ')[0],
                    'quantity': int(line.split(' | ')[1]),
                    'measure': line.split(' | ')[2],
                })

print(recipes_dict)


'''
Задача N2
'''
def get_shop_list_by_dishes(dishes, person_count):
    result_dict = {}
    for dish in dishes:
        if dish not in recipes_dict.keys():
            raise Exception('Нет блюда в списке')
        else:
            for ing in recipes_dict[dish]:
                if ing['ingredient_name'] not in result_dict.keys():
                    result_dict[ing['ingredient_name']] = {
                        'measure': ing['measure'],
                        'quantity': ing['quantity'] * person_count
                    }
                else:
                    result_dict[ing['ingredient_name']]['quantity'] += ing['quantity'] * person_count

    return result_dict


print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))



