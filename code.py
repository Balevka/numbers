import codecs

ruLetters = {'a': 1, 'б': 2, 'в': 3, 'г': 4, 'д': 5, 'е': 6, 'ё': 7, 'ж': 8, 'з': 9, 'и': 10, 'й': 20, 'к': 30, 'л': 40,
             'м': 50, 'н': 60, 'о': 70, 'п': 80, 'р': 90, 'с': 100, 'т': 200, 'у': 300, 'ф': 400, 'х': 500, 'ц': 600,
             'ч': 700, 'ш': 800, 'щ': 900, 'ъ': 1000, 'ы': 2000, 'ь': 3000, 'э': 4000, 'ю': 5000, 'я': 6000, '\n': ' ',
             'А': 1, 'Б': 2, 'В': 3, 'Г': 4, 'Д': 5, 'Е': 6, 'Ё': 7, 'Ж': 8, 'З': 9, 'И': 10, 'Й': 20, 'К': 30, 'Л': 40,
             'М': 50, 'Н': 60, 'О': 70, 'П': 80, 'Р': 90, 'С': 100, 'Т': 200, 'У': 300, 'Ф': 400, 'Х': 500, 'Ц': 600,
             'Ч': 700, 'Ш': 800, 'Щ': 900, 'Ъ': 1000, 'Ы': 2000, 'Ь': 3000, 'Э': 4000, 'Ю': 5000, 'Я': 6000}
paragraphsEnd = {}

text = 'Стоял он., дум вели.ких полн,\nИ вдаль глядел, Пред ним широко\n\n Река неслася; бедный чёлн\n\nПо ней стремился одиноко.\nПо мшистым, топким берегам\n Чернели избы здесь и там,\nПриют убогого чухонца;\nИ лес, неведомый лучам \nВ тумане спрятанного солнца,\nКругом шумел.\n\n'
newText = text
globalPoints = [0]*len(text)
points = [0]*len(text)

def lettersCounter(start, end):                    # Считает количество букв
    letters = 0
    for i in range(start, end):
        if text[i] == "," or text[i] == "." or text[i] == ";" or text[i] == "!" or text[i] == "?" or text[i] == "\n" or text[i] == " ":
            continue
        else:
            letters += 1
    return letters

def wordsCounter(start, end):                      # Считает количество слов
    words = 0
    for letter in range(start, end):
        if text[letter] == "\n" or text[letter] == " ":
            words += 1
        else:
            continue

    return words

def pointRegister(start, end):                    # Считает кол-во предложений и заносит номера точек, восклицательных м вопросительных знаков в points[]
    sentences = 0
    j = 0
    for i in range(start, end):
        if text[i-1] == "?" and text[i] == "!":
            continue
        elif text[i] == "?" or text[i] == "!" or text[i] == ".":
            sentences += 1
            points[j] = i
            j += 1
        else:
            continue
    return sentences


def globalPointRegister(start, end):                    # заносит номер всех точек а globalPoints[]
    sentences = 0
    j = 0
    for i in range(start, end):
        if text[i-1] == "?" and text[i] == "!":
            continue
        elif text[i] == "?" or text[i] == "!" or text[i] == ".":
            sentences += 1
            globalPoints[j] = i
            j += 1
        else:
            continue
    return sentences

def paragraphCounter():                 # Считает кол-во абзацев в тексте
    paragraph = 0
    for i in range(0, len(text)):
        if(text[i] == "\n" and text[i-1] == "\n"):
            paragraph += 1
            paragraphsEnd[i] = i
    return paragraph

def inSentences(start, end):
    prevPoint = 0
    print('\n in sentences:')
    for i in globalPoints:
        if(i < start):
            prevPoint = i+1
            continue
        elif (i > end):
            print('Nothing :(')
            break
        else:
            print("Letters: " + str(lettersCounter(prevPoint, i)))
            print("Words: " + str(wordsCounter(prevPoint, i)))


def everyParagraph():
    startPoint = 0
    globalPointRegister(0, len(text))
    pointRegister(0, len(text))
    paragraphCounter()
    for i in paragraphsEnd:
        print("Letters: " + str(lettersCounter(startPoint, i)))
        print("Words: " + str(wordsCounter(startPoint, i)))
        print("Sentences: " + str(pointRegister(startPoint, i)))
        inSentences(startPoint, i)
        startPoint = i+1
        print("Paragraph ends at " + str(startPoint))
        print()
    print("Symbols in text: " + str(len(text)))

def textToNumbers(newText):
    for i in ruLetters:
        s = str(ruLetters[i])
        print(str(s))
        newText.replace(i, str(s))



#sentences = pointRegister()
#words = wordsCounter()
#letters = lettersCounter(0, 257)
#paragraph = paragraphCounter()
#print("sentences = ", sentences)
#print("words = ", words)
#print("letters = ", letters)
#print("paragraphs = ", paragraph)


#everyParagraph()
textToNumbers(newText)
print(newText)