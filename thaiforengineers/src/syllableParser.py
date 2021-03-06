#-*-coding: utf-8 -*-

from enum import Enum

class SyllableParser(object):

# -n	-น, -ณ, -ญ, -ร, -ล, -ฬ
# -ng	-ง
# -m	-ม
#
# 2 More Live Endings
# -y	-ย
# -w	-ว

    #standardizes the labels applied to letters, a letter can have multiple descriptors
    class CharDescriptor(Enum):
        consonant = 1
        vowel = 2
        tone_modifier = 3
        high_class = 4
        mid_class = 5
        low_class = 6
        long_vowel = 7
        short_vowel = 8

    consonants = [u'\u0e01', u'\u0e02', u'\u0e03', u'\u0e04', u'\u0e05', u'\u0e06', u'\u0e07', u'\u0e08', u'\u0e09',
                  u'\u0e0A', u'\u0e0B', u'\u0e0C', u'\u0e0D', u'\u0e0E', u'\u0e0F',
                  u'\u0e11', u'\u0e12', u'\u0e13' u'\u0e14', u'\u0e15', u'\u0e16', u'\u0e17', u'\u0e18', u'\u0e19',
                  u'\u0e1A', u'\u0e1B', u'\u0e1C', u'\u0e1D', u'\u0e1E', u'\u0e1F',
                  u'\u0e21', u'\u0e22', u'\u0e23', u'\u0e24', u'\u0e25', u'\u0e26', u'\u0e27', u'\u0e28',
                  u'\u0e2A', u'\u0e2B', u'\u0e2C', u'\u0e2D', u'\u0e2E']

    live_consonant_endings = [u'\u0e19', u'\u0e13', u'\u0e0d', u'\u0e23', u'\u0e25', u'\u0e2c', u'\u0e07', u'\u0e21', u'\u0e22', u'\u0e27']

    #ข, ฉ, ฐ, ถ, ผ, ฝ, ศ, ษ, ส, ห
    high_class_consonants = [u'\u0e02', u'\u0e09', u'\u0e10', u'\u0e16', u'\u0e1c', u'\u0e1d', u'\u0e28', u'\u0e29', u'\u0e2a', u'\u0e2b']

    mid_class_consonants = [u'\u0e01', u'\u0e08', u'\u0e0e', u'\u0e0f', u'\u0e15', u'\u0e1a', u'\u0e1b', u'\u0e2d']

    low_class_consonants = [u'\u0e04', u'\u0e06', u'\u0e07', u'\u0e0a', u'\u0e0b', u'\u0e0c', u'\u0e0d', u'\u0e11', u'\u0e12', u'\u0e13', ]

    vowels = [u'\u0e2F', u'\u0e31', u'\u0e32',u'\u0e33', u'\u0e34', u'\u0e35', u'\u0e36', u'\u0e37', u'\u0e38', u'\u0e39', u'\u0e3A',
              u'\u0e40', u'\u0e41', u'\u0e42', u'\u0e43', u'\u0e44', u'\u0e45', u'\u0e46', u'\u0e47', u'\u0e48',u'\u0e49',
              u'\u0e4A', u'\u0e4B',  u'\u0e4C',  u'\u0e4D', u'\u0e4E']

    short_vowels = [u'\u0e30', u'\u0e34', u'\u0e36', u'\u0e38', u'\u0e44', u'\u0e43']

    long_vowels = [u'\u0e32', u'\u0e35', u'\u0e40', u'\u0e41', u'\u0e39', u'\u0e42', u'\u0e2d', u'\u0e17', u'\u0e18', u'\u0e19', u'\u0e1e', u'\u0e1f', u'\u0e20', u'\u0e21', u'\u0e22', u'\u0e23', u'\u0e25', u'\u0e27', u'\u0e2c', u'\u0e2e']

    #long complex: อือ, เออ, อัว, เอีย, เอือ, ฤา, ฦา

    # edge: เอะ (short), แอะ (short), โอะ (short), เอาะ short, when is อ a vowel?, เออะ short, เอียะ short, เอือะ short, อัวะ short, ฤ EU (short-vowel???), 6. ฤา REEUU (short), อำ short, เอา short

    #need to look for complex characters first?

    tone_modifiers = [u'\u0e47', u'\u0e48', u'\u0e49', u'\u0e4A', u'\u0e4B']

    #short vowels
    #tone modifier transform dict

    def is_live_syllable(self, syllable):
        #see if there is a short vowels or live consonant ending-> are these last in unicode anyways
        last = self.final_sound(syllable)
        return last in self.short_vowels or last in self.live_consonant_endings

    def is_dead_syllable(self, syllable):
        return not self.is_live_syllable(self, syllable)

    #When a syllable does not have a final consonant, it is called open—the pronunciation of the vowel ends the pronunciation of the syllable. If there is a final consonant, the syllable is called closed.
    def is_open_syllable(self, syllable):
        last = self.final_sound(syllable)
        return last in self.vowels

    def is_closed_syllable(self):
        return not self.is_open_syllable()

    def first_consonant(self, syllable):
        for l in syllable:
            if l in self.consonants:
                return l

    #top and bottom joining vowels follow consantants
    def final_sound(self, syllable):
        for ch in syllable.reverse():
            if ch in self.vowels or self.consonants: #don't return tone markers
                return ch

    #needs to include super character
    def is_valid_character(self, ch):
        return self.is_vowel(ch) or self.is_consonant(ch) or self.is_tone_modifier(ch)

    def is_vowel(self, ch):
        return ch in self.vowels

    def is_consonant(self, ch):
        return ch in self.consonants

    def is_tone_modifier(self, ch):
        return ch in self.tone_modifiers

    def is_high_class(self, ch):
        return ch in self.high_class_consonants

    def is_low_class(self, ch):
        return ch in self.low_class_consonants

    def is_mid_class(self, ch):
        return ch in self.mid_class_consonants

    def is_long_vowel(self, ch):
        return ch in self.long_vowels

    def is_short_vowel(self, ch):
        return ch in self.short_vowels

    def get_consonant_class(self, ch):
        if self.is_high_class(ch):
            return self.CharDescriptor.high_class
        elif self.is_low_class(ch):
            return self.CharDescriptor.low_class
        elif self.is_mid_class(ch):
            return self.CharDescriptor.mid_class

    def get_vowel_length(self, ch):
        if self.is_long_vowel:
            return self.CharDescriptor.long_vowel
        elif self.is_short_vowel:
            return self.CharDescriptor.short_vowel

    def label_char(self, ch):
        descriptors = ()
        is_vowel, is_consonant, is_tone_modifier = self.is_vowel(ch), self.is_consonant(ch), self.is_tone_modifier(ch)
        if is_vowel:
            descriptors.append(self.CharDescriptor.vowel)
            descriptors.append(self.get_vowel_length(ch))
        elif is_consonant:
            descriptors.append(self.CharDescriptor.consonant)
            descriptors.append(self.get_consonant_class(ch))
        elif is_tone_modifier: #should return type of descriptor?
            descriptors.append(self.CharDescriptor.tone_modifier)
        return descriptors

    def predict_tone(self):
        pass

    def generate_facts(self, syllable):
        #consonants
        #vowels
        #leading letter
        #short, long vowel
        #live dead syllable
        #transform of modifier
        pass

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

    #break words into parts, in order of unicode representation
    #syllable: word, open: true/false, live: true/false, predictedTone: tone, letters: [{letter: letter, character_type, class: (high/low/short/long)}]
    #add list of chracters, grouping mega character as one
    def label_parts(self, syllable):
        pass

def _main():
    p = SyllableParser()
    p.test()

if __name__ == "__main__":
    _main()