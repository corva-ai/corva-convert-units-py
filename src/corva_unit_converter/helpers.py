
def reverse_object(data):
    return {value.lower(): key for key, values in data.items() for value in values}


def get_aliases(measure):
    return [alias for unit in measure for alias in measure[unit]['aliases']]
