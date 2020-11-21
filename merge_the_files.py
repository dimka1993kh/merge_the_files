# Создадим класс с необходимыми методами:
class file_text():
    def __init__(self, file_path, list_files=''):
        self.file_path = file_path
        self.access_mode_read = 'r'
        self.access_mode_write = 'w'
        self.list_files = list_files
    # Метод чтения файла
    def read_file(self):
        with open(self.file_path, self.access_mode_read, encoding='utf-8') as f:
            return f.readlines()
    # Метод записи в файл
    def write_file_sort(self):
        list_tuple = []
        result_list = []
        # Создадим кортежи, содержащие путь к файлу, число строк в файле и сам файл.
        # Отсортируем список кортежей по количеству сторк в нем
        for file in self.list_files:
            file_text = file.read_file()
            list_tuple.append(( file.file_path + '\n', str(len(file_text)) + '\n', file_text, '--------------------', '\n'))
        sotrted_list_tuple = sorted(list_tuple, key=lambda sorted_list: sorted_list[2])
        # запишем каждую строку в result_list
        for file in sotrted_list_tuple:
            for line in file:
                result_list.append(''.join(line))
        # Запишем результат а файл
        with open(self.file_path, self.access_mode_write, encoding='utf-8') as document:  
            return document.write(''.join(result_list)) 

# Создадим экземпляры класса на основе исходных фалов
file_one = file_text('папка с исходными файлами/1.txt')
file_two = file_text('папка с исходными файлами/2.txt')
file_three = file_text('папка с исходными файлами/3.txt')
# Создадим список экземпляров
list_files = [file_one, file_two, file_three]
# Создадим нужный файл
result_file = file_text('папка с конечным файлом/result_file.txt', list_files).write_file_sort()
