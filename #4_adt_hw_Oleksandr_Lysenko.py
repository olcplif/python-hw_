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

# 2. Append 4 and 5 to the lst_d and define the id one more time. ==> ID unmuteble
lst_d.append(4)
lst_d.append(5)
print(f'Id lst_d  = {id(lst_d)} ==> ID unmuteble')

# 3. Define the type of each object from step 1.
print(f'Type int_a = {type(int_a)}')
print(f'Type str_b = {type(str_b)}')
print(f'Type set_c = {type(set_c)}')
print(f'Type lst_d  = {type(lst_d)}')
print(f'Type dict_e = {type(dict_e)}')

# 4*. Check the type of the objects by using isinstance.
print('int_a is int => ', isinstance(int_a, int))
print('str_b is str => ', isinstance(str_b, str))
print('set_c is set =>',isinstance(set_c, set))
print('lst_d is list => ',isinstance(lst_d, list))
print('dict_e is dict => ',isinstance(dict_e, dict))

