if __name__ == "__main__":

    def print_list():
        list1 = []
        single = ['1']
        double = [['2']]
    
        string = 'hello'

        num_list_1 = [1, 2, 3, 4]

        num_list_2 = [2, 3, 5]
        two_d_list = [[1, 2, 4], [1, 5, 6]]
        
        print(f'{list1} + {single} =', list1 + single)
        print(f'{list1} + {double} =', list1 + double)
        print(f'{list1} + {list1} =', list1 + list1)
        print(f'{single} + {double} =', single + double)
        print(f'{double} + {double} =', double + double)
        print(f'{single} * {single} = TypeError: can\'t multiply sequence by non-int of type list')
        print(f'{list1} + {string} = TypeError: can only concatenate list (not "str") to list')
        average_of_list = list_average(two_d_list)

        print(f'{two_d_list}')
        print(f'{average_of_list}')

    def list_average(two_d_list):
        list_ = []
        for list in two_d_list:
            sum = 0
            for num in list:
                sum += num
            list = sum / len(list)
            list_.append(list)
        return two_d_list
    
    def print_string():
        letters = 'abcdef'
        numbers = '123456'
        print(letters[0:8])
        print(numbers[0:2])


    def main():
        print_list()
        print_string()
        print("Main function is running.")


    main()