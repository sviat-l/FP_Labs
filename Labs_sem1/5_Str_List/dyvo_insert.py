def dyvo_insert(sentence, flag):
    """
    (str, str) -> str
    Inserting word "диво" before every word that starts with flag.
    >>> dyvo_insert("Кит кота по хвилях катав - кит у воді, кіт на киті", 'ки')
    'дивокит кота по хвилях катав - дивокит у воді, кіт на дивокиті'
    >>> dyvo_insert("Кит кота по хвилях катав - кит у воді, кіт на киті", 'код')
    'кит кота по хвилях катав - кит у воді, кіт на киті'
    """
    output=''
    flag_len = len(flag)

    for i in range(len(sentence) - flag_len+1):
        if sentence[i : i + flag_len].lower() == flag:
            output += 'диво'
        output += sentence[i].lower()

    if flag_len > 1:
        output += sentence [-flag_len +1 :].lower()

    return output


print(dyvo_insert("Кит кота по хвилях катав - кит у воді, кіт на киті", 'киnj'))
