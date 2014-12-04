import sqlite3

connector = sqlite3.connect("company_database")
cursor = connector.cursor()


def list_employees():
    cursor.execute('''SELECT name, position from company''')
    for row in cursor:
        list_of_employees = '{0} - {1}'.format(row[0], row[1])
        return list_of_employees


def montly_spending():
    total_montly_spending = cursor.execute('''SELECT sum(montly_salary) as sum from company''')
    for row in total_montly_spending:
        total = "Total montly spending: " + '{0}'.format(row[0])
        return total


def yearly_spending():
    total_yearly_spending = cursor.execute('''SELECT sum(montly_salary) as sum from company''')
    for row in total_yearly_spending:
        total_yearly_spending = '{0}'.format(row[0])
    bonus = cursor.execute('''SELECT sum(yearly_bonus) as sum from company''')
    for row in bonus:
        bonus = '{0}'.format(row[0])
    total_yearly = "Total yearly spending: " + str((int(total_yearly_spending) * 12) + int(bonus))
    return total_yearly

print(list_employees())
print(montly_spending())
print(yearly_spending())
