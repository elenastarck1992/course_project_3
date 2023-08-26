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


def get_date(data):
    """
    :param data: дата операции
    :return: дата операции в формате ДД.ММ.ГГ
    """
    date = data[0]['date']
    date_object = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    return date_object.strftime('%d.%m.%Y')


def get_to(accounts):
    """
    :param accounts: номер счета получателя
    :return: замаскированный счета получателя. Видны последние 4 цифры номера счета
    """
    for account in accounts:
        to = account['to']
    last_four = to[-4:]
    formatted = f'Счет **{last_four}'
    return formatted


def get_amount(transactions):
    """
    :param transactions: список словарей с операциями
    :return: сумма перевода
    """
    amounts = []
    for transaction in transactions:
        if not isinstance(transaction, dict):
            raise TypeError('Входящий параметр должен быть списком словарей')
        if "operationAmount" in transaction and isinstance(transaction["operationAmount"], dict) and "amount" in transaction["operationAmount"]:
            amounts.append(float(transaction["operationAmount"]["amount"]))
        for i in amounts:
            return i


def get_from(transactions):
    """
    :param transactions: список словарей с операциями
    :return: замаскированный номер счета/карты отправителя
    """
    to_list = []
    for transaction in transactions:
        if not isinstance(transaction, dict):
            raise TypeError('Входящий параметр должен быть списком словарей')
        if 'from' in transaction:
            to_list.append(transaction["from"])
    result = ''
    for i in to_list:
        words = i.split()
        for word in words:
            if any(char.isdigit() for char in word) and len(word) >= 16 and  len(word) <= 19:
                result += word[:4] + ' ' + word[4:6] + '**' + ' ' + '****' + ' ' + word[-4:] + ' '
            elif word.isalpha() or word.isspace():
                result += word + ' '
    return result.strip()
