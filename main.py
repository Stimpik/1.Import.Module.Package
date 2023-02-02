from datetime import datetime
from application.salary import calculate_salary as sal
from application.db.people import get_employees as pep



def main():
    print(datetime.now().strftime("Hello!\nToday is %d of %B %Y, %H-%M-%S \n\n"))
    while True:
        command = input('Поглядеть зарплату(S), поглядеть сотрудников(E), выйти(Q)')
        if command.lower() == 's':
            sal()
        if command.lower() == 'e':
            pep()
        if command.lower() == 'q':
            break

if __name__ == '__main__':
    main()


