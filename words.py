def fetch_words():
    from urllib.request import urlopen
    story = urlopen('http://sixty-north.com/c/t.txt')  # comes in bytecode not list. e.g b'Olumide Oni'
    story_words = []  # creates an empty list
    for line in story:
        # the line below changes b'olumide oni' into 'olumide oni' and the split splits the word and put in a list
        line_words = line.decode('utf-8').split()  # separate every word in the line and places in list
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def print_words(a):
    for word in a:
        print(word)


def main():
    rslt = fetch_words()
    print_words(rslt)


if __name__ == "__main__":
    main()
