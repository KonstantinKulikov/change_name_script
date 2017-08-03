import os


dir = '/Users/UserName/Documents/Image/'                                            #указываем директорию в которой лежат файлы

for file in os.listdir(dir):
       print(file+' -> '+ '{0}-{1}.jpg'.format(file[6:11], file[0:5]))              #выводим список изменяемых файлов в консоль, указываем какие части названия файла перемещаем местами
       previous_name = os.path.join(dir, file)                                      #соединяем путь к исходному файлу
       new_name = os.path.join(dir, '{0}-{1}.jpg'.format(file[6:11], file[0:5]))    #соединяем путь к переименованному файлу
       os.rename(previous_name, new_name)                                           #переименовываем файл
