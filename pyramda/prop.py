from pyramda.function.curry import curry
import builtins

@curry
def prop(name, o):
    try:
        return builtins.getattr(o, name)
    except AttributeError:
        return o[name]
