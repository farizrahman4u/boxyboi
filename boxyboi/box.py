def unbox(f):
    def wrapper(self, x):
        if type(x) is Box:
            x = x.value
        return f(self, x)
    return wrapper


class Box(object):

    def __init__(self, value, **kwargs):
        self.value = value
        for k,v in kwargs.items():
            setattr(self, k, v)

    def __getattr__(self, attr):
        if attr in self.__dict__:
            return self.__dict__[attr]
        return getattr(self.value, attr)

    def __len__(self):
        return len(self.value)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return repr(self.value)

    def __eq__(self, x):
        return self.value == x

    def __ne__(self, x):
        return self.value != x

    @unbox
    def __add__(self, x):
        return self.value + x

    @unbox
    def __iadd__(self, x):
        self.value += x
        return self

    @unbox
    def __radd__(self, x):
        return x + self.value

    @unbox
    def __sub__(self, x):
        return self.value - x

    @unbox
    def __isub__(self, x):
        self.value -= x
        return self

    @unbox
    def __rsub__(self, x):
        return x - self.value

    @unbox
    def __mul__(self, x):
        return self.value * x

    @unbox
    def __imul__(self, x):
        self.value *= x
        return self

    @unbox
    def __rmul__(self, x):
        return x * self.value

    @unbox
    def __floordiv__(self, x):
        return self.value // x

    @unbox
    def __ifloordiv__(self, x):
        self.value //= x
        return self

    @unbox
    def __rfloordiv__(self, x):
        return x // self.value

    @unbox
    def __truediv__(self, x):
        return self.value / x

    @unbox
    def __itruediv__(self, x):
        self.value /= x
        return self

    @unbox
    def __rtruediv__(self, x):
        return x / self.value

    @unbox
    def __div__(self, x):
        return self.value / x

    @unbox
    def __idiv__(self, x):
        self.value /= x
        return self

    @unbox
    def __rdiv__(self, x):
        return x / self.value

    @unbox
    def __mod__(self, x):
        return self.value % x

    @unbox
    def __imod__(self, x):
        self.value %= x
        return self

    @unbox
    def __rmod__(self, x):
        return x % self.value

    @unbox
    def __pow__(self, x):
        return self.value ** x

    @unbox
    def __ipow__(self, x):
        self.value **= x
        return self

    @unbox
    def __rpow__(self, x):
        return x ** self.value

    @unbox
    def __lshift__(self, x):
        return self.value << x

    @unbox
    def __ilshift__(self, x):
        self.value <<= x
        return self

    @unbox
    def __rlshift__(self, x):
        return x << self.value

    @unbox
    def __rshift__(self, x):
        return self.value >> x

    @unbox
    def __irshift__(self, x):
        self.value >>= x
        return self

    @unbox
    def __rrshift__(self, x):
        return x >> self.value

    @unbox
    def __and__(self, x):
        return self.value & x

    @unbox
    def __iand__(self, x):
        self.value &= x
        return self

    @unbox
    def __rand__(self, x):
        return x & self.value

    @unbox
    def __or__(self, x):
        return self.value | x

    @unbox
    def __ior__(self, x):
        self.value |= x
        return self

    @unbox
    def __ror__(self, x):
        return x | self.value

    @unbox
    def __xor__(self, x):
        return self.value ^ x

    @unbox
    def __ixor__(self, x):
        self.value ^= x
        return self

    @unbox
    def __rxor__(self, x):
        return x ^ self.value


    @unbox
    def __lt__(self, x):
        return self.value < x

    @unbox
    def __le__(self, x):
        return self.value <= x

    @unbox
    def __gt__(self, x):
        return self.value > x

    @unbox
    def __ge__(self, x):
        return self.value >= x

    def __neg__(self):
        return -self.value

    def __pos__(self):
        return +self.value

    def __abs__(self):
        return abs(self.value)

    def __invert__(self):
        return ~self.value

    def __complex__(self):
        return complex(self.value)

    def __int__(self):
        return int(self.value)

    def __long__(self):
        return long(self.value)

    def __float__(self):
        return float(self.value)

    def __hex__(self):
        return hex(self.value)

    def __oct__(self):
        return oct(self.value)

box = Box
