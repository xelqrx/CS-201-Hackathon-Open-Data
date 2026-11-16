import csv

# Завантажуємо таблицю
wmi_dict = {}

with open("data/wmi_full_table_ukr.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:
        wmi_dict[row["WMI"].strip().upper()] = row["Країна"].strip()


def get_country(code):
    """
    Визначає країну за першими двома символами WMI-коду.
    """

    if not isinstance(code, str) or len(code.strip()) < 2:
        return "Не визначено"

    wmi = code.strip()[:2].upper()

    return wmi_dict.get(wmi, "Не визначено")

