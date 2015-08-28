#Remove HTML Tags from plaintext

# When we add our words to the index, we don't really want to include
# html tags such as <body>, <head>, <table>, <a href="..."> and so on.

# Write a procedure, remove_tags, that takes as input a string and returns
# a list of words, in order, with the tags removed. Tags are defined to be
# strings surrounded by < >. Words are separated by whitespace or tags. 
# You may assume the input does not include any unclosed tags, that is,  
# there will be no '<' without a following '>'.


def remove_tags(s):
    r = []
    word = ''
    on = False
    for w in s:
        if w=='<':
            on = True
        if not on and w not in ("\n"):
            if (w==" "):
                if word:
                    r.append(word)
                    word = ''
            else:
                word += w
        if w == '>':
            on = False
            if word and word != '':
                r.append(word)
                word = ''
    if word: r.append(word)
    return r
        
        


assert remove_tags('''<h1>Title</h1><p>This is a
                    <a href="http://www.udacity.com">link</a>.<p>''') == \
                    ['Title','This','is','a','link','.']

assert remove_tags('''<table cellpadding='3'>
                     <tr><td>Hello</td><td>World!</td></tr>
                     </table>''') == \
                     ['Hello','World!']

assert remove_tags("<hello><goodbye>") == []

assert remove_tags("This is plain text.") == ['This', 'is', 'plain', 'text.']

assert remove_tags("This sentence has no tags.") == \
['This', 'sentence', 'has', 'no', 'tags.']