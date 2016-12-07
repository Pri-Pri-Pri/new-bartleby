import re
from sys import exit
from random import choice

class Neue:
    def __init__(self):
        self.bartleby_text = open('bartleby.txt', 'r')

    def replace_stuff(self, line, substitutions):
        # replace specific words with the new word in a line
        # for all substitutions provided.
        for sub in substitutions:
            to_be_replaced = sub[0]
            replacement = sub[1]
            line = re.sub(to_be_replaced, replacement, line)
        return line.strip()

    def run(self):
        # turns everyone into a fox.
        print "Would you like the characters in Bartleby, the Scrivener:"
        print "A Story of Wall Street to be foxes instead?"

        choice = raw_input("Decision: ").lower()
        if "y" in choice:
            print "Sure thing, here you go:"
            for line in self.bartleby_text:
                transformed_line = self.replace_stuff(line,
                        [(r'\bhim\b', 'her'),(r'\bHim\b', 'Her'),
                        (r'\bhimself\b', 'herself'),(r'\bHimself\b', 'Herself'),
                        (r'\bhe\b', 'she'), (r'\bHe\b', 'She'),
                        (r'\bhis\b', 'her'), (r'\bHis\b', 'Her'),
                        (r'man\b', 'fox'), (r'Man\b', 'Fox'),
                        (r'\bgentlemen\b', 'fancy-foxes'), (r'\bGentlemen\b', 'Fancy-foxes'),
                        (r'\bgentleman', 'fancy-fox'), (r'\bGentleman', 'Fancy-fox'),
                        (r'\bmen\b', 'foxes'), (r'\bMen\b', 'Foxes'),
                        (r'\bwoman\b', 'fox'), (r'\bWoman\b', 'Foxes'),
                        (r'\bwomen\b', 'foxes'), (r'\bWomen\b', 'Foxes'),
                        (r'\blad\b', 'pup'), (r'\bLad\b', 'Pup'),
                        (r'\bboy\b', 'intern'), (r'\bBoy\b', 'Intern'),
                        (r'\bfellow\b', 'animal'), (r'\bFellow\b', 'Animal'),
                        (r'\bperson\b', 'creature'), (r'\bPerson\b', 'Creature'),
                        (r'\bpersons\b', 'creatures'), (r'\bPersons\b', 'Creatures'),
                        (r'\bsir\b', 'bushy-tailed one'), (r'\bSir\b', 'Bushy-tailed one'),
                        (r'\bhumanity\b', 'the ecosystem'), (r'\bHumanity\b', 'The ecosystem'),
                        (r'\bhumanizing\b', 'anthropomorphizing'), (r'\bHumanizing\b', 'Anthropomorphizing'),
                     ])

                print transformed_line
        else:
            self.next_option()

    def next_option(self):
        # Bartleby goes missing from the text.
        print "What about deleting every line where"
        print "Bartleby is mentioned?"

        choice = raw_input("Decision: ").lower()
        if "y" in choice:
            print "OK, let's try it:"
            for line in self.bartleby_text:
                line = line.strip()
                if "Bartleby" in line:
                    print ". . . . . . . . . . . . . . . . . . . . . . . . . . Bartleby was here."
                else:
                    print line
        else:
            self.bye_poem()

    def bye_poem(self):
        adj = "salty transparent sea-green delicate expected vacant inevitable".split()
        noun = "screen silence public wave repetition good-bye".split()
        prep = "towards from into between for across".split()
        verb = "praying departing leaving desiring unfurling".split()
        adverb = "silently instantly".split()
        deter = "more less yes no".split()

        print "\n" + " " * 27 + " [bye now] " + " " * 27
        print "\n"
        line0 = " ".join(["the randomness", choice(prep), "this", choice(noun), "is", choice(adj) + ", in some ways."])
        line1 = " ".join(["in others,"])
        line2 = " " * 11 + choice(adj) + "."
        line3 = " ".join(["this", choice(noun), "is randomly", choice(adj) + " " * 17 + " as is"])
        line4 = " ".join(["the", choice(noun), "of the", choice(noun), choice(prep), "the", choice(noun) + "."])
        line5 = " ".join([choice(adverb) + ", this computer was", choice(verb) + ":", choice(deter), choice(noun) + ",", choice(deter), choice(noun) + "."])
        line6 = " ".join(["to be both", choice(verb), choice(prep), "and", choice(verb), choice(prep), "a", choice(noun) + ","])
        line7 = " ".join(["\t", choice(verb), choice(verb), choice(verb) + " " * 8 + choice(prep), "a", choice(noun) + "."])
        line8 = " ".join(["is it", choice(verb), choice(prep), "a", choice(noun) + "? yes, the", choice(noun), "is", choice(verb) + "."])
        lines = [line0, line1, line2, line3, line4, line5, line6, line7, line8]

        # iterate over an array and get back the index
        # and the item for that given index.
        for index, line in enumerate(lines):
            if index == 4 or index == 5 or index == 7 or index == 8:
                print(line)
                print("\n")
            else:
                print(line)

Neue().run()
