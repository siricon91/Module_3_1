calls = 0

def count_calls (): # создание функции 1
    global calls
    calls += 1

def string_info (string): #создание второй функции
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search): #создание третьей функции
    count_calls()
    return string.upper() in [j.upper() for j in list_to_search]


print(string_info('Petropavlovsk-Kamchatskiy'))
print(string_info('Kamchatka'))
print(is_contains('Siritsa', ['Ivanov', 'Petrov', 'SiriTsa']))
print(is_contains('Dog', ['cat', 'Doggy', 'Monkey']))
print(calls)