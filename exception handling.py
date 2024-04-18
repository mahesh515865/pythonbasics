print("starting line")
a=[11,22,33]

try:
    print(y)
except ZeroDivisionError:
    print("Exception raised due to zero devision error")
except IndexError:
    print("Exception raised due to index out of range")
except NameError:
    print("Exception raised due to undifined variable")
except:
    print("Some exception raised")
else:
    print("NO exception raised,everything worked perfectly")
finally:
    print("This is a final")
print("Outside try block")
