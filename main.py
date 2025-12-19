from stats import *
import sys



def get_book_text(path_to_file):

    with open(path_to_file) as f:
        file_content = f.read()

    return file_content





def main():

    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    
    book_path = sys.argv[1]

    str = get_book_text(book_path)

    num = count(str)
    # print(f"Found {num} total words")

    char_num = count_chars(str)
    
    sorted_list = sort_dict(char_num)

    #
    #  print(char_num)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num} total words")
    print("--------- Character Count -------")
    for val in sorted_list:
        if val["char"].isalpha(): 
            print(f"{val["char"]}: {val["num"]}")
    print("============= END ===============")

main()