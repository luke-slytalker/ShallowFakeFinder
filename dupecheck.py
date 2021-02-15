
def dupecheck_size(listOfElems):
    ''' Check if given list contains any duplicates '''
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True


def dupecheck_find(listOfElems):
    ''' Check if given list contains any duplicates '''
    setOfElems = set()
    dupes = []
    trip = 0
    for elem in listOfElems:
        if elem in setOfElems:
            trip += 1
            dupes.append(elem)
        else:
            setOfElems.add(elem)
    return dupes


def dupecheck_any(listOfElems):
    ''' Check if given list contains any duplicates '''
    for elem in listOfElems:
        if listOfElems.count(elem) > 1:
            return True
    return False
