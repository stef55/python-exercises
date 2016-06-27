#call a function both with positional and keyword arguments
def speak(country,language):
    print('in ' +country+' the most spoken language is '+language)
speak('great britain','english')
speak(language='german',country='germany')
speak('italy',language='italian')
