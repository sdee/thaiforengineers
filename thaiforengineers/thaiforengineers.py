#-*-coding: utf-8 -*-

class Parser(object):

    live_constant_endings = []

    #tone modifier transform dict

    def is_live_syllable(self, syllable):
        #see if there is a short vowels or live consonant ending
        pass

    def is_dead_syllable(self):
        return not self.is_live_syllable(self)

    def is_open_syllable(self):
        pass

    def is_closed_syllable(self):
        pass

    def ends_with_consonant(self):
        pass

    def is_character(self):
        pass

    def is_vowel(self):
        pass

    def is_consonant(self):
        pass

    def is_high_class(self):
        pass

    def is_low_class(self):
        pass

    def is_mid_class(self):
        pass

    def is_tone_modifier(self):
        pass

    def predict_tone(self):
        pass

    def generate_facts(self):
        pass

    # advanced

    #looks to see if consonant is beginning or end, read in tsv exported from spreadsheet
    def sound(self):
        pass

    #return sound hint based on other words
    def sound_reminder(self):
        pass

    def test(self):
        for c in self.consonants:
            print unicode(c)
            print unicode(c) in u'ข'

        print u'ข' in self.consonants

def _main():
    p = Parser()
    p.test()

if __name__ == "__main__":
    _main()