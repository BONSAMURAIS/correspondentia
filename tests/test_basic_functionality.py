from correspondentia import match_fields
from correspondentia.disaggregation import equal_split


def test_default_disaggregation():
    numbers_to_names = {
        1: [{"value": "one", "type": "exact"}],
        2: [{"value": "two", "weight": 0.75, "type": "disaggregation"},
            {"value": "deux", "weight": 0.25, "type": "disaggregation"}],
    }

    my_data = [{
        'count': 1,
        'name': 'foo'
    }, {
        'count': 2,
        'name': 'bar'
    }]

    expected = [
        {'count': 'one', 'name': 'foo'},
        {'count': 'two', 'name': 'bar', 'correspondentia_allocation': 0.75},
        {'count': 'deux', 'name': 'bar', 'correspondentia_allocation': 0.25}
    ]

    assert list(match_fields(my_data, numbers_to_names, "count")) == expected

def test_equal_split():
    numbers_to_names = {
        1: [{"value": "one", "type": "exact"}],
        2: [{"value": "two", "weight": 0.5, "type": "disaggregation"},
            {"value": "deux", "weight": 0.5, "type": "disaggregation"}],
    }

    my_data = [{
        'count': 1,
        'name': 'foo'
    }, {
        'count': 2,
        'name': 'bar'
    }]

    expected = [
        {'count': 'one', 'name': 'foo'},
        {'count': 'two', 'name': 'bar', 'correspondentia_allocation': 0.5},
        {'count': 'deux', 'name': 'bar', 'correspondentia_allocation': 0.5}
    ]

    assert list(match_fields(my_data, numbers_to_names, "count",
                             split_function=equal_split)) == expected
