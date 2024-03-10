
# Напишите проект, содержащий функционал работы с заметками. Программа должна уметь создавать заметку, 
# сохранять её, читать список заметок, редактировать заметку, удалять заметку.

def add_new_note(fileName: str):
    with open(fileName, 'a+', encoding='utf-8') as f:
        name = input('Введите название: ')
        text = input('Введите текст: ')
        f.write(f'{name}. {text}\n')
        
def read_all(fileName: str):
    with open(fileName, 'r+', encoding='utf-8') as f:
        d = f.readlines()
        return d
    
def output_title(lists: list) -> None:
    print()

    count = 1
    for i in lists:
        s = i.split('. ')
        print(str(count) + '. ' + s[0])
        count+=1
    print()

def show_note(fileName: str):
    with open(fileName, 'r', encoding='utf-8') as f:
        date = f.readlines()
        marker = input('Введите имя для поиска: ')
        res = list(filter(lambda x: x.split('.')[0] == marker, date))
        return res
    
def replace(lists: list):
    list1 = []        
    for i in lists:
        print(i)
        list1.append(i.rstrip().split('. '))
    index = int(input('Введите порядковый номер заметки для изменения: ')) - 1
    print(list1[index])
    new_text = input('Введите новый текст: ')
    list1[index][1] = new_text
    with open(file, 'w', encoding='utf-8') as f:
        for i in list1:
            f.write(f'{i[0]}. {i[1]}\n')

def remove(lists: list):
    index = int(input('Введите порядковый номер заметки для удаления: ')) - 1
    print(lists[index])
    with open(file, 'w', encoding='utf-8') as f:
        for i in range(len(lists)):
            if i == index:
                continue
            else:
                f.write(f'{lists[i]}')
     
file = 'bib.txt' 

def main():
    print('')
    print('Доступные операции: ')
    print('1 - Список заметок')
    print('2 - Показать заметку')
    print('3 - Изменить заметку')
    print('4 - Удалить заметку')
    print('5 - Новая заметка')
    print('0 - Выход')
    print('')
    flag = False
    while not flag:
        
        answer = input('Введите операцию: ')
        if answer not in '012345':
            print('Неверный выбор!')
        elif answer == '1':
            output_title(read_all(file))
        elif answer == '2':
            print('.'.join(show_note(file)))
        elif answer == '3':
            replace(read_all(file))
        elif answer == '4':
            remove(read_all(file))
        elif answer == '5':
            add_new_note(file)
        elif answer == '0':
            flag = True

if __name__ == '__main__':
    main()
