from enum import Enum


class EnumTest(Enum):
    YELLOW = 1
    BLACK = 2


a = 1

if EnumTest(a) == EnumTest.YELLOW:
    print("true")
else:
    print("false")