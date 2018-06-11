from pyramda.function.curry import curry

"""This functions takes two list and creates a dictionary with it"""
zip_obj = curry(lambda key, val: dict(zip(key, val)))
