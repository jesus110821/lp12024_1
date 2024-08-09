while True:
    protesto = input()
    try:
        if protesto == '0':
            print('vai ter copa!')
        else:
            print('vai ter duas!')
    except EOFError:
        break