import csv
import statistics
from sys import argv

if str(argv[1]) == '-h':
    print(f'Программа используется с введенными параметрами "Имя функции" "Имя csv файла" "Delimiter"')
else:
    name, filename, delim = argv
    with open(filename, 'r+', newline='') as csv_file:

        '''filewriter = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['Months', 'North', 'South', 'West', 'East'])
        filewriter.writerow(['September', '1', '3', '2', '4'])
        filewriter.writerow(['October', '1', '', '2', '3'])
        filewriter.writerow(['November', '2', '1', '', '3'])
        filewriter.writerow(['December', '4', '3', '2', '1'])'''
        csv_reader = csv.reader(csv_file, delimiter=delim)
        summ = 0  
        blank = 0
        line_count = 0
        lencnt = 0
        items = []
        print(f'Введите номер компании о которой хотите узнать:')
        i = input()
        for row in csv_reader:
            while i < '1' or i > str(len(row)):
                print(f'Введен неверный тип данных, либо компании с таким номером не существует. Попробуйте еще раз:')
                i = input()
            else:
                a = int(i)
            if len(row[a]) != 0:
                if row[a].isdigit() != 1:
                    print(f'Название компании {row[a]}')
                else:
                    summ += float(row[a])
                    items.append(row[a])
                    lencnt += 1
            else:
                blank += 1
        if len(items) > 2:
            print(f'Медиана {statistics.median(items)}')
        else:
            print(f'Слишком мало значений для определения медианы!')
        print(f'Сумма {summ}')
        print(f'Среднее {summ/lencnt}')
        print(f'Колличество пропусков {blank}')

