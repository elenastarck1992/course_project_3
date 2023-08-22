from utils import *
from config import file_name


def main():
    list_oper =  load_json(file_name)
    print(list_oper)
    new_c = filter_by_state(list_oper)
    print(new_c)
    sort_data = sort_by_date(new_c)
    print(sort_data)
    get_five = print_five_operations(sort_data)
    print(get_five)
    for i in range(5):
        info = get_id_info(get_five, i-1)
        print(f'{get_date(info)} {get_description(info)} \n{get_from(info)} -> {get_to(info)} \n{get_amount(info)}')


if __name__ == '__main__':
    main()
