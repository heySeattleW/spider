def walk_man():
    walks = 0

    def walk(step):
        walks += step

    return walk


class WalkMan:
    pass


f = walk_man()
print(f(2))
print(f(3))
