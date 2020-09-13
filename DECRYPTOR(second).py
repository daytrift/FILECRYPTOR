import pyAesCrypt, os
 
file = input ('Введите имя файла для расшифровки:')
password = input ('Введите пароль для расшифровки:')
 
bufferSize = 64 * 1024
 
try:
    pyAesCrypt.decryptFile(str (file), str (os.path.splitext(file)[0]) , password, bufferSize)
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), file)
    os.remove(path)
except FileNotFoundError:
    print ("ФАЙЛ НЕ НАЙДЕН!")
else:
    print ("ФАЙЛ '" + str (os.path.splitext(file)[0]) + " ' УСПЕШНО СОХРАНЕН!")
