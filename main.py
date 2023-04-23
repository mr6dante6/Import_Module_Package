import locale
from datetime import datetime
import emoji
from application.salary import calculate_salary
from application.db.people import get_employees
from dirty_main import *


locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
today = datetime.now().strftime('%A, %d %B %Y %I:%M%p')

if __name__ == '__main__':
    print(f'На данный момент ({today}) - {calculate_salary()}')
    print(f'На данный момент ({today}) - {get_employees()}')
    print(emoji.emojize('Python is :thumbs_up:'))
    example1()
    example2()
    example3()