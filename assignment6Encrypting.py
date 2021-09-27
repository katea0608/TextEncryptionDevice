#Kate Anderson U21933376

def main():

    text = open('desiderata.txt','r')
    contents = text.read()
    encrypt(contents)
    
    out1 = open('encryptedText.txt', 'w')
    out1.write(encrypt(contents))
    out1.close()

    in1= open('encryptedText.txt','r')
    translation = in1.read()
    in1.close()

    print(translation)
    

    #end main


def encrypt(contents):

    encrypt_code = {
        'A': ')', 'a':'0', 'B':'(', 'b':'9', 'C':'*','c':'8',
        'D':'&', 'd':'7', 'E':'^', 'e':'6',' F':'%','f':'5',
        'G':'$','g':'4','H':'#','h':'3','I':'@','i':'2',
        'J':'!','j':'1','K':'Z','k':'z','L':'Y','l':'y',
        'M':'X','m':'x','N':'W','n':'w','O':'V','o':'v',
        'P':'U','p':'u','Q':'T','q':'t','R':'S','r':'s',
        'S':'R','s':'r','T':'Q','t':'q','U':'P','u':'p',
        'V':'O','v':'o','W':'N','w':'n','X':'M','x':'m',
        'Y':'L','y':'l','Z':'K','z':'k','!':'J','1':'j',
        '@':'I','2':'i','#':'H','3':'h','$':'G','4':'g',
        '%':'F','5':'f','^':'E','6':'e','&':'D','7':'d',
        '*':'C','8':'c','(':'B','9':'b',')':'A','0':'a',
        ':':',',',':':','?':'.','.':'?','<':'>','>':'<',
        "'":'"','"':"'",'+':'-','-':'+','=':';',';':'=',
        '{':'[','[':'{','}':']',']':'}'
        }

    x = contents.split()

    newlist = []
    
    for i in x:
        for s in i:
            t = encrypt_code[s]
            newlist.append(t)

    encryption = ''
    for i in newlist:
        encryption = encryption + i + ' '

    return encryption
        
            

main()    
