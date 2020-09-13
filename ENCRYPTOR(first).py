import pyAesCrypt, os
 
file = input ('Введите имя файла для шифрования:')
password = input ('Введите пароль для шифрования:')
 
bufferSize = 64 * 1024
 
try:
    pyAesCrypt.encryptFile (str (file), str (file) + ".crpt", password, bufferSize)
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), file)
    os.remove(path)
except FileNotFoundError:
    print ("ФАЙЛ НЕ НАЙДЕН!")
    
else:
    print ("ФАЙЛ '"+str (file) + " .crpt' УСПЕШНО СОХРАНЕН!")
