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

