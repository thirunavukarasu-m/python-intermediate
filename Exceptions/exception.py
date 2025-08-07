try:
    # a  = 5 + 'as'
    a = 10+10

except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print("error happened", e)
else:
    # Runs when there is no exception
    print("All good")
finally:
    # Runs at the end of everything
    # used for cleanup
    print("finally")
x = 0
assert(x>=0), 'x should be positive'

