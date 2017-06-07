#!/usr/bin/python
# -*- coding: UTF-8 -*-




def CountOccurencesInText(word,text):
    """Number of occurences of word (case insensitive) in text"""
    #This does not pass the unittests:
    tmpWord = word.lower().split()
    #tmpText = text.lower().split()
    tmpText = text.lower().replace("."," ").replace("!"," ").replace("?","").replace(","," ").replace(":","").split()
    numWord = 0
    #print tmpText
    #print tmpWord
    if len(tmpWord) == 1:
        for word in tmpText:
            print word
            if word == tmpWord[0]:
                numWord = numWord + 1
    else:
        isFound = False
        firstIndex = 0
        lastIndex = len(tmpText)
        if tmpWord[0][0] == '\'' and tmpWord[-1][-1] == '\'':
            #print "lenWord:"+str(len(tmpWord))
            while tmpText :
                
                #print "tmpText:-----"+tmpText[0]
                #print "tmpWord:-----"+tmpWord[0]+"\n"
                if tmpText[0] == tmpWord[0]:
                    tmpText.pop(0)
                    #print "apres pop,tmpText:"+tmpText[0]
                    for i in range(1,len(tmpWord)):
                        #print "in for,tmpWord:"+tmpWord[i]
                        if tmpWord[i] == tmpText[0]:
                            tmpText.pop(0)
                            if i == len(tmpWord)-1:
                                numWord = numWord + 1
                        else:
                            break
                else:
                    tmpText.pop(0)
        #if the first symbol is a letter, we compare the word with (word)
        elif tmpWord[0][0].isalpha():
            while tmpText:
                #tmpText.pop()
                # print "tmpText[0][0]:------"+tmpText[0][0]+str(tmpText[0][0] == u"\u201c")
                # print "tmpWord[0]:------"+tmpWord[0]
                if (tmpText[0][0] == "(" and tmpText[0].replace('(','') == tmpWord[0]) or (tmpText[0][0] == u"«" and tmpText[0].replace(u'«','') == tmpWord[0]) or (tmpText[0][0] == u"\u201c" and tmpText[0].replace(u'\u201c','') == tmpWord[0]):
                    tmpText.pop(0)
                    # print "tmpText in if---------"
                    # print tmpText
                    for i in range(1,len(tmpWord)): 
                        if tmpWord[i] == tmpText[0]:
                            tmpText.pop(0)
                            print "match!"
                        else:
                            if i == len(tmpWord)-1:
                                if (tmpText[0][-1]==')' and tmpWord[i] == tmpText[0].replace(')','')) or (tmpText[0][-1]==u'»' and tmpWord[i] == tmpText[0].replace(u'»','')) or (tmpText[0][-1]==u'\u201d' and tmpWord[i] == tmpText[0].replace(u'\u201d','')) :
                                    numWord = numWord + 1
                                else:
                                    print "doesn't match"
                                    break
                else:
                    tmpText.pop(0)
                    #print tmpText
            tmpText = text.lower().replace("."," ").replace("!"," ").replace("?","").replace(","," ").replace(":","").split()
            print tmpText
            while tmpText:
                if tmpText[0] == tmpWord[0]:
                    tmpText.pop(0)
                    for i in range(1,len(tmpWord)):
                        if tmpWord[i] == tmpText[0]:
                            tmpText.pop(0)
                            print "match!!"+str(len(tmpWord))+" "+str(i)
                            if i == len(tmpWord) - 1:
                                print "hah"
                                numWord = numWord + 1
                        else:
                            if i == len(tmpWord) - 1:
                                print "oeee"
                                if tmpText[0][-1] == '\"' and tmpWord[i] == tmpText[0].replace('\"',''):
                                    numWord = numWord + 1
                                else:
                                    print "doesn match"
                                    break
                else:
                    tmpText.pop(0)
            # tmpText = text.lower().replace("."," ").replace("!"," ").replace("?","").replace(","," ").split()
            # while tmpText:
            #     if tmpText[0][0] == '«' tmpText[0] == tmpWord[0]:
            #         tmpText.pop(0)
            #         for i in range(1,len(tmpWord)):
            #             if tmpWord[i] == tmpText[0]:
            #                 tmpText.pop(0)
            #                 print "match!"
            #             else:
            #                 if i == len(tmpWord) - 1:
            #                     if tmpText[0][-1] == '\"' and tmpWord[i] == tmpText[0].replace('\"',''):
            #                         numWord = numWord + 1
            #                     else:
            #                         print "doesn match"
            #                         break
            #     else:
            #         tmpText.pop(0)

    print numWord
    return numWord


