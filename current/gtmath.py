import gttunings

def standardCalc(note):
    root = gttunings.getRoot(note)
    standardHz = [int(root), int(root*1.3347894672), int(root*1.7817012498), int(root*2.3783521417), int(root*2.9964810095), int(root*4)]
    return standardHz

def dropCalc(note):
    root = gttunings.getRoot(note)
    dropHz = [int(root), int(root*1.4982293652), int(root*2), int(root*2.6695723236), int(root*3.3633887224), int(root*4.4896485971)]
    return dropHz