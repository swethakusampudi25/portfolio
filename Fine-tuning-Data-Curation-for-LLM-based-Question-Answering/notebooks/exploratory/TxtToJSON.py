# Convert txt files to json files
import json
# import re
# import spacy

def TripleFromOneLine(line):
    oneTriple = {"instruction": "Answer the question truthfully", "input":"", "output":"" } 
    if not "?" in line:
        return oneTriple
    line2 = str(line).replace('"question": ', '').replace('"answer": ', '').replace('"q": ', '').replace('"a": ', '').replace('{', '').replace('}', '').replace('"', '').replace(',', '')
    # print(f"line2 is {line2}.")
    words = line2.split("?")
    if len(words)<2:
        return oneTriple
    wBefore = str(words[0]).strip()
    wAfter  = str(words[1]).strip()     
    if len(wBefore)>3 and len(wAfter)>0:  
        oneTriple = {"instruction": "Answer the question truthfully", "input": wBefore+"?", "output":wAfter } 
    return oneTriple

def TripleFromTwoLines(line, nextLine):
    oneTriple = {"instruction": "Answer the question truthfully", "input":"", "output":"" } 
    if not "?" in line:
        return oneTriple
    line2 = str(line).replace('"question": ', '').replace('"answer": ', '').replace('"q": ', '').replace('"a": ', '').replace('{', '').replace('}', '').replace('"', '').replace(',', '')
    nextLine2 = str(nextLine).replace('"question": ', '').replace('"answer": ', '').replace('"q": ', '').replace('"a": ', '').replace('{', '').replace('}', '').replace('"', '').replace(',', '')
 
    if len(line2)>3 and len(nextLine2)>0:  
        oneTriple = {"instruction": "Answer the question truthfully", "input": line2, "output":nextLine2 } 
    return oneTriple

  

def text2JSONFile(inputFile, outputFile):
    rf = open(inputFile, 'r', encoding="utf8")
    lines = rf.readlines() 
    rf.close()

    data = []
    for line in lines:
        if "?" in line:
            oneTriple = TripleFromOneLine(line)
            if len(oneTriple['input'])>0 and len(oneTriple['output'])>0:
                data.append(oneTriple)

    with open(outputFile, "w", encoding="utf8") as outfile:
        outfile.write('[') 
    outfile.close()

    with open(outputFile, "a") as outfile:
        d_amount = 0
        for d in data:
            d_amount += 1
        i = 0            
        for d in data:
            json.dump(d, outfile)
            i += 1
            if (i < d_amount):
                outfile.write(',') 
        outfile.write(']') 
    outfile.close()

def lines2JSONFile(inputFile, outputFile):
    rf = open(inputFile, 'r', encoding="utf8")
    lines = rf.readlines() 
    rf.close()
    lenlines = len(lines)
    print(f"lenlines = {lenlines}")
    data = []
    i = 0
    count = 0
    while i < lenlines:
        line = lines[i]
        if '?", "answer":'  in line:
            oneTriple = TripleFromOneLine(line)
            if len(oneTriple['input'])>0 and len(oneTriple['output'])>0:
                data.append(oneTriple)
                count += 1
        elif '?'  in line:
            i  += 1
            if i >= lenlines:
                break
            nextLine = lines[i]
            oneTriple = TripleFromTwoLines(line, nextLine)
            if len(oneTriple['input'])>0 and len(oneTriple['output'])>0:
                data.append(oneTriple)
                count += 1
        i += 1

    print(f"count = {count}")

    with open(outputFile, "w", encoding="utf8") as outfile:
        outfile.write('[') 
    outfile.close()

    with open(outputFile, "a") as outfile:
        d_amount = 0
        for d in data:
            d_amount += 1
        i = 0            
        for d in data:
            json.dump(d, outfile)
            i += 1
            if (i < d_amount):
                outfile.write(',') 
        outfile.write(']') 
    outfile.close()

lines2JSONFile("../../data/processed/EngineeringReference1_5_QAGPT4.txt", "../../data/processed/EngineeringReference1_5_QAGPT4.json")
lines2JSONFile("../../data/processed/EngineeringReference1_5_TESTQAGPT4omini.txt", "../../data/processed/EngineeringReference1_5_TESTQAGPT4omini.json")