def testCountOccurencesInText():
    """ Test the CountOccurencesInText function"""
    text="""Georges is my name and I like python. Oh ! your name is georges? And you like Python!
Yes is is true, I like PYTHON
and my name is GEORGES"""
    # test with a little text.
    '''assert( 3 == CountOccurencesInText("Georges",text) )
    assert( 3 == CountOccurencesInText("GEORGES",text) )
    assert( 3 == CountOccurencesInText("georges",text) )
    assert( 0 == CountOccurencesInText("george",text) )
    assert( 3 == CountOccurencesInText("python",text) )
    assert( 3 == CountOccurencesInText("PYTHON",text) )
    assert( 2 == CountOccurencesInText("I",text) )
    assert( 0 == CountOccurencesInText("n",text) )
    assert( 1 == CountOccurencesInText("true",text) )    
    # regard ' as text:
    assert ( 0 == CountOccurencesInText ( "maley", "John O'maley is my friend" ) )
    # Test it but with a BIG length file. (we once had a memory error with this...)
    text = """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy dog.""" * 500
    text += """The quick brown fox jump over the lazy dog.The quick brown Georges jump over the lazy dog."""
    text += """esrf sqfdg sfdglkj sdflgh sdflgjdsqrgl """ * 4000
    text += """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy python.""" 
    text += """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy dog.""" * 500
    text += """The quick brown fox jump over the lazy dog.The quick brown Georges jump over the lazy dog."""
    text += """esrf sqfdg sfdglkj sdflgh sdflgjdsqrgl """ * 4000
    text += """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy python.""" 
    text += """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy dog.""" * 500
    text += """The quick brown fox jump over the lazy dog.The quick brown Georges jump over the lazy dog."""
    text += """esrf sqfdg sfdglkj sdflgh sdflgjdsqrgl """ * 4000
    text += """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy python.""" 
    text += """The quick brown fox jump over the true lazy dog.The quick brown fox jump over the lazy dog."""
    text += """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy dog.""" * 500
    text += """ I vsfgsdfg sfdg sdfg sdgh sgh I sfdgsdf"""
    text += """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy dog.""" * 500
    assert( 3 == CountOccurencesInText("Georges",text) )
    assert( 3 == CountOccurencesInText("GEORGES",text) )
    assert( 3 == CountOccurencesInText("georges",text) )
    assert( 0 == CountOccurencesInText("george",text) )
    assert( 3 == CountOccurencesInText("python",text) )
    assert( 3 == CountOccurencesInText("PYTHON",text) )
    assert( 2 == CountOccurencesInText("I",text) )
    assert( 0 == CountOccurencesInText("n",text) )
    assert( 1 == CountOccurencesInText("true",text) )'''
    assert( 0 == CountOccurencesInText("reflexion mirror",
     "I am a senior citizen and I live in the Fun-Plex 'Reflexion Mirror' in Sopchoppy, Florida") )
    assert( 1 == CountOccurencesInText("'reflexion mirror'",
     "I am a senior citizen and I live in the Fun-Plex 'Reflexion Mirror' in Sopchoppy, Florida") )
    assert( 1 == CountOccurencesInText("reflexion mirror",
     "I am a senior citizen and I live in the Fun-Plex (Reflexion Mirror) in Sopchoppy, Florida") )
    assert( 1 == CountOccurencesInText("reflexion mirror",
     "Reflexion Mirror\" in Sopchoppy, Florida") )
    assert( 1 == CountOccurencesInText("reflexion mirror",
     u"I am a senior citizen and I live in the Fun-Plex «Reflexion Mirror» in Sopchoppy, Florida") )
    assert( 1 == CountOccurencesInText("reflexion mirror",
     u"I am a senior citizen and I live in the Fun-Plex \u201cReflexion Mirror\u201d in Sopchoppy, Florida") )
    assert( 1 == CountOccurencesInText("legitimate",
     u"who is approved by OILS is completely legitimate: their employees are of legal working age") )
    assert( 0 == CountOccurencesInText("legitimate their",
     u"who is approved by OILS is completely legitimate: their employees are of legal working age") )
    assert( 1 == CountOccurencesInText("get back to me",
     u"I hope you will consider this proposal, and get back to me as soon as possible") )
    assert( 1 == CountOccurencesInText("skin-care",
     u"enable Delavigne and its subsidiaries to create a skin-care monopoly") )
    assert( 1 == CountOccurencesInText("skin-care monopoly",
     u"enable Delavigne and its subsidiaries to create a skin-care monopoly") )
    assert( 0 == CountOccurencesInText("skin-care monopoly in the US",
     u"enable Delavigne and its subsidiaries to create a skin-care monopoly") )
    assert( 1 == CountOccurencesInText("get back to me",
     u"When you know:get back to me") )
    assert( 1 == CountOccurencesInText("don't be left" , """emergency alarm warning.
Don't be left unprotected. Order your SSSS3000 today!""" ) )
    assert( 1 == CountOccurencesInText("don" , """emergency alarm warning.
Don't be left unprotected. Order your don SSSS3000 today!""" ) )
    assert( 1 == CountOccurencesInText("take that as a 'yes'",
     "Do I have to take that as a 'yes'?") )
    assert( 1 == CountOccurencesInText("don't take that as a 'yes'",
     "I don't take that as a 'yes'?") )        
    assert( 1 == CountOccurencesInText("take that as a 'yes'",
     "I don't take that as a 'yes'?") )
    assert( 1 == CountOccurencesInText("don't",
     "I don't take that as a 'yes'?") )
    assert( 1 == CountOccurencesInText("attaching my c.v. to this e-mail",
     "I am attaching my c.v. to this e-mail." ))
    assert ( 1 == CountOccurencesInText ( "Linguist", "'''Linguist Specialist Found Dead on Laboratory Floor'''" ))
    assert ( 1 == CountOccurencesInText ( "Linguist Specialist", "'''Linguist Specialist Found Dead on Laboratory Floor'''" ))
    assert ( 1 == CountOccurencesInText ( "Laboratory Floor", "'''Linguist Specialist Found Dead on Laboratory Floor'''" ))
    assert ( 1 == CountOccurencesInText ( "Floor", "'''Linguist Specialist Found Dead on Laboratory Floor'''" ))
    assert ( 1 == CountOccurencesInText ( "Floor", "''Linguist Specialist Found Dead on Laboratory Floor''" ))        
    assert ( 1 == CountOccurencesInText ( "Floor", "__Linguist Specialist Found Dead on Laboratory Floor__" ))
    assert ( 1 == CountOccurencesInText ( "Floor", "'''''Linguist Specialist Found Dead on Laboratory Floor'''''" ))
    assert ( 1 == CountOccurencesInText ( "Linguist", "'''Linguist Specialist Found Dead on Laboratory Floor'''" ))
    assert ( 1 == CountOccurencesInText ( "Linguist", "''Linguist Specialist Found Dead on Laboratory Floor''" ))        
    assert ( 1 == CountOccurencesInText ( "Linguist", "__Linguist Specialist Found Dead on Laboratory Floor__" ))
    assert ( 1 == CountOccurencesInText ( "Linguist", "'''''Linguist Specialist Found Dead on Laboratory Floor'''''" ))
    assert ( 1 == CountOccurencesInText ( "Floor", """Look: ''Linguist Specialist Found Dead on Laboratory Floor'' is the headline today."""))

    
