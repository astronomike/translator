import sys

class letter:
    """
    Contains general attributes for each single unicode character
    """
    
    def __init__(self):
        self.name = None
        self.diacritic = None
        self.position = None
        
        """dictionary of unicode characters found from 
        https://en.wikipedia.org/wiki/Arabic_script_in_Unicode """
        self.dict_isolated = {
            "a": "\u0627",
            "b": "\u0628",
            "t": "\u062A",
            "th": "\u062B",
            "j": "\u062C",
            "hdot": "\u062D",
            "kh": "\u062E",
            "d": "\u0062F",
            "dh": "\u0630",
            "r": "\u0631",
            "z": "\u0632",
            "s": "\u0633",
            "sh": "\u0634",
            "sdot": "\u0635",
            "ddot": "\u0636",
            "tdot": "\u0637",
            "zdot": "\u0638",
            "'": "\u0639",
            "gh": "\u063A",
            "f": "\u0641",
            "q": "\u0642",
            "k": "\u0643",
            "l": "\u0644",
            "m": "\u0645",
            "n": "\u0646",
            "h": "\u0647",
            "w": "\u0648",
            "y": "\u064A"
        }
        
        #needs to be edited
        self.dict_beg = {
            "a": "\u0627",
            "b": "\u0628",
            "t": "\u062A",
            "th": "\u062B",
            "j": "\u062C",
            "hdot": "\u062D",
            "kh": "\u062E",
            "d": "\u0062F",
            "dh": "\u0630",
            "r": "\u0631",
            "z": "\u0632",
            "s": "\u0633",
            "sh": "\u0634",
            "sdot": "\u0635",
            "ddot": "\u0636",
            "tdot": "\u0637",
            "zdot": "\u0638",
            "'": "\u0639",
            "gh": "\u063A",
            "f": "\u0641",
            "q": "\u0642",
            "k": "\u0643",
            "l": "\u0644",
            "m": "\u0645",
            "n": "\u0646",
            "h": "\u0647",
            "w": "\u0648",
            "y": "\u064A"              
        }
        
        #needs to be edited
        self.dict_mid = {
            "a": "\u0627",
            "b": "\u0628",
            "t": "\u062A",
            "th": "\u062B",
            "j": "\u062C",
            "hdot": "\u062D",
            "kh": "\u062E",
            "d": "\u0062F",
            "dh": "\u0630",
            "r": "\u0631",
            "z": "\u0632",
            "s": "\u0633",
            "sh": "\u0634",
            "sdot": "\u0635",
            "ddot": "\u0636",
            "tdot": "\u0637",
            "zdot": "\u0638",
            "'": "\u0639",
            "gh": "\u063A",
            "f": "\u0641",
            "q": "\u0642",
            "k": "\u0643",
            "l": "\u0644",
            "m": "\u0645",
            "n": "\u0646",
            "h": "\u0647",
            "w": "\u0648",
            "y": "\u064A"              
        }
        
        #needs to be edited
        self.dict_end = {
            "a": "\u0627",
            "b": "\u0628",
            "t": "\u062A",
            "th": "\u062B",
            "j": "\u062C",
            "hdot": "\u062D",
            "kh": "\u062E",
            "d": "\u0062F",
            "dh": "\u0630",
            "r": "\u0631",
            "z": "\u0632",
            "s": "\u0633",
            "sh": "\u0634",
            "sdot": "\u0635",
            "ddot": "\u0636",
            "tdot": "\u0637",
            "zdot": "\u0638",
            "'": "\u0639",
            "gh": "\u063A",
            "f": "\u0641",
            "q": "\u0642",
            "k": "\u0643",
            "l": "\u0644",
            "m": "\u0645",
            "n": "\u0646",
            "h": "\u0647",
            "w": "\u0648",
            "y": "\u064A"              
        }
        

def translate_word(eng_word):
    """
    Function to translate a single word. 
    -------------------
    Parameters
    -------------------
    eng_word : input string of latin characters : string

    -------------------
    Returns
    -------------------
    arb_word : translated string of arabic unicode characters : string        
    """
    
    arb_word = []
    print(eng_word)
    for i in range(len(eng_word)):
        l = letter()
        l.name = eng_word[i]
        if i == 0:    
            arb_word.append(l.dict_beg[l.name])
        elif i == len(eng_word):
            arb_word.append(l.dict_end[l.name])
        else:
            arb_word.append(l.dict_mid[l.name])

    return arb_word

def translate_line(eng_sent):
    """
    Function to translate one or more english sentences. Makes use of 
    translate_word() iteratively. 
    -------------------
    Parameters
    -------------------
    eng_sent : input string of latin characters : string

    -------------------
    Returns
    -------------------
    arb_sent : translated string of arabic unicode characters : string        
    """
    arb_sent = []
    
    #main loop to run through sentence and append translated arabic chars
    for i in range(len(eng_sent)):
        
        #find spaces that separate words. 
        if eng_sent[i] == " ":     
            continue   
        
    return arb_sent

def translate_file(infile):
    
    try:
        with open(infile,"r") as df:
            parameters = []            
            lines = df.read().splitlines()
            
            for i in range(len(lines)):
                if (lines[i] == "") or (lines[i][0] == "#") or (lines[i][0] == "\n"):
                    continue
                else:
                    parameters.append(lines[i].split(" = "))
    except FileNotFoundError():
        print("File does not exist")

#%%
"""
######################################################################
Execution
"""
eng_word = sys.argv[1]
print(translate_word(eng_word))



