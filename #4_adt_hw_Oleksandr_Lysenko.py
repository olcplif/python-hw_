# 1. Define the id of next variables:
int_a = 55
print(f'Id int_a = {id(int_a)}')

str_b = 'cursor'
print(f'Id str_b = {id(str_b)}')

set_c = {1, 2, 3}
print(f'Id set_c = {id(set_c)}')

lst_d = [1, 2, 3]
print(f'Id lst_d  = {id(lst_d)}')

dict_e = {'a': 1, 'b': 2, 'c': 3}
print(f'Id dict_e = {id(dict_e)}')

# 2. Append 4 and 5 to the lst_d and define the id one more time.
lst_d.append(4)
lst_d.append(5)
print(f'Id lst_d = {id(lst_d)} ==> The ID differs after each new start of the program')

# 3. Define the type of each object from step 1.
print(f'Type int_a = {type(int_a)}')
print(f'Type str_b = {type(str_b)}')
print(f'Type set_c = {type(set_c)}')
print(f'Type lst_d  = {type(lst_d)}')
print(f'Type dict_e = {type(dict_e)}')

# 4*. Check the type of the objects by using isinstance.
print('4.')


def type_definition(obj):
    if isinstance(obj, str):
        answer = "this str type"
    elif isinstance(obj, int):
        answer = "this int type"
    elif isinstance(obj, list):
        answer = "this list type"
    elif isinstance(obj, dict):
        answer = "this dict type"
    elif isinstance(obj, set):
        answer = "this set type"
    elif isinstance(obj, tuple):
        answer = "this tuple type"
    elif isinstance(obj, float):
        answer = 'this float type'
    return answer


def name_var(**variables):
    return [v for v in variables]


print(name_var(int_a=int_a), type_definition(int_a))  # OUTPUT: ['int_a'] this int type
print(name_var(str_b=str_b), type_definition(str_b))  # OUTPUT: ['str_b'] this str type
print(name_var(set_c=set_c), type_definition(set_c))  # OUTPUT: ['set_c'] this set type
print(name_var(lst_d=lst_d), type_definition(lst_d))  # OUTPUT: ['lst_d'] this list type
print(name_var(dict_e=dict_e), type_definition(dict_e))  # OUTPUT: ['dict_e'] this dict type

print('Anna has {apples} apples and {peaches} peaches.'.format(apples=int(input("Enter apples:")), peaches=input("Enter peaches:" )))
