def do_stuff(num=0):
    try:
        if num:
            return int(num) + 5
        else:
            return 'please enter a number'
    except ValueError as error:
        return error


