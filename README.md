# Correspondentia

Python library to map correspondence tables in different formats to data structures.

A quick example:

    from correspondentia import match_fields

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

    list(match_fields(my_data, numbers_to_names, "count"))
    > [{'count': 'one', 'name': 'foo'},
       {'count': 'two', 'name': 'bar', 'correspondentia_allocation': 0.5},
       {'count': 'deux', 'name': 'bar', 'correspondentia_allocation': 0.5}]

## Installation

Installation via normal pathways; currently has no dependencies.

## Contributing

Follow standard fork/pull-request procedure.
