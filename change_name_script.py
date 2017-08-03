import os

#указываем директорию в которой лежат файлы
dir = '/Users/UserName/Documents/Image/'                                            

for file in os.listdir(dir):
       #выводим список изменяемых файлов в консоль, 
       #указываем какие части названия файла перемещаем местами
       print(file+' -> '+ '{0}-{1}.jpg'.format(file[6:11], file[0:5]))
       
       #соединяем путь к исходному файлу
       previous_name = os.path.join(dir, file)
       
       #соединяем путь к переименованному файлу
       new_name = os.path.join(dir, '{0}-{1}.jpg'.format(file[6:11], file[0:5]))
       
       #переименовываем файл
       os.rename(previous_name, new_name)
