"""
Исходные данные для тестов:
test1 = {"temperature": "25"}
test2 = {"temperature": "hot"}
test3 = {}

Нужно написать:
def parse_temperature(data):

Контракт функции:
{"temperature": "25"}  → 25
{"temperature": "hot"} → None
{}                     → None
Требования: возьми значение по ключу "temperature", попробуй преобразовать его через int(),
используй try / except, поймай конкретно KeyError и ValueError, результат возвращай через return.
Не используй:
except:
или:
except Exception:"""

test1 = {"temperature": "25"}
test2 = {"temperature": "hot"}
test3 = {}

def parse_temperature(data):
    try:
        temperature = int(data["temperature"])
        return temperature
    except ValueError:
        return None
    except KeyError:
        return None
print(parse_temperature(test1))
print(parse_temperature(test2))
print(parse_temperature(test3))