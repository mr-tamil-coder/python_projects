class customException(Exception):
    pass
class precedingLetterError(Exception):
    pass
class succeedingLetterError(Exception):
    pass
alphabet='k'
while True:
    try:
        foo=input("Enter an alphabet")
        if foo<alphabet:
            raise precedingLetterError
        elif foo>alphabet:
            raise succeedingLetterError
        break
    except precedingLetterError:
        print("enter alphabet is preceding one,try again!")
    except succeedingLetterError:
        print("The entered alphabet is succeeding one,try again!")
print("congratulations! you guessed it correctly")
