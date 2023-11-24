# TODO  Напишите функцию count_letters
def count_letters(text):
    text_lower = text.lower()
    dict_letters = {}
    for i in range(len(text_lower)):
        if text_lower[i].isalpha():
            if text_lower[i] in dict_letters.keys():
                dict_letters[text_lower[i]] += 1
            else:
                dict_letters[text_lower[i]] = 1
    return dict_letters

# TODO Напишите функцию calculate_frequency
def calculate_frequency(dict_letters):
    number_of_letters = 0
    for j in dict_letters.values():
        number_of_letters += j
    for key in list(dict_letters.keys()):
        dict_letters[key] = '{:.2f}'.format(round((dict_letters[key] / number_of_letters), 2))
    return dict_letters


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте

result = calculate_frequency(count_letters(main_str))
for key, value in result.items():
    print(key + ":", value)
    