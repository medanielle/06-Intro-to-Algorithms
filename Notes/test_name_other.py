import test_name_main

print(f'Other Module: {__name__}')

# so the file you are running is considered __main__, while the other is its file name
""" Output:
Original file: test_name_main
Not in Main
Other Module: __main__
"""