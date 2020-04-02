def cezar(text, n):
    n = int(n)
    text = text.lower()
    print(n)
    abc = " abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    finish = ''
    for i in text:
        if (i == "."):
            finish += "."
        elif (i == " "):
            finish += " "
        elif (i == ","):
            finish += ","
        else:
            finish += abc[(abc.index(i) + n)]
    print(finish)
op = open('txt-r.txt', 'r')
lines = "".join(op)
number = open('number.txt', 'r')
n = "".join(number)
code = cezar(lines, n)
wr = open('txt-w.txt', 'w')
wr.write(code)
wr.close()
