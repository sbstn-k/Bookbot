def count(text: str):
    
    arr = text.split()

    return len(arr)


def count_chars(text):

    dic = {}

    for char in text:
        x = char.lower()
        if x in dic:
            dic[x]+=1
        else:
            dic[x]=1

    return dic

def sort_on(items):
    return items["num"]


def sort_dict(dic: dict):

    final_dic: list = []

    for val in dic:
        final_dic.append({"char": val, "num": dic[val]})
    
    final_dic.sort(reverse=True, key=sort_on)

    return final_dic


    






    
