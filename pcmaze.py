def connected( x, y ):
    if x > y:
        return connected( y, x )
    if (x,y) in ((1 ,5) ,(2,3) ,(3,7) ,(4,8) ,(5,6) ,(5,9) ,(6,7),(8 ,12) ,(9 ,10) ,(9 ,13) ,(10 ,11) ,(10 ,14) ,(11 ,12) ,(11 ,15),(15 ,16)):
        return True
    return False


def entrance():
    return 1


def exit():
    return 16


def main():
    print(find_path(entrance(), entrance()))
    return


def find_path(pos, last):
    if pos == exit():
        return pos
    for x in range(1, 17):
        conn = connected(pos, x)
        # Only show the path with true
        if conn is True:
            print(str(conn) + ' : ' + str(pos))
        if connected(pos, x) and x != last:
            return find_path(x, pos)


if __name__ == '__main__':
    main()
