import re

# def money from string(amount):
#     # amount is a string like "$140.75"
#     match = re.search(r'A\$(?P<dollars>\d+)\.(?P<cents>\d\d)$', amount)
#     dollars = int(match.group('dollars'))
#     cents = int(match.group('cents'))
#     return Money(dollars, cents)


def money_from_string(amount):
    match = re.search(
        r'A\$(?P<dollars>\d+)\.(?P<cents>\d\d)$', amount)
    # Adding the next two lines here
    if match is None:
        raise ValueError("Invalid amount: " + amount)
    dollars = int(match.group('dollars'))
    cents = int(match.group('cents'))
    return Money(dollars, cents)


class Money:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def __repr__(self):
        # 'Improves the default representation in stack traces.'
        return "Money({},{})".format(
            self.dollars, self.cents)
        # Plus other methods.
