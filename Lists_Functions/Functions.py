def find_equals(vectorA, vectorB):
    vectorC = []

    for index in range(0, len(vectorA)):
        for index2 in range(0, len(vectorB)):
            if vectorA[index] == vectorB[index2]:
                vectorC.append(vectorA[index])
            index2 += 1
    index += 1
    return vectorC
