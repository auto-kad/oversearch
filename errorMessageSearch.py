import sys
from googlesearch import search
import webbrowser

""" the bash script sends an array of strings to this python script;
to be properly parsed as an error message, it needs to be put back together
as a string, which is done via the join method. """

errorMessageList = sys.argv[1:]
errorMessageString = ' '.join([str(partialString) for partialString in errorMessageList])


""" errorMessageString is the input used to search the web for the top result """


for error in search(errorMessageString, tld = "com", num = 1, stop = 1):
    print(errorMessageString)
    webbrowser.open(error, new = 2)
    print("The url: " + error + " was opened")
    
    

    


