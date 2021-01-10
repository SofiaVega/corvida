nombre=input("nombre: ")
f=open("txts/"+nombre+".txt","r")
html=open("cuentos/"+nombre+".html","a")
templateA=open("templateA.html","r")
templateB=open("templateB.html","r")
for line in templateA:
    html.write(line)
first=True
for line in f:
    if first:
        html.write("<div class=\"block\">")
        html.write("<p class=\"title\">")
        html.write(line)
        html.write("</p></div>")
        first=False
    else:
        html.write("<div class=\"block\">")
        html.write(line)
        html.write("</div>")
for line in templateB:
    html.write(line)
f.close()
html.close()
templateA.close()
templateB.close()