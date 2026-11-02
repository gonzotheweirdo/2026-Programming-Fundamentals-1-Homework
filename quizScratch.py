classA = {101, 102, 103, 104, 105}
classB = {104, 105, 106, 107, 108}

def goDisplay(set1, set2):
    commonClasses = set1.intersection(set2)
    return commonClasses

print(goDisplay(classA, classB))

