# TODO  Напишите функцию count_letters
def count_letters(text):
    dict_ = {}
    for item in text:
        if item.isalpha():
            dict_[item] = text.count(item)
    return dict_


# TODO Напишите функцию calculate_frequency
def calculate_frequency(dict_):
    new_dict = {}
    num_of_letters = sum(dict_.values())
    for item in dict_:
        new_dict[item] = format(dict_.get(item) / num_of_letters, '.2f')
    return new_dict


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
main_str = main_str.lower()
dict_ = count_letters(main_str)
new_dict = calculate_frequency(dict_)
for item in new_dict:
    print(f"{item}: {new_dict.get(item)}")
# TODO Распечатайте в столбик букву и её частоту в тексте
