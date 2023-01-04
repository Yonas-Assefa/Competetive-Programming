class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:

        duplicateFiles = defaultdict(list)
        ans = []

        for path in paths:
            splitedPath = path.split(" ")
            splitedPathLength = len(splitedPath)

            for i in range(1, splitedPathLength):
                files = splitedPath[i]
                splitedFile = files.split("(")
                fileContent = splitedFile[1][: -1]
                filePath = splitedPath[0] + "/" + splitedFile[0]
                duplicateFiles[fileContent].append(filePath)

        for filePath in duplicateFiles:
            if len(duplicateFiles[filePath]) >= 2:
                ans.append(duplicateFiles[filePath])

        return ans



                

       


