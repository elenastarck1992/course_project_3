from src.utils import filter_by_state, sort_by_date, get_date, get_description, get_amount, get_from, get_to, \
    print_five_operations


def test_filter_by_state():
    data = [{"state": "CANCELED"}, {"state": "EXECUTED"}]
    assert filter_by_state(data) == [{"state": "EXECUTED"}]


def test_sort_by_date():
    data = [{"date": "2018-01-26T15:40:13.413061"}, {"date": "2018-11-29T07:18:23.941293"}]
    assert sort_by_date(data) == [{"date": "2018-11-29T07:18:23.941293"}, {"date": "2018-01-26T15:40:13.413061"}, ]


def test_get_description():
    data = [{"date": "2018-11-29T07:18:23.941293", "description": "Перевод с карты на счет"}]
    assert get_description(data) == "Перевод с карты на счет"


def test_get_date():
    data = [{"date": "2018-01-26T15:40:13.413061"}, {"date": "2018-11-29T07:18:23.941293"}]
    assert get_date(data) == "26.01.2018"


def test_get_amount():
    data = [{"operationAmount": {
        "amount": "96995.73",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }}}
    ]
    assert get_amount(data) == 96995.73


def test_get_from():
    transaction = [{"from": "Счет 27248529432547658655"}]
    assert get_from(transaction) == "Счет"


def test_get_to():
    transaction = [{"to": "Maestro 3806652527413662"}]
    assert get_to(transaction) == "Счет **3662"


def test_print_five_operations():
    data = [{1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}]
    assert print_five_operations(data) == [{1}, {2}, {3}, {4}, {5}]
