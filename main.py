def main():
    book_path = "books/frankenstein.txt"
    report(book_path)
    
    

def book_text(p):
    with open(p) as f:
        return f.read()

def count(text):
    words = text.split()
    return len(words)

def sort_on(dict):
    return dict["occurance"]

def text_dict(text):
    dic_count = {}
    list_dic = []
    for l in text:
        if l.isalpha():
            l = l.lower()
            if l in dic_count:
                dic_count[l] += 1
            else: dic_count[l] = 1
    for k,v in dic_count.items():
        list_dic.append({"letter": k,"occurance": v})
    list_dic.sort(reverse=True, key =sort_on)
    return (list_dic)

def report(path):
    b_txt = book_text(path)
    b_wcount = count(b_txt)
    b_dic = text_dict(b_txt)
    print("--- report of {0} ---".format(path))
    print("{} words found in the documnet".format(b_wcount))
    print()
    for d in b_dic:
        letter = d["letter"]
        occurance = d["occurance"]
        print("The {} character was found {} times".format(letter,occurance))
    print("--- End report ---")
main()