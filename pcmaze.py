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
    print('Found path: ' + str(find_path(entrance(), entrance())))
    return


def find_path(pos, last):
    # check if we are at the end
    if last == exit():
        return True
    # loop over entrance() and exit()
    for i in range( entrance(), exit()+1):
        # check if i is pos or not connected
        if i == pos or not connected(last, i):
            continue
        # check if path is possible
        if find_path(last, i):

            return True
    return False


if __name__ == '__main__':
    main()
