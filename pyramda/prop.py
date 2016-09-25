from pyramda.function.curry import curry

@curry
def prop(x, obj):
    if isinstance(obj, dict):
        return obj[x]
    return getattr(obj, x)
