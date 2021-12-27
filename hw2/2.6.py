# 6. * Реализовать структуру данных «Товары»Товары.
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и
# словарь с параметрами (характеристиками товара: название,
# цена, количество, единица измерения). Структуру нужно сформировать
# программно, т.е. запрашивать все данные у пользователя.

goods = [
    (1, {"Cur_ID":1, "Cur_ParentID":1, "Cur_Code":"008", "Cur_Abbreviation":"ALL", "Cur_Name":"Албанский лек", "Cur_Name_Bel":"Албанскі лек", "Cur_Name_Eng":"Albanian Lek", "Cur_QuotName":"1 Албанский лек", "Cur_QuotName_Bel":"1 Албанскі лек", "Cur_QuotName_Eng":"1 Albanian Lek", "Cur_NameMulti":"", "Cur_Name_BelMulti":"", "Cur_Name_EngMulti":"", "Cur_Scale":1, "Cur_Periodicity":1, "Cur_DateStart":"1991-01-01T00:00:00", "Cur_DateEnd":"2007-11-30T00:00:00"}),
    (2, {"Cur_ID":2, "Cur_ParentID":2, "Cur_Code":"012", "Cur_Abbreviation":"DZD", "Cur_Name":"Алжирский динар", "Cur_Name_Bel":"Алжырскі дынар", "Cur_Name_Eng":"Algerian Dinar", "Cur_QuotName":"1 Алжирский динар", "Cur_QuotName_Bel":"1 Алжырскі дынар", "Cur_QuotName_Eng":"1 Algerian Dinar", "Cur_NameMulti":"", "Cur_Name_BelMulti":"", "Cur_Name_EngMulti":"", "Cur_Scale":1, "Cur_Periodicity":1, "Cur_DateStart":"1991-01-01T00:00:00", "Cur_DateEnd":"2016-06-30T00:00:00"}),
    (3, {"Cur_ID":5, "Cur_ParentID":5, "Cur_Code":"032", "Cur_Abbreviation":"ARS", "Cur_Name":"Аргентинское песо", "Cur_Name_Bel":"Аргенцінскае песа", "Cur_Name_Eng":"Argentine Peso", "Cur_QuotName":"1 Аргентинское песо", "Cur_QuotName_Bel":"1 Аргенцінскае песа", "Cur_QuotName_Eng":"1 Argentine Peso", "Cur_NameMulti":"", "Cur_Name_BelMulti":"", "Cur_Name_EngMulti":"", "Cur_Scale":1, "Cur_Periodicity":1, "Cur_DateStart":"1991-01-01T00:00:00", "Cur_DateEnd":"2016-06-30T00:00:00"}),
    (4, {"Cur_ID":6, "Cur_ParentID":6, "Cur_Code":"100", "Cur_Abbreviation":"BGL", "Cur_Name":"Болгарский лев", "Cur_Name_Bel":"Балгарскі леў", "Cur_Name_Eng":"Bulgarian Lev", "Cur_QuotName":"1 болгарский лев", "Cur_QuotName_Bel":"1 балгарскі леў", "Cur_QuotName_Eng":"1 Bulgarian Lev", "Cur_NameMulti":"болгарский лев", "Cur_Name_BelMulti":"балгарскі леў", "Cur_Name_EngMulti":"Bulgarian Lev", "Cur_Scale":1, "Cur_Periodicity":0, "Cur_DateStart":"1991-01-01T00:00:00", "Cur_DateEnd":"2002-12-31T00:00:00"}),
    (5, {"Cur_ID":7, "Cur_ParentID":7, "Cur_Code":"040", "Cur_Abbreviation":"ATS", "Cur_Name":"Австрийский шиллинг", "Cur_Name_Bel":"Аўстрыйскі шылінг", "Cur_Name_Eng":"Austrian Schilling", "Cur_QuotName":"1 австрийский шиллинг", "Cur_QuotName_Bel":"1 aўстрыйскі шылінг", "Cur_QuotName_Eng":"1 Austrian Schilling", "Cur_NameMulti":"австрийский шиллинг", "Cur_Name_BelMulti":"aўстрыйскі шылінг", "Cur_Name_EngMulti":"Austrian Schilling", "Cur_Scale":1, "Cur_Periodicity":0, "Cur_DateStart":"1991-01-01T00:00:00", "Cur_DateEnd":"2001-12-31T00:00:00"}),
    (6, {"Cur_ID":12, "Cur_ParentID":12, "Cur_Code":"056", "Cur_Abbreviation":"BEF", "Cur_Name":"Бельгийский франк", "Cur_Name_Bel":"Бельгійскі франк", "Cur_Name_Eng":"Belgian Franc", "Cur_QuotName":"10 бельгийских франков", "Cur_QuotName_Bel":"10 бельгійскіх франкаў", "Cur_QuotName_Eng":"10 Belgian Franc", "Cur_NameMulti":"бельгийских франков", "Cur_Name_BelMulti":"бельгійскіх франкаў", "Cur_Name_EngMulti":"Belgian Franc", "Cur_Scale":10, "Cur_Periodicity":0, "Cur_DateStart":"1991-01-01T00:00:00", "Cur_DateEnd":"2001-12-31T00:00:00"}),
    (7, {"Cur_ID":19, "Cur_ParentID":19, "Cur_Code":"978", "Cur_Abbreviation":"EUR", "Cur_Name":"Евро", "Cur_Name_Bel":"Еўра", "Cur_Name_Eng":"EURO", "Cur_QuotName":"1 Евро", "Cur_QuotName_Bel":"1 Еўра", "Cur_QuotName_Eng":"1 EURO", "Cur_NameMulti":"", "Cur_Name_BelMulti":"", "Cur_Name_EngMulti":"", "Cur_Scale":1, "Cur_Periodicity":0, "Cur_DateStart":"1999-01-01T00:00:00", "Cur_DateEnd":"2016-06-30T00:00:00"}),
    (8, {"Cur_ID":23, "Cur_ParentID":23, "Cur_Code":"124", "Cur_Abbreviation":"CAD", "Cur_Name":"Канадский доллар", "Cur_Name_Bel":"Канадскі долар", "Cur_Name_Eng":"Canadian Dollar", "Cur_QuotName":"1 Канадский доллар", "Cur_QuotName_Bel":"1 Канадскі долар", "Cur_QuotName_Eng":"1 Canadian Dollar", "Cur_NameMulti":"Канадских долларов", "Cur_Name_BelMulti":"Канадскіх долараў", "Cur_Name_EngMulti":"Canadian Dollars", "Cur_Scale":1, "Cur_Periodicity":0, "Cur_DateStart":"1991-01-01T00:00:00", "Cur_DateEnd":"2021-07-08T00:00:00"}),
    (9, {"Cur_ID":26, "Cur_ParentID":26, "Cur_Code":"144", "Cur_Abbreviation":"LKR", "Cur_Name":"Шри-Ланкийская рупия", "Cur_Name_Bel":"Шры-Ланкійская рупія", "Cur_Name_Eng":"Sri Lanka Rupee", "Cur_QuotName":"1 Шри-Ланкийская рупия", "Cur_QuotName_Bel":"1 Шры-Ланкійская рупія", "Cur_QuotName_Eng":"1 Sri Lanka Rupee", "Cur_NameMulti":"", "Cur_Name_BelMulti":"", "Cur_Name_EngMulti":"", "Cur_Scale":1, "Cur_Periodicity":1, "Cur_DateStart":"1991-01-01T00:00:00", "Cur_DateEnd":"2013-05-31T00:00:00"})
]

result = {}

for value in goods:
    good = value[1]
    for value in good:
        if not result.get(value) :
            result[value] = []
        result[value].append(good[value])

print(result)