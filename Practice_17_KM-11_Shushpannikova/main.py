import exp_root.exponentiation
import exp_root.root
import factorial.factorial 
import logarithm.logarithm
from enum import Enum
from inspect import signature
print()

class VariableOfInputing(Enum):
    Ask = 1
    Function = 2
    Data = 3

exponentiation_list=dir(exp_root.exponentiation)[8:]
root_list = dir(exp_root.root)[8:]
factorial_list = dir(factorial.factorial)[8:]
logarithm_list = dir(logarithm.logarithm)[8:-1]

def module_checker(func, exp = exponentiation_list, roo = root_list, fac = factorial_list, log = logarithm_list):
    if func in exp: return 'exp_root.exponentiation.'
    elif func in roo: return 'exp_root.root.'
    elif func in fac: return 'factorial.factorial.'
    else: return 'logarithm.logarithm.'





def is_correct_input(reaction, situation, all_funk_list=[]):

    if situation == VariableOfInputing.Ask:
        if "yes" in reaction or "no" in reaction:
            return reaction
        else:
            not_correct_input = True
            while not_correct_input:
                print('Please, write yes or no.')
                reaction = input('yes or no: ')
                if "yes" in reaction or "no" in reaction:
                    return reaction

    elif situation == VariableOfInputing.Function:
        for funk in all_funk_list:
            if funk in reaction:
                return funk
        if funk == all_funk_list[len(all_funk_list)-1]:
            bad_situation = True
            while bad_situation:
                print(f'Please, choose function from list: {all_funk_list}')
                reaction = input('your function is: ')
                for funk in all_funk_list:
                    if funk in reaction:
                        return funk

    elif situation == VariableOfInputing.Data:
        func = reaction
        sig = str(signature(func))[1:-1]
        if len(sig)!=0:
            if sig.count(',')==0:
                sig=1
            else:
                sig=sig.count(',')+1
        else:
            sig=0
        try:
            if sig==0:
                result = func()
            print('your data is: ', end='')
            data = list(map(float, input().split()))
            if sig == len(data):
                if sig == 1:
                    result = func(data[0])
                elif sig == 2:
                    result = func(data[0], data[1])
                elif sig == 3:
                    result = func(data[0], data[1], data[2])
                else:
                    return "Function has too many arguments. Try change 68 line in main.py"
            else:
                print(f'Invalid inputing. You should write {sig} numbers.')
                return is_correct_input(reaction, situation)
            if type(result) is str:
                print('Invalid inputing. Write other numbers.')
                return is_correct_input(reaction, situation)
            else:
                return result
        except:
            print('Invalid inputing. Write only numbers.')
            return is_correct_input(reaction, situation)







def funk_list_maker():
    all_funk_list=[]
    all_funk_list.extend(dir(exp_root.exponentiation)[8:])
    all_funk_list.extend(dir(exp_root.root)[8:])
    all_funk_list.extend(dir(factorial.factorial)[8:]) 
    all_funk_list.extend(dir(logarithm.logarithm)[8:-1])
    return all_funk_list





def main():
    print('Do you want to exit?')
    reaction = is_correct_input(input('yes or no: '), situation = VariableOfInputing.Ask)
    if "no" in reaction:
        all_funk = funk_list_maker()

        print(f'Choose one of this functions: {all_funk}')
        reaction = is_correct_input(input('your function is: '), situation = VariableOfInputing.Function, all_funk_list= all_funk)

        func = eval(module_checker(reaction)+reaction)

        print(f"Write Your data for {reaction} function.") 
        data =  is_correct_input(func, situation = VariableOfInputing.Data)
        print(f'Result is: {data}')
        print('-------------------')
        return main()
    else:
        print('Bye Bye')
    



if __name__ == '__main__':
    main()
