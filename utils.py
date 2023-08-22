import json
from datetime import datetime


def load_json(file_name):
    """
    Открывает файл с историей банковских операций. Декодирует json в список словарей
    :param file_name: имя файла
    :return: список словарей
    """
    with open(file_name, 'r', encoding='utf-8') as f:
        operations_list = json.load(f)
    execute = []
    for i in operations_list:
        execute.append(i)
    return execute


def filter_by_state(operations_list):
    """
    :param operations_list: список совершенных операций
    :return: список операций со статусом EXECUTED
    """
    new_list = []
    for i in operations_list:
        if "state" in i and i['state'] == 'EXECUTED':
            new_list.append(i)
    return new_list


def sort_by_date(lst):
    """
    :param lst: список операций со статусом EXECUTED
    :return: список операций со статусом EXECUTED, отсортированный по дате
    """
    return sorted(lst, key=lambda x: x['date'], reverse=True)


def print_five_operations(lst):
    """
    :param lst: список операций со статусом EXECUTED, отсортированный по дате
    :return: вывод пяти последних операций со статусом EXECUTED, отсортированный по дате
    """
    five_oper = lst[:5]
    return five_oper


def get_id_info(lst, id):
    """
    :param lst: список операций со статусом EXECUTED, отсортированный по дате
    :param id: номер операции
    :return:
    """
    oper = lst[id]
    oper_id = oper['id']
    id_info = []
    for operation in lst:
        if operation['id'] == oper_id:
            id_info.append(operation)
    return id_info


def get_description(data):
    """
    :param data: данные об операции
    :return: назначение платежа
    """
    return data[0]["description"]