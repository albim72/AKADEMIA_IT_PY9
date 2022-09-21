from xml.dom.minidom import parse

dom = parse("dane.xml")
name = dom.getElementsByTagName('name')
kod = dom.getElementsByTagName('kod')
strona = dom.getElementsByTagName('strona')

#wewnątrz funckji join() jest osadzona funkcja anonimowa Pythona (return instrukcje)
print(" ".join(t.nodeValue for t in name[0].childNodes if t.nodeType == t.TEXT_NODE))
print(" ".join(t.nodeValue for t in kod[0].childNodes if t.nodeType == t.TEXT_NODE))
print(" ".join(t.nodeValue for t in strona[0].childNodes if t.nodeType == t.TEXT_NODE))
print(" ".join(t.nodeValue for t in kod[1].childNodes if t.nodeType == t.TEXT_NODE))
