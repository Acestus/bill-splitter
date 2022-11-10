class NotInBoundsError(Exception):
    def __str__(self):
        return "There is an error!"


def check_integer(num):
    if 45 < num < 67:
        print(num)
    else:
        raise NotInBoundsError


def error_handling(num):
    try:
        check_integer(num)
    except NotInBoundsError as e:
        print(e)
