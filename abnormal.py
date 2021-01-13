#打开《Asteroid Justice》计算有多少个单词
file_name = "Asteroid Justice.txt"

try:
    with open(file_name) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    error_msg = "Sorry the " + file_name + " does not exist."
    print(error_msg)
else:
    words = contents.split()
    num = len(words)
    print("The file have " + str(num) + " words")

#并不是所有的错误都需要提示,通过捕获后的pass 可以避免traceback的提示
#except FileNotFoundError:
#    pass
