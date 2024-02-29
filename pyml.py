from tkinter import *
from tkinter import ttk
import sys
import importlib

def runRestAsPython(page):
    exec(page, globals())

def parse(root, page):
    reader = ""
    finished = False
    inParenthesis = False
    readingContent = False
    currentAttrValue = ""
    currentContent = ""
    allCurrentAttrs = []
    readingTag = False
    counter = 0
    for char in str.replace(page, '\n', ' '):
        if finished:
            break
        counter += 1
        ignoreChar = False
        if(str.__contains__(reader, "@py")):
            runRestAsPython(page[counter:-1])
            finished = True
        match char:
            case "<":
                if readingContent:
                    currentContent = reader[1:-1]
                #print("opening tag")
                ignoreChar = True
                readingTag = True
                readingContent = False
                reader = ""
            case " ":
                if readingTag:
                    readingTag = False
                    ignoreChar = True
                    if reader.startswith("/"):
                        CreateTag(root, currentTagName, currentContent, allCurrentAttrs)
                        allCurrentAttrs = []
                        print("closed tag", currentTagName)
                        currentTagName = ""
                    else:
                        currentTagName = reader
                        reader = ""
                        print("created tag", currentTagName)

            case ">":
                if readingTag:
                    readingTag = False
                    ignoreChar = True
                    if reader.startswith("/"):
                        CreateTag(root, currentTagName, currentContent, allCurrentAttrs)
                        allCurrentAttrs = []
                        print("closed tag", currentTagName)
                        currentTagName = ""
                    else:


                        if currentTagName == "":
                            readingContent = True
                            currentTagName = reader
                        print("created tag", currentTagName)
            case "=":
                currentAttrName = reader.replace("\"", "") .strip()
                reader = ""
                ignoreChar = True
                #print("Starting new attribute:", currentAttrName)
            case "\"":
                if inParenthesis:
                    inParenthesis = False
                    if not currentAttrName == "":
                        currentAttrValue = reader.replace("\"", "") .strip()
                        reader = ""
                        allCurrentAttrs.append([currentAttrName, currentAttrValue])
                        print(f"Registered attr '{currentAttrName}' with value '{currentAttrValue}'")
                        currentAttrName = ""
                    inParenthesis = False
                    reader = ""
                else:
                    inParenthesis = True

        if not ignoreChar:
            reader += char

def CreateTag(root, tagName, tagContent, tagAttributes=[]):
    match tagName:
        case "p":
            a = Label(root, text=tagContent)
            a.pack()
        case "button":
            command = GetAttr(tagAttributes, "onclick", "print('hello world')")
            print(command)
            btn = Button(root, text=tagContent, bd="5", command=lambda: exec(command, globals()))
            btn.pack(side="top")
        case "meta":
            if GetAttr(tagAttributes, "doctype", "") != "pyml-1":
                print("Error: Version mismatch (document should be using pyml-1)")
                sys.exit()
            x = GetAttr(tagAttributes, "window-x", 100)
            y = GetAttr(tagAttributes, "window-y", 100)

            root.geometry(f"{x}x{y}")
            root.title(GetAttr(tagAttributes, "title", "Home"))
        case "py":
            print(tagContent)
            lambda: exec (tagContent)
        case "script":
            package = GetAttr(tagAttributes, "href", "")
            globals()[package] = importlib.import_module(package)

def GetAttr(attrs, attrName, default):
    for attr in attrs:
        if(attr[0]==attrName):
            return attr[1]
    return default