import re
def get_content():
    file = open('php.txt','r',encoding="utf-8")
    lines = file.readlines()
    file.close()
    for ids, line in enumerate(lines):
        if line.split():
            pattern = ""
            # data = "".join(i for i in line if ord(i) < 255)
            # data = "".join(re.findall(pattern, line.upper()))
            word = re.compile(r'[\u0061-\u007a,\u0020]')
            data = "".join(word.findall(line.lower()))

            clearfile = open('phpclear.txt','a')
            clearfile.write(data+' \n')
            clearfile.close()

    file.close()

if __name__ == '__main__':
    get_content()