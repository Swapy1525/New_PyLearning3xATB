#OverflowError: math range error
#- can be handled by exception


# import math
# math.exp(1000)      #OverflowError: math range error

try:
    import math
    math.exp(1000)
except Exception as e:
    print(e)
#got math range error exception





