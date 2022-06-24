inputText1 = Element("inputText1")
inputText2 = Element("inputText2")   

salidasuma = Element("salidasuma")
salidaresta = Element("salidaresta")
salidamulti = Element("salidamulti")
salidadivi = Element("salidadivi")

def clear(*args, **kwargs):
    inputText1.clear()
    inputText2.clear()
    salidasuma.clear()
    salidaresta.clear()
    salidamulti.clear()
    salidadivi.clear()

def operacion(*args, **kwargs):
    totalsuma = int(inputText1.value) + int(inputText2.value)
    salidasuma.write(totalsuma)
    totalresta = int(inputText1.value) - int(inputText2.value)
    salidaresta.write(totalresta)
    totalmulti = int(inputText1.value) * int(inputText2.value)
    salidamulti.write(totalmulti)
    totaldivi = int(inputText1.value) / int(inputText2.value)
    salidadivi.write(totaldivi)