SampleTextForBench = """
A Suggestion Box Entry from Bob Carter

Dear Anonymous,

I'm not quite sure I understand the concept of this 'Anonymous' Suggestion Box. If no one reads what we write, then how will anything ever
change?

But in the spirit of good will, I've decided to offer my two cents, and hopefully Kevin won't steal it! (ha, ha). I would really like to
see more varieties of coffee in the coffee machine in the break room. 'Milk and sugar', 'black with sugar', 'extra sugar' and 'cream and su
gar' don't offer much diversity. Also, the selection of drinks seems heavily weighted in favor of 'sugar'. What if we don't want any suga
r?

But all this is beside the point because I quite like sugar, to be honest. In fact, that's my second suggestion: more sugar in the office.
Cakes, candy, insulin, aspartame... I'm not picky. I'll take it by mouth or inject it intravenously, if I have to.

Also, if someone could please fix the lock on the men's room stall, that would be helpful. Yesterday I was doing my business when Icarus ne
arly climbed into my lap.

So, have a great day!

Anonymously,
 Bob Carter
"""

    
    
def doit():
    """Run CountOccurencesInText on a few examples"""
    i = 0
    for x in xrange(400):
        i+= CountOccurencesInText("word" , SampleTextForBench)
        i+= CountOccurencesInText("sugar" , SampleTextForBench)
        i+= CountOccurencesInText("help" , SampleTextForBench)
        i+= CountOccurencesInText("heavily" , SampleTextForBench)
        i+= CountOccurencesInText("witfull" , SampleTextForBench)
        i+= CountOccurencesInText("dog" , SampleTextForBench)
        i+= CountOccurencesInText("almost" , SampleTextForBench)
        i+= CountOccurencesInText("insulin" , SampleTextForBench)
        i+= CountOccurencesInText("attaching" , SampleTextForBench)
        i+= CountOccurencesInText("asma" , SampleTextForBench)
        i+= CountOccurencesInText("neither" , SampleTextForBench)
        i+= CountOccurencesInText("won't" , SampleTextForBench)
        i+= CountOccurencesInText("green" , SampleTextForBench)
        i+= CountOccurencesInText("parabole" , SampleTextForBench)
    print i
        



#Start the tests     
if __name__ == '__main__':
    #I need to pass the test:
    try:
        testCountOccurencesInText()
    except:
        print "Error !"
        raise
    print "Tests passed"
    #I need to be fast as well:
    import profile
    profile.run('doit()')
    
    


