from pprint import pprint


def read_recipes():
    recipe_dict = {}

    with open('recipes.txt', encoding='utf-8') as f:
        while True:
            dish_name = f.readline().strip()
            recipe_dict[dish_name] = []

            ingredients_count = int(f.readline().strip())

            for i in range(ingredients_count):
                ingredient, quantity, measure = f.readline().strip().split(' | ')
                quantity_dict = {'ingredient_name': ingredient, 'quantity': int(quantity), 'measure': measure}
                recipe_dict[dish_name].append(quantity_dict)

            if f.readline() == '':
                break

    return recipe_dict


def get_shop_list_by_dishes(dishes_list, person_count=1):
    shopping_list = {}

    #не  придумал как получить в функции словарь, не передавая через параметры и глобальные данные
    recipes_dict = read_recipes()

    for dish in dishes_list:
        ingredients = recipes_dict[dish]

        for ingredient in ingredients:

            name = ingredient['ingredient_name']
            measure = ingredient['measure']
            quantity = ingredient['quantity']

            if name in shopping_list.keys():
                shopping_list[name]['quantity'] += quantity * person_count
            else:
                shopping_list[name] = { 'measure': measure, 'quantity': quantity * person_count }

    return shopping_list


def main():
    # recipes_dict = read_recipes()
    # pprint(recipes_dict)

    dishes_list = ['Фахитос', 'Тушеный картофель']
    shopping_list = get_shop_list_by_dishes(dishes_list, 3)
    pprint(shopping_list)


if __name__ == '__main__':
    main()

