def do_stuff(num):
    try:
        return int(num) + 5
    except ValueError as error:
        return error


