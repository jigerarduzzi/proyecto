from dataCleaner import cleanText

def clasificarLeyes(lgr_pipeline):

    f = open("./Leyes/BoraBora_2022718_Ley1.txt")
    lines = f.readlines()
    lawText=""
    for line in lines:
        lawText=lawText+line
    #print(cleanText(line))
    return lgr_pipeline.predict([cleanText(lawText)])