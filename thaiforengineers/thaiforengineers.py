#-*-coding: utf-8 -*-

class Parser(object):

    live_constant_endings = []

    consonants = [u'\u0e01', u'\u0e02', u'\u0e03', u'\u0e04', u'\u0e05', u'\u0e06', u'\u0e07', u'\u0e08', u'\u0e09',
                  u'\u0e0A', u'\u0e0B', u'\u0e0C', u'\u0e0D', u'\u0e0E', u'\u0e0F',
                  u'\u0e11', u'\u0e12', u'\u0e13' u'\u0e14', u'\u0e15', u'\u0e16', u'\u0e17', u'\u0e18', u'\u0e19',
                  u'\u0e1A', u'\u0e1B', u'\u0e1C', u'\u0e1D', u'\u0e1E', u'\u0e1F',
                  u'\u0e21', u'\u0e22', u'\u0e23', u'\u0e24', u'\u0e25', u'\u0e26', u'\u0e27', u'\u0e28',
                  u'\u0e2A', u'\u0e2B', u'\u0e2C', u'\u0e2D', u'\u0e2E']

    vowels = [u'\u0e2F', u'\u0e31', u'\u0e32',u'\u0e33', u'\u0e34', u'\u0e35', u'\u0e36', u'\u0e37', u'\u0e38', u'\u0e39', u'\u0e3A',
              u'\u0e40', u'\u0e41', u'\u0e42', u'\u0e43', u'\u0e44', u'\u0e45', u'\u0e46', u'\u0e47', u'\u0e48',u'\u0e49',
              u'\u0e4A', u'\u0e4B',  u'\u0e4C',  u'\u0e4D', u'\u0e4E']

    #short vowels
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

        print "-----------"
        for v in self.vowels:
            print unicode(v)

    def label_parts_of_syllable(self):
        pass

def _main():
    p = Parser()
    p.test()

if __name__ == "__main__":
    _main()