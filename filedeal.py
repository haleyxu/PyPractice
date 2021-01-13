#打开文件
with open("pi_data.txt") as file_object:
    contents = file_object.read()
    print(contents)


print('-' * 20)
#打开文件，按行输出
file_name = "pi_data.txt"

with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())

print('-' * 20) 
#with代码段外使用文件内容
with open(file_name) as file_object:
    outfile = file_object.read()
print(outfile)

#写入文件 py只能写入字符串 w：写入 a:追加 r:读取（默认） r+:读取和写入
write_file_name = "write.txt"
with open(write_file_name, 'w') as write_file:
    write_file.write("python example\n")
    write_file.write("3.1415926535\n")

with open(write_file_name, 'a') as append_file:
    append_file.write("new line\n")
    append_file.write("Oh cool")



