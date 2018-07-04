def juxt(fs):
    return lambda *args: [f(*args) for f in fs]
