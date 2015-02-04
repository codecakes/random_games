"""
Speak out the Sentence in revese.
Reverse a simple sentence with a full stop.
Doesn't account for space difference if there are other
punctuations. Might work on it if I feel like.Anyway, the point of
making this is not that it can't be easily done in C or Golang
but instead of using string.split() and reverse and join and blaah,
just wanted to manually fit in and strip away those extra spaces while
speaking the sentence in reverse!
"""


def clean_string(word):
    tmp_w = ''
    for let in word:
        if tmp_w:
            if tmp_w[-1] == '.':
                tmp_w += ' ' + let
                continue
        tmp_w += let
    return tmp_w


def rev_string(input_word):
    """
    Reverse a string/sentence.

    rev_string("I.am what aye yam.")
    '.yam aye what am I.'

    rev_string(".I.am what aye yam.")
    '.yam aye what am I. .'
    """
    store = ""
    parser = ""
    if len(input_word):
        word = clean_string(input_word)
        for ptr in xrange(len(word)-1,-2,-1):
            if ptr >= 0: w = word[ptr]
            if (w == " " and len(parser)) or ptr==-1:
                if parser[0] == '.':
                    store += '.'+parser[1:][::-1]
                else:
                    store = store.strip() + " " + parser[::-1]
                parser = ""
            parser += w
            #print "ptr %s w %s parser %s parser len %s store %s" %(ptr, w, repr(parser), len(parser), repr(store))
        #print repr(store.strip())
        del parser, word
        return (store.strip())
