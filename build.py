import operator


def solution_asc(dic):
    dic=sorted(dic.items())
    return dic


def solution_desc(dic):
    dic=sorted(dic.items(),reverse=True)
    return dic
