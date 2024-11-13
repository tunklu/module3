from operator import length_hint

calls = 0

def count_calls ():
    global calls
    calls+=1

def string_info (string):
    count_calls()
    inforamtion = len(string), string.upper(), string.lower()
    return inforamtion

def is_contains (string, list_to_search):
    count_calls()
    return string.upper() in [s.upper() for s in list_to_search]

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBan
print(is_contains('cycle', ['recycle', 'cyclic'])) # No matches
print(calls)