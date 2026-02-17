def count_words(filename):
    f = open(filename, "r")
    text = f.read()
    f.close()

    words = text.split()
    return len(words)

