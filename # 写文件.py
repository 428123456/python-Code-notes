# 写文件
with open ("test.txt","wt") as out_file:
    out_file.write("该文件会写入到文件\n看到我吧！")

#Read a file
with open("test.txt","rt") as in_file:
    text = in_file.read()

print(text)
