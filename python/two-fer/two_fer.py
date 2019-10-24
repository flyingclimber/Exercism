def two_fer(name=None):
    if not name or name.isspace():
        return "One for you, one for me."
    else:
        return "One for {}, one for me.".format(name)
