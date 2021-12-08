
entries = []
globalSum = 0

class Entry:
    def __init__(self,segments,output):
        self.segments = segments
        self.output = output
        self.display = ['','','','','','','']

f = open("input.txt","r")
for line in f:
    
    line = line.replace('\n', '')
    delim = line.split(" | ")

    words = delim[1].split(" ")
    segments = delim[0].split(" ")
    entries.append(Entry(segments,words))

knownSegments = [2,3,4,7]

for entry in entries:
    possibilities = []
    for x in knownSegments:
        for seg in entry.segments:
            if len(seg) == x:
                if x == 2:
                    possibilities.append(['','',seg[0],'','',seg[1],''])
                    possibilities.append(['','',seg[1],'','',seg[0],''])

                if x == 3:
                    for p in possibilities:
                        for s in seg:
                            if not s in p:
                                p[0] = s

                if x == 4:
                    newPossibilities = []
                    for p in possibilities:
                        newSegments = []
                        for s in seg:
                            if not s in p:
                                newSegments.append(s)
                        newPossibilities.append([p[0],newSegments[0],p[2],newSegments[1],'',p[5],''])
                        newPossibilities.append([p[0],newSegments[1],p[2],newSegments[0],'',p[5],''])
                    possibilities = newPossibilities

                if x == 7:
                    newPossibilities = []
                    for p in possibilities:
                        newSegments = []
                        for s in seg:
                            if not s in p:
                                newSegments.append(s)
                        newPossibilities.append([p[0],p[1],p[2],p[3],newSegments[0],p[5],newSegments[1]])
                        newPossibilities.append([p[0],p[1],p[2],p[3],newSegments[1],p[5],newSegments[0]])
                    possibilities = newPossibilities

    solution = []
    #test each possibility
    for p in possibilities:
        possibleSolution = ["","","","","","","","","",""]
        for seg in entry.segments:

            if len(seg) == 2:
                possibleSolution[1] = seg
            if len(seg) == 3:
                possibleSolution[7] = seg
            if len(seg) == 4:
                possibleSolution[4] = seg
            if len(seg) == 7:
                possibleSolution[8] = seg

            if len(seg) == 6:# 0, 6, or 9
                if not p[3] in seg:
                    #zero
                    possibleSolution[0] = seg
                elif not p[2] in seg:
                    #6
                    possibleSolution[6] = seg
                elif not p[4] in seg:
                    #9
                    possibleSolution[9] = seg

            if len(seg) == 5:
                if not p[5] in seg:
                    #2
                    possibleSolution[2] = seg
                elif not p[1] in seg and not p[4] in seg:
                    #3
                    possibleSolution[3] = seg
                elif not p[2] in seg:
                    #5
                    possibleSolution[5] = seg

        if not "" in possibleSolution:
            solution = possibleSolution

    decodedOut = ''
    for out in entry.output:
        for i in range(len(solution)):
            if set(out) == set(solution[i]):
                decodedOut += str(i)

    globalSum += int(decodedOut)

print(globalSum)