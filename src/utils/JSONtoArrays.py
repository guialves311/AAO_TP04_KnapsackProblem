def json_to_arrays(data):
    items = []
    values = []
    weights = []

    for item in data['items']:
        items.append(item['id'])
        values.append(item['value'])
        weights.append(item['weight'])

    return values, weights, items