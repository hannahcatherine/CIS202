mydict = {}

def main():
    input_name = input('Enter the name of the input file: ')

    input_file = open(input_name, 'r')
    text = input_file.read()
    words = text.split()

    unique_words = set(words)

    print('These are the unique words in the text:')
    for word in unique_words:
        print(word)

    for word in unique_words:
        mydict[word] = 0

    for item in words:
        mydict[item] += 1

    input_file.close()


main()
