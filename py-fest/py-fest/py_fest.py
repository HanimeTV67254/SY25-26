lineup = ['Band A', 'Band B', 'Band C', 'Band D']






def main():
    print('---py--fest---')
    print('1.view lineup')
    print('2.Add band to lineup')
    print('3.move first band to end of lineup')
    print('4.remove band from lineup')
    print('5.move band to specific poiton')
    print('6.Exit')




while True:
    main()
    number = int(input ('-Enter your choice:'))
    

    if number == 1:
        print(" ")
        print(lineup)
        print(" ")


    if number == 2:
        print(" ")
        New_band = str(input('New Band:'))
        lineup.append(New_band)
        print(" ")

    if number == 3:
        print(" ")
        print(lineup[0] , "has been moved to end")
        remove = str(lineup.pop(0))
        lineup.append(remove)
        print(" ")

    if number == 4:
        print(" ")
        band_r = str(input('Band to remove:'))
        lineup.remove(band_r)
        print(" ")

    if number == 5:
        print(" ")
        band_r = str(input('Band to remove:'))
        lineup.remove(band_r)
        print(" ")

    if number == 6:
        break

        if number > 6:
            print(' ')
            print('not valid input')
            print(" ")




