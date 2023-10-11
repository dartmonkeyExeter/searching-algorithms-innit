from math import trunc


def insertion_sort(name_list):
    for i in range(1, len(name_list)):
        key = name_list[i]
        j = i - 1
        while j >= 0 and key < name_list[j]:
            name_list[j + 1] = name_list[j]
            j -= 1
        name_list[j + 1] = key
    return name_list

def func():
    name_list = []
    while True:
        user_input = input('do you wanna (a)dd or (s)earch\n')
        if user_input == 'a':
            name_to_add = input('what name do you wanna add?\n').lower()
            name_list.append(name_to_add)
        elif user_input == 's':
            if not name_list:
                print('no names in list')
                continue
            name_list = insertion_sort(name_list)
            maximum = len(name_list)
            minimum = 1
            name_to_find = input('what name do you want to find?\n').lower()
            current_guess = trunc(maximum / 2)
            count = 1
            list(set(name_list))
            while name_list[current_guess] != name_to_find:
                if current_guess == 0:
                    print('not in list')
                    break
                if name_list[current_guess] > name_to_find:
                    maximum = current_guess - 1
                elif name_list[current_guess] < name_to_find:
                    minimum = current_guess + 1
                current_guess = trunc((maximum + minimum) / 2)
                count += 1
            print(f'that name is located at position {current_guess + 1}')
        else:
            print('invalid input')

def main():
    func()


if __name__ == '__main__':
    main()
