try:
    x = 7 / 0
except Exception as e:
    print(e)
finally:
    print('inside finally')

    # raise FileNotFoundException('not found') like throw new Error('bad') in JS