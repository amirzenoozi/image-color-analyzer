def save_file(filename, data):
    with open(filename, 'wb') as f:
        f.write(data)