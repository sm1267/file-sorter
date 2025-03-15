import os
import shutil

def createFolder(path: str, extension: str) -> str:
    folderName: str = extension[1:]
    folderPath: str = os.path.join(path, folderName)

    if not os.path.exists(folderPath):
        os.makedirs(folderPath)

    return folderPath


def sortFiles(sourcePath: str):

    for rootDir, subDir, filenames in os.walk(sourcePath):
        for filename in filenames:
            filePath: str = os.path.join(rootDir, filename)
            extension: str = os.path.splitext(filename)[1]

            if extension:
                targetFolder: str = createFolder(sourcePath, extension)
                targetPath: str = os.path.join(targetFolder, filename)

                shutil.move(filePath, targetPath)

def removeEmptyFolders(sourcePath: str):
    for rootDir, subDir, filenames in os.walk(sourcePath, topdown=False):
        for currentDir in subDir:
            folderPath: str = os.path.join(rootDir, currentDir)

            if not os.listdir(folderPath):
                os.rmdir(folderPath)

def main():
    userInput: str = input('File Path: ')

    if os.path.exists(path=userInput):
        sortFiles(userInput)
        removeEmptyFolders(userInput)
        print('Sorted')
    else:
        print('Invalid path')

if __name__ == '__main__':
    main()