from src.utils import *
from config import file_name


def main():
    list_oper = load_json(file_name)
    new_c = filter_by_state(list_oper)
    sort_data = sort_by_date(new_c)
    get_five = print_five_operations(sort_data)
    for i in range(5):
        info = get_id_info(get_five, i-1)
        print(f'{get_date(info)} {get_description(info)} \n{get_from(info)} -> {get_to(info)} \n{get_amount(info)}')


if __name__ == '__main__':
    main()
