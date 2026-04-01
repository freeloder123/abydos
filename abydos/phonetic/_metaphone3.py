"""abydos.phonetic._metaphone3.

Metaphone 3
"""

# Copyright 2026 by OpenAI.
# This file is part of Abydos.
#
# Abydos is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Abydos is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Abydos. If not, see <http://www.gnu.org/licenses/>.
#
# Portions of this file are adapted from `dlclark/metaphone3`, licensed under
# the BSD 3-Clause License, which in turn is based on the BSD-licensed
# OpenRefine Metaphone 3 reference implementation by Lawrence Philips.

from __future__ import annotations

from ._phonetic import _Phonetic

__all__ = ['Metaphone3']

DEFAULT_MAX_LENGTH = 8
REPLACEMENT_CHAR = '\ufffd'


def isVowel(in_char: str) -> bool:
    return in_char in {
        'A', 'E', 'I', 'O', 'U', 'Y',
        'À', 'Á', 'Â', 'Ã', 'Ä', 'Å', 'Æ',
        'È', 'É', 'Ê', 'Ë',
        'Ì', 'Í', 'Î', 'Ï',
        'Ò', 'Ó', 'Ô', 'Õ', 'Ö', 'Ø',
        'Ù', 'Ú', 'Û', 'Ü', 'Ý',
        '\uC29F',
        '\uC28C',
    }


def rootOrInflections(in_word, root: str) -> bool:
    len_diff = len(in_word) - len(root)
    if len_diff < 0:
        return False
    last = len(root) - 1
    for i in range(last):
        if in_word[i] != root[i]:
            return False
    in_word = in_word[last:]
    if in_word[0] == root[last]:
        if len_diff == 0:
            return True
        elif len_diff == 1 and in_word[1] == 'S':
            return True
    if root[last] == 'E':
        if len_diff == 1 and in_word[0] == 'E' and in_word[1] == 'D':
            return True
        len_diff += 1
    else:
        if in_word[0] != root[last]:
            return False
        if len_diff == 2 and in_word[1] == 'E' and in_word[2] in {'S', 'D'}:
            return True
        in_word = in_word[1:]
    if len_diff == 3 and areEqual(in_word, list('ING')):
        return True
    elif len_diff == 5 and areEqual(in_word, list('INGLY')):
        return True
    elif len_diff == 1 and in_word[0] == 'Y':
        return True
    return False


def areEqual(buf1, buf2) -> bool:
    return buf1 == buf2


class Encoder:
    def __init__(self, encode_vowels: bool = False, encode_exact: bool = False, max_length: int = DEFAULT_MAX_LENGTH):
        self.encode_vowels = encode_vowels
        self.encode_exact = encode_exact
        self.max_length = max_length
        self.word = []
        self.idx = 0
        self.last_idx = 0
        self.prim_buf = []
        self.second_buf = []
        self.flag_al_inversion = False

    def Encode(self, in_: str):
        if in_ == '':
            return '', ''
        if self.max_length <= 0:
            self.max_length = DEFAULT_MAX_LENGTH
        self.flag_al_inversion = False
        self.word = [r.upper() for r in in_]
        self.last_idx = len(self.word) - 1
        self.prim_buf = []
        self.second_buf = []
        self.idx = 0
        while self.idx < len(self.word):
            if len(self.prim_buf) >= self.max_length and len(self.second_buf) >= self.max_length:
                break
            c = self.word[self.idx]
            if c == 'B':
                self.encodeB()
            elif c in {'ß', 'Ç'}:
                self.metaphAdd('S')
            elif c == 'C':
                self.encodeC()
            elif c == 'D':
                self.encodeD()
            elif c == 'F':
                self.encodeF()
            elif c == 'G':
                self.encodeG()
            elif c == 'H':
                self.encodeH()
            elif c == 'J':
                self.encodeJ()
            elif c == 'K':
                self.encodeK()
            elif c == 'L':
                self.encodeL()
            elif c == 'M':
                self.encodeM()
            elif c == 'N':
                self.encodeN()
            elif c == 'Ñ':
                self.metaphAdd('N')
            elif c == 'P':
                self.encodeP()
            elif c == 'Q':
                self.encodeQ()
            elif c == 'R':
                self.encodeR()
            elif c == 'S':
                self.encodeS()
            elif c == 'T':
                self.encodeT()
            elif c in {'Ð', 'Þ'}:
                self.metaphAdd('0')
            elif c == 'V':
                self.encodeV()
            elif c == 'W':
                self.encodeW()
            elif c == 'X':
                self.encodeX()
            elif c == '슊':
                self.metaphAdd('X')
            elif c == '슎':
                self.metaphAdd('S')
            elif c == 'Z':
                self.encodeZ()
            else:
                if isVowel(c):
                    self.encodeVowels()
            self.idx += 1
        if len(self.prim_buf) > self.max_length:
            self.prim_buf = self.prim_buf[:self.max_length]
        if len(self.second_buf) > self.max_length:
            self.second_buf = self.second_buf[:self.max_length]
        primary = ''.join(self.prim_buf)
        secondary = ''.join(self.second_buf)
        if primary == secondary:
            secondary = ''
        return primary, secondary

    def isSlavoGermanic(self) -> bool:
        return self.stringStart('SCH', 'SW') or self.word[0] in {'J', 'W'}

    def charNextIs(self, c: str) -> bool:
        return self.charAt(1, c)

    def isVowelAt(self, offset: int) -> bool:
        at = self.idx + offset
        if at < 0 or at >= len(self.word):
            return False
        return isVowel(self.word[at])

    def charAt(self, offset: int, c: str) -> bool:
        idx = self.idx + offset
        if idx < 0 or idx >= len(self.word):
            return False
        return self.word[idx] == c

    def stringAtStart(self, offset: int, *vals: str) -> bool:
        if offset != -self.idx:
            return False
        return self.stringAt(offset, *vals)

    def stringAtEnd(self, offset: int, *vals: str) -> bool:
        start = self.idx + offset
        if start < 0 or start >= len(self.word) or start + len(vals[0]) > len(self.word):
            return False
        for v in vals:
            last = start + len(v)
            inlen = len(self.word)
            if last > inlen:
                return False
            if last < inlen:
                continue
            ok = True
            for i, c in enumerate(v):
                if c != self.word[start + i]:
                    ok = False
                    break
            if ok:
                return True
        return False

    def stringAt(self, offset: int, *vals: str) -> bool:
        start = self.idx + offset
        if start < 0 or start >= len(self.word) or start + len(vals[0]) > len(self.word):
            return False
        for v in vals:
            if start + len(v) > len(self.word):
                return False
            ok = True
            for i, c in enumerate(v):
                if c != self.word[start + i]:
                    ok = False
                    break
            if ok:
                return True
        return False

    def stringStart(self, *vals: str) -> bool:
        return self.stringAt(-self.idx, *vals)

    def stringEnd(self, *vals: str) -> bool:
        for v in vals:
            idx = len(self.word) - len(v)
            if idx < 0:
                return False
            ok = True
            for c in v:
                if c != self.word[idx]:
                    ok = False
                    break
                idx += 1
            if ok:
                return True
        return False

    def stringExact(self, *vals: str) -> bool:
        for v in vals:
            if len(v) > len(self.word):
                return False
            elif len(v) < len(self.word):
                continue
            ok = True
            for i, c in enumerate(v):
                if c != self.word[i]:
                    ok = False
                    break
            if ok:
                return True
        return False

    def stringContains(self, val: str) -> bool:
        last_possible_start = len(self.word) - len(val)
        if last_possible_start < 0:
            return False
        for i in range(last_possible_start + 1):
            tmp = i
            for c in val:
                if self.word[tmp] != c:
                    break
                tmp += 1
            if tmp - i == len(val):
                return True
        return False

    def metaphAdd(self, in_char: str) -> None:
        self.metaphAddAlt(in_char, in_char)

    def metaphAddAlt(self, prim: str, second: str) -> None:
        if prim != REPLACEMENT_CHAR:
            if not (prim == 'A' and self.prim_buf and self.prim_buf[-1] == 'A'):
                self.prim_buf.append(prim)
        if second != REPLACEMENT_CHAR:
            if not (second == 'A' and self.second_buf and self.second_buf[-1] == 'A'):
                self.second_buf.append(second)

    def metaphAddStr(self, prim: str, second: str) -> None:
        if not (prim == 'A' and self.prim_buf and self.prim_buf[-1] == 'A'):
            self.prim_buf.extend(list(prim))
        if second != '' and not (second == 'A' and self.second_buf and self.second_buf[-1] == 'A'):
            self.second_buf.extend(list(second))

    def metaphAddExactApproxAlt(self, exact: str, altExact: str, main: str, alt: str) -> None:
        if self.encode_exact:
            self.metaphAddStr(exact, altExact)
        else:
            self.metaphAddStr(main, alt)

    def metaphAddExactApprox(self, exact: str, main: str) -> None:
        if self.encode_exact:
            self.metaphAddStr(exact, exact)
        else:
            self.metaphAddStr(main, main)

    def skipVowels(self, at: int) -> int:
        if at < 0:
            return 0
        if at >= len(self.word):
            return len(self.word)
        it = self.word[at]
        off = at - self.idx
        while isVowel(it) or it == 'W':
            if self.stringAt(off, 'WICZ', 'WITZ', 'WIAK') or self.stringAt(off - 1, 'EWSKI', 'EWSKY', 'OWSKI', 'OWSKY') or self.stringAtEnd(off, 'WICKI', 'WACKI'):
                break
            off += 1
            if self.charAt(off - 1, 'W') and self.charAt(off, 'H') and not self.stringAt(off, 'HOP', 'HIDE', 'HARD', 'HEAD', 'HAWK', 'HERD', 'HOOK', 'HAND', 'HOLE', 'HEART', 'HOUSE', 'HOUND', 'HAMMER'):
                off += 1
            if self.idx + off > self.last_idx:
                break
            it = self.word[self.idx + off]
        if off < 1:
            raise RuntimeError('bug: skipping vowels moving backward')
        return self.idx + off - 1

    def advanceCounter(self, noEncodeVowel: int, encodeVowel: int) -> None:
        if self.encode_vowels:
            self.idx += encodeVowel
        else:
            self.idx += noEncodeVowel

    def encodeB(self):
        if self.encodeSilentB():
            return



        self.metaphAddExactApprox("B", "P")


        if self.charNextIs('B')  or  (self.charNextIs('P')  and  self.idx+2 < len(self.word)  and  self.word[self.idx+2] != 'H'):
            self.idx += 1


    def encodeSilentB(self):

        if self.stringAt(-2, "DEBT", "SUBTL", "SUBTIL")  or  self.stringAt(-3, "DOUBT"):
            self.metaphAdd('T')
            self.idx += 1
            return True

        return False

    def encodeC(self):
        if self.encodeSilentCAtBeginning()  or  self.encodeCaToS()  or  self.encodeCoToS()  or  self.encodeCh()  or  self.encodeCcia()  or  self.encodeCc()  or  self.encodeCkCgCq()  or  self.encodeCFrontVowel()  or  self.encodeSilentC()  or  self.encodeCz()  or  self.encodeCs():
            return

        if not self.stringAt(-1, "C", "K", "G", "Q"):
            self.metaphAdd('K')


        if self.stringAt(1, " C", " Q", " G"):
            self.idx += 1
        else:
            if self.stringAt(1, "C", "K", "Q")  and  not self.stringAt(1, "CE", "CI"):
                self.idx += 1

                if self.stringAt(1, "C", "K", "Q")  and  not self.stringAt(2, "CE", "CI"):
                    self.idx += 1

    def encodeSilentCAtBeginning(self):
        if self.idx == 0  and  self.stringAt(0, "CT", "CN"):
            return True
        return False



    def encodeCaToS(self):


        if (self.idx == 0  and  self.stringAt(0, "CAES", "CAEC", "CAEM"))  or  self.stringStart("FACADE", "FRANCAIS", "FRANCAIX", "LINGUICA", "GONCALVES", "PROVENCAL"):
            self.metaphAdd('S')
            self.advanceCounter(1, 0)
            return True

        return False



    def encodeCoToS(self):

        if self.stringAt(0, "COEL")  and  (self.isVowelAt(4)  or  self.idx+3 == self.last_idx)  or  self.stringAt(0, "COENA", "COENO")  or  self.stringStart("GARCON", "FRANCOIS", "MELANCON"):

            self.metaphAdd('S')
            self.advanceCounter(2, 0)
            return True

        return False

    def encodeCh(self):
        if not self.stringAt(0, "CH"):
            return False

        if self.encodeChae()  or  self.encodeChToH()  or  self.encodeSilentCh()  or  self.encodeArch()  or  self.encodeChToX()  or  self.encodeEnglishChToK()  or  self.encodeGermanicChToK()  or  self.encodeGreekChInitial()  or  self.encodeGreekChNonInitial():
            return True

        if self.idx > 0:
            if self.stringStart("MC")  and  self.idx == 1:

                self.metaphAdd('K')
            else:
                self.metaphAddAlt('X', 'K')
        else:
            self.metaphAdd('X')

        self.idx += 1
        return True

    def encodeChae(self):

        if self.idx > 0  and  self.stringAt(2, "AE"):
            if self.stringStart("RACHAEL"):
                self.metaphAdd('X')
            elif not self.stringAt(-1, "C", "K", "G", "Q"):
                self.metaphAdd('K')

            self.advanceCounter(3, 1)
            return True

        return False





    def encodeChToH(self):

        if (self.idx == 0  and  (self.stringAt(2, "AIM", "ETH", "ELM", "ASID", "AZAN", "UPPAH", "UTZPA", "ALLAH", "ALUTZ", "AMETZ", "ESHVAN", "ADARIM", "ANUKAH", "ALLLOTH", "ANNUKAH", "AROSETH")))  or  self.stringAt(-3, "CLACHAN"):

            self.metaphAdd('H')
            self.advanceCounter(2, 1)
            return True

        return False

    def encodeSilentCh(self):
        if self.stringAt(-2, "YACHT", "FUCHSIA")  or  self.stringStart("STRACHAN", "CRICHTON")  or  (self.stringAt(-3, "DRACHM")  and  not self.stringAt(-3, "DRACHMA")):
            self.idx += 1
            return True

        return False

    def encodeChToX(self):

        if (self.stringAt(-2, "OACH", "EACH", "EECH", "OUCH", "OOCH", "MUCH", "SUCH")  and  not self.stringAt(-3, "JOACH"))  or  self.stringAtEnd(-1, "ACHA", "ACHO")  or  self.stringAtEnd(0, "CHOT", "CHOD", "CHAT")  or  (self.stringAtEnd(-1, "OCHE")  and  not self.stringAt(-2, "DOCHE"))  or  self.stringAt(-4, "ATTACH", "DETACH", "KOVACH", "PARACHUT")  or  self.stringAt(-5, "SPINACH", "MASSACHU")  or  self.stringStart("MACHAU")  or  (self.stringAt(-3, "THACH")  and  not self.stringAt(2, "E"))  or  self.stringAt(-2, "VACHON"):

            self.metaphAdd('X')
            self.idx += 1
            return True

        return False

    def encodeEnglishChToK(self):

        if (self.idx == 1  and  rootOrInflections(self.word, "ACHE"))  or  ((self.idx > 3  and  rootOrInflections(self.word[self.idx-1:], "ACHE"))  and  self.stringStart("EAR", "HEAD", "BACK", "HEART", "BELLY", "TOOTH"))  or  self.stringAt(-1, "ECHO")  or  self.stringAt(-2, "MICHEAL")  or  self.stringAt(-4, "JERICHO")  or  self.stringAt(-5, "LEPRECH"):

            self.metaphAddAlt('K', 'X')
            self.idx += 1
            return True

        return False

    def encodeGermanicChToK(self):



        if (self.idx > 1  and  not self.isVowelAt(-2)  and  self.stringAt(-1, "ACH")  and  not self.stringAt(-2, "MACHADO", "MACHUCA", "LACHANC", "LACHAPE", "KACHATU")  and  not self.stringAt(-3, "KHACHAT")  and  (not self.charAt(2, 'I')  and  (not self.charAt(2, 'E')  or  self.stringAt(-2, "BACHER", "MACHER", "MACHEN", "LACHER")))  or  (self.stringAt(2, "T", "S")  and  not (self.stringStart("LUNCHTIME", "WHICHSOEVER")))  or  self.stringStart("SCHR")  or  (self.idx > 2  and  self.stringAt(-2, "MACHE"))  or  (self.idx == 2  and  self.stringAt(-2, "ZACH"))  or  self.stringAt(-4, "SCHACH")  or  self.stringAt(-1, "ACHEN")  or  self.stringAt(-3, "SPICH", "ZURCH", "BUECH")  or  (self.stringAt(-3, "KIRCH", "JOACH", "BLECH", "MALCH")  and  not (self.stringAt(-3, "KIRCHNER")  or  self.idx+1 == self.last_idx))  or  self.stringAtEnd(-2, "NICH", "LICH", "BACH")  or  (self.stringAtEnd(-3, "URICH", "BRICH", "ERICH", "DRICH", "NRICH")  and  not self.stringAtEnd(-5, "ALDRICH")  and  not self.stringAtEnd(-6, "GOODRICH")  and  not self.stringAtEnd(-7, "GINGERICH")))  or  self.stringAtEnd(-4, "ULRICH", "LFRICH", "LLRICH", "EMRICH", "ZURICH", "EYRICH")  or  ((self.stringAt(-1, "A", "O", "U", "E")  or  self.idx == 0)  and  self.stringAt(2, "L", "R", "N", "M", "B", "H", "F", "V", "W", " ")):



            if self.stringAt(2, "R", "L")  or  self.isSlavoGermanic():
                self.metaphAdd('K')
            else:
                self.metaphAddAlt('K', 'X')
            self.idx += 1
            return True

        return False



    def encodeArch(self):
        if self.stringAt(-2, "ARCH"):


            if ((self.isVowelAt(2)  and  self.stringAt(-2, "ARCHA", "ARCHI", "ARCHO", "ARCHU", "ARCHY"))  or  self.stringAt(-2, "ARCHEA", "ARCHEG", "ARCHEO", "ARCHET", "ARCHEL", "ARCHES", "ARCHEP", "ARCHEM", "ARCHEN")  or  self.stringAtEnd(-2, "ARCH")  or  self.stringStart("MENARCH"))  and  (not rootOrInflections(self.word, "ARCH")  and  not self.stringAt(-4, "SEARCH", "POARCH")  and  not self.stringStart("ARCHER", "ARCHIE", "ARCHENEMY", "ARCHIBALD", "ARCHULETA", "ARCHAMBAU")  and  not ((((self.stringAt(-3, "LARCH", "MARCH", "PARCH")  or  self.stringAt(-4, "STARCH"))  and  not self.stringStart("EPARCH", "NOMARCH", "EXILARCH", "HIPPARCH", "MARCHESE", "ARISTARCH", "MARCHETTI"))  or  rootOrInflections(self.word, "STARCH"))  and  (not self.stringAt(-2, "ARCHU", "ARCHY")  or  self.stringStart("STARCHY")))):

                self.metaphAddAlt('K', 'X')
            else:
                self.metaphAdd('X')
            self.idx += 1
            return True

        return False

    def encodeGreekChInitial(self):

        if (self.stringAt(0, "CHAMOM", "CHARAC", "CHARIS", "CHARTO", "CHARTU", "CHARYB", "CHRIST", "CHEMIC", "CHILIA")  or  (self.stringAt(0, "CHEMI", "CHEMO", "CHEMU", "CHEMY", "CHOND", "CHONA", "CHONI", "CHOIR", "CHASM", "CHARO", "CHROM", "CHROI", "CHAMA", "CHALC", "CHALD", "CHAET", "CHIRO", "CHILO", "CHELA", "CHOUS", "CHEIL", "CHEIR", "CHEIM", "CHITI", "CHEOP")  and  not (self.stringAt(0, "CHEMIN")  or  self.stringAt(-2, "ANCHONDO")))  or  (self.stringAt(0, "CHISM", "CHELI")  and  not (self.stringStart("MICHEL", "MACHISMO", "RICHELIEU", "REVANCHISM")  or  self.stringExact("CHISM")))  or  (self.stringAt(0, "CHOR", "CHOL", "CHYM", "CHYL", "CHLO", "CHOS", "CHUS", "CHOE")  and  not self.stringStart("CHOLLO", "CHOLLA", "CHORIZ"))  or  (self.stringAt(0, "CHAO")  and  self.idx+3 != self.last_idx)  or  (self.stringAt(0, "CHIA")  and  not (self.stringStart("CHIAPAS", "APPALACHIA")))  or  self.stringAt(0, "CHIMERA", "CHIMAER", "CHIMERI")  or  self.stringStart("CHAME", "CHELO", "CHITO")  or  ((self.idx+4 == self.last_idx  or  self.idx+5 == self.last_idx)  and  self.stringAt(-1, "OCHETE")))  and  not (self.stringExact("CHORE", "CHOLO", "CHOLA")  or  self.stringAt(0, "CHORT", "CHOSE")  or  self.stringAt(-3, "CROCHET")  or  self.stringStart("CHEMISE", "CHARISE", "CHARISS", "CHAROLE")):

            if self.stringAt(2, "R", "L"):
                self.metaphAdd('K')
            else:
                self.metaphAddAlt('K', 'X')
            self.idx += 1
            return True

        return False

    def encodeGreekChNonInitial(self):

        if self.stringAt(-2, "LYCHN", "TACHO", "ORCHO", "ORCHI", "LICHO", "ORCHID", "NICHOL", "MECHAN", "LICHEN", "MACHIC", "PACHEL", "RACHIF", "RACHID", "RACHIS", "RACHIC", "MICHAL", "ORCHESTR")  or  self.stringAt(-3, "MELCH", "GLOCH", "TRACH", "TROCH", "BRACH", "SYNCH", "PSYCH", "STICH", "PULCH", "EPOCH")  or  (self.stringAt(-3, "TRICH")  and  not self.stringAt(-5, "OSTRICH"))  or  (self.stringAt(-2, "TYCH", "TOCH", "BUCH", "MOCH", "CICH", "DICH", "NUCH", "EICH", "LOCH", "DOCH", "ZECH", "WYCH")  and  not (self.stringAt(-4, "INDOCHINA")  or  self.stringAt(-2, "BUCHON")))  or  ((self.idx == 1  or  self.idx == 2)  and  self.stringAt(-1, "OCHER", "ECHIN", "ECHID"))  or  self.stringAt(-4, "BRONCH", "STOICH", "STRYCH", "TELECH", "PLANCH", "CATECH", "MANICH", "MALACH", "BIANCH", "DIDACH", "BRANCHIO", "BRANCHIF")  or  self.stringStart("ICHA", "ICHN")  or  (self.stringAt(-1, "ACHAB", "ACHAD", "ACHAN", "ACHAZ")  and  not self.stringAt(-2, "MACHADO", "LACHANC"))  or  self.stringAt(-1, "ACHISH", "ACHILL", "ACHAIA", "ACHENE", "ACHAIAN", "ACHATES", "ACHIRAL", "ACHERON", "ACHILLEA", "ACHIMAAS", "ACHILARY", "ACHELOUS", "ACHENIAL", "ACHERNAR", "ACHALASIA", "ACHILLEAN", "ACHIMENES", "ACHIMELECH", "ACHITOPHEL")  or  (self.idx == 2  and  (self.stringStart("INCHOA"))  or  self.stringStart("ISCH"))  or  (self.idx+1 == self.last_idx  and  self.stringAt(-1, "A", "O", "U", "E")  and  not (self.stringStart("DEBAUCH")  or  self.stringAt(-2, "MUCH", "SUCH", "KOCH")  or  self.stringAt(-5, "OODRICH", "ALDRICH"))):

            self.metaphAddAlt('K', 'X')
            self.idx += 1
            return True

        return False


    def encodeCcia(self):

        if self.stringAt(1, "CIA"):
            self.metaphAddAlt('X', 'S')
            self.idx += 1
            return True

        return False

    def encodeCc(self):

        if self.stringAt(0, "CC")  and  not (self.idx == 1  and  self.word[0] == 'M'):

            if self.stringAt(-3, "FLACCID"):
                self.metaphAdd('S')
                self.advanceCounter(2, 1)
                return True


            if self.stringAtEnd(2, "I")  or  self.stringAt(2, "IO")  or  self.stringAtEnd(2, "INO", "INI"):
                self.metaphAdd('X')
                self.advanceCounter(2, 1)
                return True


            if self.stringAt(2, "I", "E", "Y")  and  not (self.charAt(2, 'H')  or  self.stringAt(-2, "SOCCER")):
                self.metaphAddStr("KS", "KS")
                self.advanceCounter(2, 1)
                return True

            self.metaphAdd('K')
            self.idx += 1
            return True

        return False

    def encodeCkCgCq(self):
        if self.stringAt(0, "CK", "CG", "CQ"):


            if self.stringAtEnd(0, "CKI", "CKY")  and  len(self.word) > 6:
                self.metaphAddStr("K", "SK")
            else:
                self.metaphAdd('K')
            self.idx += 1

            if self.stringAt(1, "K", "G", "Q"):
                self.idx += 1

            return True

        return False



    def encodeCFrontVowel(self):
        if self.stringAt(0, "CI", "CE", "CY"):
            if self.encodeBritishSilentCE()  or  self.encodeCe()  or  self.encodeCi()  or  self.encodeLatinateSuffixes():

                self.advanceCounter(1, 0)
                return True

            self.metaphAdd('S')
            self.advanceCounter(1, 0)
            return True

        return False

    def encodeBritishSilentCE(self):

        if self.stringAtEnd(1, "ESTER")  or  self.stringAt(1, "ESTERSHIRE"):
            return True

        return False

    def encodeCe(self):

        if (self.stringAt(1, "EAN")  and  self.isVowelAt(-1))  or  (self.stringAtEnd(-1, "ACEA")  and  not self.stringStart("PANACEA"))  or  self.stringAt(1, "ELLI", "ERTO", "EORL")  or  self.stringAtEnd(-3, "CROCE")  or  self.stringAt(-3, "DOLCE")  or  self.stringAtEnd(1, "ELLO"):

            self.metaphAddAlt('X', 'S')
            return True

        return False

    def encodeCi(self):



        if (self.stringAtEnd(1, "INI")  and  not self.stringExact("MANCINI"))  or  self.stringAtEnd(-1, "ICI")  or  self.stringAt(-1, "RCIAL", "NCIAL", "RCIAN", "UCIUS")  or  self.stringAt(-3, "MARCIA")  or  self.stringAt(-2, "ANCIENT"):
            self.metaphAddAlt('X', 'S')
            return True


        if self.stringAt(-4, "COERCION"):
            self.metaphAdd('J')
            return True


        if (self.stringAt(0, "CIO", "CIE", "CIA")  and  self.isVowelAt(-1))  or  self.stringAt(1, "IAO"):

            if (self.stringAt(0, "CIAN", "CIAL", "CIAO", "CIES", "CIOL", "CION")  or  self.stringAt(-3, "GLACIER")  or  self.stringAt(0, "CIENT", "CIENC", "CIOUS", "CIATE", "CIATI", "CIATO", "CIABL", "CIARY")  or  self.stringAtEnd(0, "CIA", "CIO", "CIAS", "CIOS"))  and  not (self.stringAt(-4, "ASSOCIATION")  or  self.stringStart("OCIE")  or  self.stringAt(-2, "LUCIO", "SOCIO", "SOCIE", "MACIAS", "LUCIANO", "HACIENDA")  or  self.stringAt(-3, "GRACIE", "GRACIA", "MARCIANO")  or  self.stringAt(-4, "PALACIO", "POLICIES", "FELICIANO")  or  self.stringAt(-5, "MAURICIO")  or  self.stringAt(-6, "ANDALUCIA")  or  self.stringAt(-7, "ENCARNACION")):

                self.metaphAddAlt('X', 'S')
            else:
                self.metaphAddAlt('S', 'X')

            return True

        return False

    def encodeLatinateSuffixes(self):
        if self.stringAt(1, "EOUS", "IOUS"):
            self.metaphAddAlt('X', 'S')
            return True
        return False

    def encodeSilentC(self):
        if self.stringAt(1, "T", "S")  and  self.stringStart("INDICT", "TUCSON", "CONNECTICUT"):
            return True

        return False



    def encodeCz(self):
        if self.stringAt(1, "Z")  and  not self.stringAt(-1, "ECZEMA"):
            if self.stringAt(0, "CZAR"):
                self.metaphAdd('S')
            else:

                self.metaphAdd('X')
            self.idx += 1
            return True

        return False

    def encodeCs(self):




        if self.stringStart("KOVACS"):
            self.metaphAddStr("KS", "X")
            self.idx += 1
            return True

        if self.stringAtEnd(-1, "ACS")  and  not self.stringAt(-4, "ISAACS"):
            self.metaphAdd('X')
            self.idx += 1
            return True

        return False

    def encodeD(self):
        if self.encodeDg()  or  self.encodeDj()  or  self.encodeDtDd()  or  self.encodeDToJ()  or  self.encodeDous()  or  self.encodeSilentD():
            return

        if self.encode_exact:


            if self.stringAtEnd(-3, "SSED"):
                self.metaphAdd('T')
            else:
                self.metaphAdd('D')
        else:
            self.metaphAdd('T')

    def encodeDg(self):
        if self.stringAt(0, "DG"):



            if self.stringAt(2, "A", "O")  or  self.stringAt(1, "GUN", "GUT", "GEAR", "GLAS", "GRIP", "GREN", "GILL", "GRAF", "GUARD", "GUILT", "GRAVE", "GRASS", "GROUSE"):

                self.metaphAddExactApprox("DG", "TK")
            else:

                self.metaphAdd('J')

            self.idx += 1
            return True

        return False

    def encodeDj(self):

        if self.stringAt(0, "DJ"):
            self.metaphAdd('J')
            self.idx += 1
            return True
        return False

    def encodeDtDd(self):

        if self.stringAt(0, "DT", "DD"):
            if self.stringAt(0, "DTH"):
                self.metaphAddExactApprox("D0", "T0")
                self.idx += 2
            else:
                if self.encode_exact:

                    if self.stringAt(0, "DT"):
                        self.metaphAdd('T')
                    else:
                        self.metaphAdd('D')
                else:
                    self.metaphAdd('T')
                self.idx += 1

            return True
        return False

    def encodeDToJ(self):

        if (self.stringAt(0, "DUL")  and  self.isVowelAt(-1)  and  self.isVowelAt(3))  or  self.stringAtEnd(-1, "LDIER", "NDEUR", "EDURE", "RDURE")  or  self.stringAt(-3, "CORDIAL")  or  self.stringAt(-1, "ADUA", "IDUA", "IDUU", "NDULA", "NDULU", "EDUCA"):

            self.metaphAddExactApproxAlt("J", "D", "J", "T")
            self.advanceCounter(1, 0)
            return True
        return False

    def encodeDous(self):

        if self.stringAt(1, "UOUS"):
            self.metaphAddExactApproxAlt("J", "D", "J", "T")
            self.advanceCounter(3, 0)
            return True
        return False

    def encodeSilentD(self):

        return self.stringAt(-2, "WEDNESDAY")  or  self.stringAt(-3, "HANDKER", "HANDSOM", "WINDSOR")  or self.stringEnd("PERNOD", "ARTAUD", "RENAUD", "RIMBAUD", "MICHAUD", "BICHAUD")

    def encodeF(self):



        if self.stringAt(-1, "OFTEN"):
            self.metaphAddStr("F", "FT")
            self.idx += 1
            return


        if self.charNextIs('F'):
            self.idx += 1
        self.metaphAdd('F')

    def encodeG(self):
        if self.encodeSilentGAtBeginning()  or  self.encodeGg()  or  self.encodeGk()  or  self.encodeGh()  or  self.encodeSilentG()  or  self.encodeGn()  or  self.encodeGl()  or  self.encodeInitialGFrontVowel()  or  self.encodeNger()  or  self.encodeGer()  or  self.encodeGel()  or  self.encodeNonInitialGFrontVowel()  or  self.encodeGaToJ():
            return

        if not self.stringAt(-1, "C", "K", "G", "Q"):
            self.metaphAddExactApprox("G", "K")

    def encodeSilentGAtBeginning(self):
        return self.stringAtStart(0, "GN")

    def encodeGg(self):
        if self.charNextIs('G'):

            if self.stringAt(-1, "AGGIA", "OGGIA", "AGGIO", "EGGIO", "EGGIA", "IGGIO")  or  (self.stringAt(-1, "UGGIE")  and  not (self.idx+3 == self.last_idx  or  self.idx+4 == self.last_idx))  or  self.stringAtEnd(-1, "AGGI", "OGGI")  or  self.stringAt(-2, "SUGGES", "XAGGER", "REGGIE"):


                if self.stringAt(-2, "SUGGEST"):
                    self.metaphAddExactApprox("G", "K")
                self.metaphAdd('J')
                self.advanceCounter(2, 1)
            else:
                self.metaphAddExactApprox("G", "K")
                self.idx += 1

            return True

        return False

    def encodeGk(self):

        if self.charNextIs('K'):
            self.metaphAdd('K')
            self.idx += 1
            return True
        return False

    def encodeGh(self):
        if self.charNextIs('H'):
            if self.encodeGhAfterConsonant()  or  self.encodeInitialGh()  or  self.encodeGhToJ()  or  self.encodeGhToH()  or  self.encodeUght()  or  self.encodeGhHPartOfOtherWord()  or  self.encodeSilentGh()  or  self.encodeGhToF():
                return True

            self.metaphAddExactApprox("G", "K")
            self.idx += 1
            return True
        return False

    def encodeGhAfterConsonant(self):

        if self.idx > 0  and  not self.isVowelAt(-1)  and  not self.stringAtEnd(-3, "HALGH"):
            self.metaphAddExactApprox("G", "K")
            self.idx += 1
            return True
        return False

    def encodeInitialGh(self):
        if self.idx == 0:

            if self.charAt(2, 'I'):
                self.metaphAdd('J')
            else:
                self.metaphAddExactApprox("G", "K")
            self.idx += 1
            return True
        return False

    def encodeGhToJ(self):

        if self.stringAtEnd(-2, "ALGH"):
            self.metaphAddAlt('J', REPLACEMENT_CHAR)
            self.idx += 1
            return True
        return False

    def encodeGhToH(self):


        if (self.stringAt(-4, "DONO", "DONA")  and  self.isVowelAt(2))  or  self.stringAt(-5, "CALLAGHAN"):
            self.metaphAdd('H')
            self.idx += 1
            return True
        return False

    def encodeUght(self):

        if self.stringAt(-1, "UGHT"):
            if (self.stringAt(-3, "LAUGH")  and  not (self.stringAt(-4, "SLAUGHT")  or  self.stringAt(-3, "LAUGHTO")))  or  self.stringAt(-4, "DRAUGH"):

                self.metaphAddStr("FT", "FT")
            else:
                self.metaphAdd('T')

            self.idx += 2
            return True
        return False

    def encodeGhHPartOfOtherWord(self):

        if self.stringAt(1, "HOUS", "HEAD", "HOLE", "HORN", "HARN"):
            self.metaphAddExactApprox("G", "K")
            self.idx += 1
            return True
        return False

    def encodeSilentGh(self):

        if ((self.stringAt(-2, "B", "H", "D", "G", "L")  or  (self.stringAt(-3, "B", "H", "D", "K", "W", "N", "P", "V")  and  not self.stringStart("ENOUGH"))  or  self.stringAt(-4, "B", "H", "PL", "SL")  or  (self.idx > 0  and  (self.charAt(-1, 'I')  or  self.stringStart("PUGH")  or  self.stringAtEnd(-1, "AGH")  or  self.stringAt(-4, "GERAGH", "DRAUGH")  or  (self.stringAt(-3, "GAUGH", "GEOGH", "MAUGH")  and  not self.stringStart("MCGAUGHEY"))  or  (self.stringAt(-2, "OUGH")  and  self.idx > 3  and  not self.stringAt(-4, "CCOUGH", "ENOUGH", "TROUGH", "CLOUGH")))))  and  (self.stringAt(-3, "VAUGH", "FEIGH", "LEIGH")  or  self.stringAt(-2, "HIGH", "TIGH")  or  self.idx+1 == self.last_idx  or  (self.stringAtEnd(2, "IE", "EY", "ES", "ER", "ED", "TY")  and  not self.stringAt(-5, "GALLAGHER"))  or  self.stringAtEnd(2, "Y", "ING", "OUT", "ERTY")  or  (not self.isVowelAt(2)  or  self.stringAt(-3, "GAUGH", "GEOGH", "MAUGH")  or  self.stringAt(-4, "BROUGHAM"))))  and  not (self.stringStart("BALOGH", "SABAGH")  or  self.stringAt(-2, "BAGHDAD")  or  self.stringAt(-3, "WHIGH")  or  self.stringAt(-5, "SABBAGH", "AKHLAGH")):

            self.idx += 1
            return True
        return False

    def encodeGhSpecialCases(self):
        handled = False


        if self.stringAt(-6, "HICCOUGH"):
            self.metaphAdd('P')
            handled = True
        elif self.stringStart("LOUGH"):

            self.metaphAdd('K')
            handled = True
        elif self.stringStart("BALOGH"):

            self.metaphAddExactApproxAlt("G", "", "K", "")
            handled = True
        elif self.stringAt(-3, "LAUGHLIN", "COUGHLAN", "LOUGHLIN"):

            self.metaphAddAlt('K', 'F')
            handled = True
        elif self.stringAt(-3, "GOUGH")  or  self.stringAt(-7, "COLCLOUGH"):
            self.metaphAddAlt(REPLACEMENT_CHAR, 'F')
            handled = True

        if handled:
            self.idx += 1

        return handled

    def encodeGhToF(self):


        if self.encodeGhSpecialCases():
            return True


        if self.idx > 2  and  self.charAt(-1, 'U')  and  self.isVowelAt(-2)  and  self.stringAt(-3, "C", "G", "L", "R", "T", "N", "S")  and  not self.stringAt(-4, "BREUGHEL", "FLAUGHER"):

            self.metaphAdd('F')
            self.idx += 1
            return True
        return False

    def encodeSilentG(self):

        if self.stringAtEnd(-1, "EGM", "IGM", "AGM")  or  self.stringAtEnd(0, "GT")  or  self.stringExact("HUGES"):
            return True


        if self.stringStart("NG")  and  self.idx != self.last_idx:
            return True
        return False

    def encodeGn(self):
        if self.charNextIs('N'):


            if (self.idx > 1  and  ((self.stringAt(-1, "I", "U", "E")  or  self.stringAt(-3, "CHAGNON", "LORGNETTE")  or  self.stringAt(-2, "COGNAC", "LAGNIAPPE")  or  self.stringAt(-4, "BOLOGN")  or  self.stringAt(-5, "COMPAGNIE"))  and  not (self.stringAt(2, "ATE", "ITY", "ATOR", "ATION")  or  (self.stringAt(2, "AN", "AC", "IA", "UM")  and  not (self.stringAt(-3, "POIGNANT")  or  self.stringAt(-2, "COGNAC")))  or  self.stringStart("SPIGNER", "STEGNER")  or  self.stringExact("SIGNE")  or  self.stringAt(-2, "LIGNI", "LIGNO", "REGNA", "DIGNI", "WEGNE", "TIGNE", "RIGNE", "REGNE", "TIGNO", "SIGNAL", "SIGNIF", "SIGNAT")  or  self.stringAt(-1, "IGNIT"))  and  not self.stringAt(-2, "SIGNET", "LIGNEO")))  or  (self.stringAtEnd(0, "GNE", "GNA")  and  not self.stringAt(-2, "SIGNA", "MAGNA", "SIGNE")):
                self.metaphAddExactApproxAlt("N", "GN", "N", "KN")
            else:
                self.metaphAddExactApprox("GN", "KN")
            self.idx += 1
            return True

        return False

    def encodeGl(self):


        if self.stringAt(1, "LIA", "LIO", "LIE")  and  self.isVowelAt(-1):
            self.metaphAddExactApproxAlt("L", "GL", "L", "KL")
            self.idx += 1
            return True
        return False

    def encodeInitialGFrontVowel(self):
        if self.idx == 0  and  self.frontVowel(1):

            if self.stringExact("GILA"):
                self.metaphAdd('H')
            elif self.initialGSoft():
                self.metaphAddExactApproxAlt("J", "G", "J", "K")
            elif self.charNextIs('E')  or  self.charNextIs('I'):
                self.metaphAddExactApproxAlt("G", "J", "K", "J")
            else:
                self.metaphAddExactApprox("G", "K")

            self.advanceCounter(1, 0)
            return True

        return False

    def initialGSoft(self):
        if (self.stringAt(1, "EL", "EM", "EN", "EO", "ER", "ES", "IA", "IN", "IO", "IP", "IU", "YM", "YN", "YP", "YR", "EE", "IRA", "IRO")  and  not self.stringAt(1, "ELD", "ELT", "ERT", "INZ", "ERH", "ITE", "ERD", "ERL", "ERN", "INT", "EES", "EEK", "ELB", "EER", "ERSH", "ERST", "INSB", "INGR", "EROW", "ERKE", "EREN", "ELLER", "ERDIE", "ERBER", "ESUND", "ESNER", "INGKO", "INKGO", "IPPER", "ESELL", "IPSON", "EEZER", "ERSON", "ELMAN", "ESTALT", "ESTAPO", "INGHAM", "ERRITY", "ERRISH", "ESSNER", "ENGLER", "YNAECOL", "YNECOLO", "ENTHNER", "ERAGHTY", "INGERICH", "EOGHEGAN"))  or  (self.isVowelAt(1)  and  (self.stringAt(1, "EE ", "EEW")  or  (self.stringAt(1, "IGI", "IRA", "IBE", "AOL", "IDE", "IGL")  and  not self.stringAt(1, "IDEON"))  or  self.stringAt(1, "ILES", "INGI", "ISEL", "IBBER", "IBBET", "IBLET", "IBRAN", "IGOLO", "IRARD", "IGANT", "IRAFFE", "EEWHIZ", "ILLETTE", "IBRALTA")  or  (self.stringAt(1, "INGER")  and  not self.stringAt(1, "INGERICH")))):

            return True

        return False

    def frontVowel(self, offset):
        return self.charAt(offset, 'E')  or  self.charAt(offset, 'I')  or  self.charAt(offset, 'Y')

    def encodeNger(self):
        if self.stringAt(-1, "NGER"):






            if not (rootOrInflections(self.word, "ANGER")  or  rootOrInflections(self.word, "LINGER")  or  rootOrInflections(self.word, "MALINGER")  or  rootOrInflections(self.word, "FINGER")  or  (self.stringAt(-3, "HUNG", "FING", "BUNG", "WING", "RING", "DING", "ZENG", "ZING", "JUNG", "LONG", "PING", "CONG", "MONG", "BANG", "GANG", "HANG", "LANG", "SANG", "SING", "WANG", "ZANG")  and  not (self.stringAt(-6, "BOULANG", "SLESING", "KISSING", "DERRING", "BARRING", "PHALANGER")  or  self.stringAt(-8, "SCHLESING")  or  self.stringAt(-5, "SALING", "BELANG")  or  self.stringAt(-4, "CHANG")))  or  self.stringAt(-4, "STING", "YOUNG")  or  self.stringAt(-5, "STRONG")  or  self.stringStart("UNG", "ENG", "ING", "SENGER")  or  self.stringAt(0, "GERICH")  or  self.stringAt(-2, "ANGERLY", "ANGERBO", "INGERSO")  or  self.stringAt(-3, "WENGER", "MUNGER", "SONGER", "KINGER", "LINGERF")  or  self.stringAt(-4, "FLINGER", "SLINGER", "STANGER", "STENGER", "KLINGER", "CLINGER")  or  self.stringAt(-5, "SPRINGER", "SPRENGER")):

                self.metaphAddExactApproxAlt("J", "G", "J", "K")
            else:
                self.metaphAddExactApproxAlt("G", "J", "K", "J")

            self.advanceCounter(1, 0)
            return True
        return False

    def encodeGer(self):
        if self.idx > 0  and  self.stringAt(1, "ER"):



            if ((self.idx == 2  and  self.isVowelAt(-1)  and  not self.isVowelAt(-2)  and  not self.stringAt(-2, "PAGER", "WAGER", "NIGER", "ROGER", "LEGER", "CAGER")  or  self.stringAt(-2, "AUGER", "EAGER", "INGER", "YAGER"))  or  self.stringAt(-3, "SEEGER", "JAEGER", "GEIGER", "KRUGER", "SAUGER", "BURGER", "MEAGER", "MARGER", "RIEGER", "YAEGER", "STEGER", "PRAGER", "SWIGER", "YERGER", "TORGER", "FERGER", "HILGER", "ZEIGER", "YARGER", "COWGER", "CREGER", "KROGER", "KREGER", "GRAGER", "STIGER", "BERGER")  or  self.stringAtEnd(-3, "BERGER")  or  self.stringAt(-4, "KREIGER", "KRUEGER", "METZGER", "KRIEGER", "KROEGER", "STEIGER", "DRAEGER", "BUERGER", "BOERGER", "FIBIGER")  or  (self.stringAt(-3, "BARGER")  and  self.idx > 4)  or  (self.stringAt(0, "GERBER")  and  self.idx > 0)  or  self.stringAt(-5, "SCHWAGER", "LYBARGER", "SPRENGER", "GALLAGER", "WILLIGER")  or  self.stringStart("HARGER")  or  self.stringExact("AGER", "EGER")  or  self.stringAt(-1, "YGERNE")  or  self.stringAt(-6, "SCHWEIGER"))  and  not (self.stringAt(-5, "BELLIGEREN")  or  self.stringStart("MARGERY")  or  self.stringAt(-3, "BERGERAC")):

                if self.isSlavoGermanic():
                    self.metaphAddExactApprox("G", "K")
                else:
                    self.metaphAddExactApproxAlt("G", "J", "K", "J")
            else:
                self.metaphAddExactApproxAlt("J", "G", "J", "K")

            self.advanceCounter(1, 0)
            return True
        return False

    def encodeGel(self):

        if self.stringAt(1, "EL")  and  self.idx > 0:


            if (len(self.word) == 5  and  self.isVowelAt(-1)  and  not self.isVowelAt(-2)  and  not self.stringAt(-2, "NIGEL", "RIGEL"))  or  self.stringAt(-2, "ENGEL", "HEGEL", "NAGEL", "VOGEL")  or  self.stringAt(-3, "MANGEL", "WEIGEL", "FLUGEL", "RANGEL", "HAUGEN", "RIEGEL", "VOEGEL")  or  self.stringAt(-4, "SPEIGEL", "STEIGEL", "WRANGEL", "SPIEGEL", "DANEGELD"):

                if self.isSlavoGermanic():
                    self.metaphAddExactApprox("G", "K")
                else:
                    self.metaphAddExactApproxAlt("G", "J", "K", "J")
            else:
                self.metaphAddExactApproxAlt("J", "G", "J", "K")

            self.advanceCounter(1, 0)
            return True

        return False



    def encodeNonInitialGFrontVowel(self):

        if self.stringAt(1, "E", "I", "Y"):


            if self.stringAtEnd(0, "GE"):

                if self.stringStart("INGE", "LAGE", "HAGE", "LANGE", "SYNGE", "BENGE", "RUNGE", "HELGE", "BYRGE", "BIRGE", "BERGE", "HAUGE", "RENEGE", "STONGE", "STANGE", "PRANGE", "KRESGE"):
                    if self.isSlavoGermanic():
                        self.metaphAddExactApprox("G", "K")
                    else:
                        self.metaphAddExactApproxAlt("G", "J", "K", "J")
                else:
                    self.metaphAdd('J')
            else:
                if self.internalHardG():


                    if not self.stringAtStart(-2, "MC")  or  self.stringAtStart(-3, "MAC"):
                        if self.isSlavoGermanic():
                            self.metaphAddExactApprox("G", "K")
                        else:
                            self.metaphAddExactApproxAlt("G", "J", "K", "J")
                else:
                    self.metaphAddExactApproxAlt("J", "G", "J", "K")

            self.advanceCounter(1, 0)
            return True

        return False

    def internalHardG(self):

        if not (self.idx+1 == self.last_idx  and  self.charNextIs('E'))  and  (self.internalHardNg()  or  self.internalHardGenGinGetGit()  or  self.internalHardGOpenSyllable()  or  self.internalHardGOther()):
            return True

        return False

    def internalHardNg(self):
        if (self.stringAt(-3, "DANG", "FANG", "SING")  and  not self.stringAt(-5, "DISINGEN"))  or  self.stringStart("INGEB", "ENGEB")  or  (self.stringAt(-3, "RING", "WING", "HANG", "LONG")  and  not (self.stringAt(-4, "CRING", "FRING", "ORANG", "TWING", "CHANG", "PHANG")  or  self.stringAt(-5, "SYRING")  or  self.stringAt(-3, "RINGENC", "RINGENT", "LONGITU", "LONGEVI")  or  self.stringAtEnd(0, "GELO", "GINO")))  or  (self.stringAt(-1, "NGY")  and  not (self.stringAt(-3, "RANGY", "MANGY", "MINGY")  or  self.stringAt(-4, "SPONGY", "STINGY"))):
            return True

        return False

    def internalHardGenGinGetGit(self):
        if (self.stringAt(-3, "FORGET", "TARGET", "MARGIT", "MARGET", "TURGEN", "BERGEN", "MORGEN", "JORGEN", "HAUGEN", "JERGEN", "JURGEN", "LINGEN", "BORGEN", "LANGEN", "KLAGEN", "STIGER", "BERGER")  and  not self.stringAt(0, "GENETIC", "GENESIS")  and  not self.stringAt(-4, "PLANGENT"))  or  self.stringAtEnd(-3, "BERGIN", "FEAGIN", "DURGIN")  or  (self.stringAt(-2, "ENGEN")  and  not self.stringAt(3, "DER", "ETI", "ESI"))  or  self.stringAt(-4, "JUERGEN")  or  self.stringStart("NAGIN", "MAGIN", "HAGIN")  or  self.stringExact("ENGIN", "DEGEN", "LAGEN", "MAGEN", "NAGIN")  or  (self.stringAt(-2, "BEGET", "BEGIN", "HAGEN", "FAGIN", "BOGEN", "WIGIN", "NTGEN", "EIGEN", "WEGEN", "WAGEN")  and  not self.stringAt(-5, "OSPHAGEN")):
            return True
        return False

    def internalHardGOpenSyllable(self):
        return self.stringAt(1, "EYE")  or  self.stringAt(-2, "FOGY", "POGY", "YOGI", "MAGEE", "MCGEE", "HAGIO")  or  self.stringAt(-1, "RGEY", "OGEY")  or  self.stringAt(-3, "HOAGY", "STOGY", "PORGY")  or  self.stringAt(-5, "CARNEGIE")  or  self.stringAtEnd(-1, "OGEY", "OGIE")

    def internalHardGOther(self):
        if (self.stringAt(0, "GETH", "GEAR", "GEIS", "GIRL", "GIVI", "GIVE", "GIFT", "GIRD", "GIRT", "GILV", "GILD", "GELD")  and  not self.stringAt(-3, "GINGIV"))  or  (self.stringAt(1, "ISH")  and  self.idx > 0  and  not self.stringStart("LARG"))  or  (self.stringAt(-2, "MAGED", "MEGID")  and  self.idx+2 != self.last_idx)  or  self.stringAt(0, "GEZ")  or  self.stringStart("WEGE", "HAGE", "VOEGE", "BERGE", "HELGE", "INGEBORG", "CORREGIDOR")  or  (self.stringAtEnd(-2, "ONGEST", "UNGEST")  and  not self.stringAt(-3, "CONGEST"))  or  self.stringExact("ENGE", "BOGY")  or  self.stringAt(0, "GIBBON")  or  (self.stringAt(0, "GILL")  and  (self.idx+3 == self.last_idx  or  self.idx+4 == self.last_idx)  and  not self.stringStart("STURGILL")):

            return True

        return False

    def encodeGaToJ(self):


        if (self.stringAt(-3, "MARGARY", "MARGARI")  and  not self.stringAt(-3, "MARGARIT"))  or  self.stringStart("GAOL")  or  self.stringAt(-2, "ALGAE"):

            self.metaphAddExactApproxAlt("J", "G", "J", "K")
            self.advanceCounter(1, 0)
            return True
        return False

    def encodeH(self):
        if self.encodeInitialSilentH()  or  self.encodeInitialHs()  or  self.encodeInitialHuHw()  or  self.encodeNonInitialSilentH():
            return


        if not self.encodeHPronounced():
            pass


    def encodeInitialSilentH(self):

        if self.stringAt(1, "OUR", "ERB", "EIR", "ONOR", "ONOUR", "ONEST"):



            if self.stringAtStart(0, "HERB"):
                if self.encode_vowels:
                    self.metaphAddStr("HA", "A")
                else:
                    self.metaphAddAlt('H', 'A')
            elif self.idx == 0  or  self.encode_vowels:
                self.metaphAdd('A')


            self.idx = self.skipVowels(self.idx + 1)
            return True

        return False

    def encodeInitialHs(self):


        if self.stringAtStart(0, "HS"):
            self.metaphAdd('X')
            self.idx += 1
            return True
        return False

    def encodeInitialHuHw(self):

        if self.stringStart("HUA", "HUE", "HWA")  and  not self.stringAt(0, "HUEY"):
            self.metaphAdd('A')

            if not self.encode_vowels:
                self.idx += 2
            else:
                self.idx += 1


                while self.isVowelAt(0) or self.charAt(0, 'W'):
                    self.idx += 1
                self.idx -= 1
            return True

        return False

    def encodeNonInitialSilentH(self):
        if self.stringAt(-2, "NIHIL", "VEHEM", "LOHEN", "NEHEM", "MAHON", "MAHAN", "COHEN", "GAHAN")  or  self.stringAt(-3, "TOUHY", "GRAHAM", "PROHIB", "FRAHER", "TOOHEY", "TOUHEY")  or  self.stringStart("CHIHUAHUA"):
            if self.encode_vowels:
                self.idx += 1
            else:
                self.idx = self.skipVowels(self.idx + 1)
            return True
        return False

    def encodeHPronounced(self):
        if ((self.idx == 0  or  self.isVowelAt(-1)  or  (self.idx > 0  and  self.charAt(-1, 'W')))  and  self.isVowelAt(1))  or  (self.charNextIs('H')  and  self.isVowelAt(2)):

            self.metaphAdd('H')
            self.advanceCounter(1, 0)
            return True

        return False

    def encodeJ(self):
        if self.encodeSpanishJ()  or  self.encodeSpanishOjUj():
            return


        if self.idx == 0:
            if self.encodeGermanJ():
                return
            elif self.encodeJToJ():
                return
        else:
            if self.encodeSpanishJ2():
                return
            elif not self.encodeJAsVowel():
                self.metaphAdd('J')



            if self.charNextIs('J'):
                self.idx += 1

    def encodeSpanishJ(self):

        if (self.stringAt(1, "UAN", "ACI", "ALI", "EFE", "ICA", "IME", "OAQ", "UAR")  and  not self.stringAt(0, "JIMERSON", "JIMERSEN"))  or  self.stringAtEnd(1, "OSE")  or  self.stringAt(1, "EREZ", "UNTA", "AIME", "AVIE", "AVIA", "IMINEZ", "ARAMIL")  or  self.stringAtEnd(-2, "MEJIA")  or  self.stringAt(-2, "TEJED", "TEJAD", "LUJAN", "FAJAR", "BEJAR", "BOJOR", "CAJIG", "DEJAS", "DUJAR", "DUJAN", "MIJAR", "MEJOR", "NAJAR", "NOJOS", "RAJED", "RIJAL", "REJON", "TEJAN", "UIJAN")  or  self.stringAt(-3, "ALEJANDR", "GUAJARDO", "TRUJILLO")  or  (self.stringAt(-2, "RAJAS")  and  self.idx > 2)  or  (self.stringAt(-2, "MEJIA")  and  not self.stringAt(-2, "MEJIAN"))  or  self.stringAt(-1, "OJEDA")  or  self.stringAt(-3, "LEIJA", "MINJA", "VIAJES", "GRAJAL")  or  self.stringAt(0, "JAUREGUI")  or  self.stringAt(-4, "HINOJOSA")  or  self.stringStart("SAN ")  or  ((self.idx+1 == self.last_idx)  and  self.charAt(1, 'O')  and  not self.stringStart("TOJO", "BANJO", "MARYJO")):






            if not (self.stringAt(0, "JUAN")  or  self.stringAt(0, "JOAQ")):
                self.metaphAdd('H')
            elif self.idx == 0:
                self.metaphAdd('A')
            self.advanceCounter(1, 0)
            return True


        if self.stringAt(1, "ORGE", "ULIO", "ESUS")  and  not self.stringStart("JORGEN"):

            if self.stringAtEnd(1, "ORGE"):
                if self.encode_vowels:
                    self.metaphAddStr("JARJ", "HARHA")
                else:
                    self.metaphAddStr("JRJ", "HRH")
                self.advanceCounter(4, 4)
                return True
            self.metaphAddAlt('J', 'H')
            self.advanceCounter(1, 0)
            return True

        return False

    def encodeGermanJ(self):
        if self.stringAt(1, "AH", "UGO")  or  self.stringExact("JOHANN")  or  (self.stringAt(1, "UNG")  and  not self.charAt(4, 'L')):

            self.metaphAdd('A')
            self.advanceCounter(1, 0)
            return True

        return False

    def encodeSpanishOjUj(self):
        if self.stringAt(1, "OJOBA", "UJUY"):
            if self.encode_vowels:
                self.metaphAddStr("HAH", "HAH")
            else:
                self.metaphAddStr("HH", "HH")

            self.advanceCounter(3, 2)
            return True

        return False

    def encodeJToJ(self):
        if self.isVowelAt(1):
            if self.idx == 0  and  self.namesBeginningWithJThatGetAltY():


                if self.encode_vowels:
                    self.metaphAddStr("JA", "A")
                else:
                    self.metaphAddAlt('J', 'A')
            else:
                if self.encode_vowels:
                    self.metaphAddStr("JA", "JA")
                else:
                    self.metaphAdd('J')
            self.idx = self.skipVowels(self.idx + 1)
            return False

        self.metaphAdd('J')
        return True

    def encodeSpanishJ2(self):

        if self.stringAtStart(-2, "BOJA", "BAJA", "BEJA", "BOJO", "MOJA", "MOJI", "MEJI")  or  self.stringAtStart(-3, "FRIJO", "BRUJO", "BRUJA", "GRAJE", "GRIJA", "LEIJA", "QUIJA")  or  self.stringAtEnd(-1, "AJOS", "EJOS", "OJAS", "OJOS", "UJON", "AJOZ", "AJAL", "UJAR", "EJON", "EJAN", "AJARA")  or  (self.stringAtEnd(-1, "OJA", "EJA")  and  not self.stringStart("DEJA")):

            self.metaphAdd('H')
            self.advanceCounter(1, 0)
            return True

        return False

    def encodeJAsVowel(self):
        if self.stringAt(0, "JEWSK"):
            self.metaphAddAlt('J', REPLACEMENT_CHAR)
            return True



        if (self.stringAt(1, "L", "T", "K", "S", "N", "M")  and  not self.stringAt(2, "A"))  or  self.stringStart("FJ", "WOJ", "LJUB", "BJOR", "HAJEK", "HALLELUJA", "LJUBLJANA")  or  self.stringAt(0, "JAVIK", "JEVIC")  or  self.stringExact("SONJA", "TANJA", "TONJA"):

            return True

        return False

    def namesBeginningWithJThatGetAltY(self):
        return self.stringStart("JAN", "JON", "JAN", "JIN", "JEN", "JUHL", "JULY", "JOEL", "JOHN", "JOSH", "JUDE", "JUNE", "JONI", "JULI", "JENA", "JUNG", "JINA", "JANA", "JENI", "JOEL", "JANN", "JONA", "JENE", "JULE", "JANI", "JONG", "JOHN", "JEAN", "JUNG", "JONE", "JARA", "JUST", "JOST", "JAHN", "JACO", "JANG", "JUDE", "JONE", "JOANN", "JANEY", "JANAE", "JOANA", "JUTTA", "JULEE", "JANAY", "JANEE", "JETTA", "JOHNA", "JOANE", "JAYNA", "JANES", "JONAS", "JONIE", "JUSTA", "JUNIE", "JUNKO", "JENAE", "JULIO", "JINNY", "JOHNS", "JACOB", "JETER", "JAFFE", "JESKE", "JANKE", "JAGER", "JANIK", "JANDA", "JOSHI", "JULES", "JANTZ", "JEANS", "JUDAH", "JANUS", "JENNY", "JENEE", "JONAH", "JONAS", "JACOB", "JOSUE", "JOSEF", "JULES", "JULIE", "JULIA", "JANIE", "JANIS", "JENNA", "JANNA", "JEANA", "JENNI", "JEANE", "JONNA", "JAKOB", "JORDAN", "JORDON", "JOSEPH", "JOSHUA", "JOSIAH", "JOSPEH", "JUDSON", "JULIAN", "JULIUS", "JUNIOR", "JUDITH", "JOESPH", "JOHNIE", "JOANNE", "JEANNE", "JOANNA", "JOSEFA", "JULIET", "JANNIE", "JANELL", "JASMIN", "JANINE", "JOHNNY", "JEANIE", "JEANNA", "JOHNNA", "JOELLE", "JOVITA", "JOSEPH", "JONNIE", "JANEEN", "JANINA", "JOANIE", "JAZMIN", "JOHNIE", "JANENE", "JOHNNY", "JONELL", "JENELL", "JANETT", "JANETH", "JENINE", "JOELLA", "JOEANN", "JULIAN", "JOHANA", "JENICE", "JANNET", "JANISE", "JULENE", "JOSHUA", "JANEAN", "JAIMEE", "JOETTE", "JANYCE", "JENEVA", "JORDAN", "JACOBS", "JENSEN", "JOSEPH", "JANSEN", "JORDON", "JULIAN", "JAEGER", "JACOBY", "JENSON", "JARMAN", "JOSLIN", "JESSEN", "JAHNKE", "JACOBO", "JULIEN", "JOSHUA", "JEPSON", "JULIUS", "JANSON", "JACOBI", "JUDSON", "JARBOE", "JOHSON", "JANZEN", "JETTON", "JUNKER", "JONSON", "JAROSZ", "JENNER", "JAGGER", "JASMIN", "JEPSEN", "JORDEN", "JANNEY", "JUHASZ", "JERGEN", "JOHNSON", "JOHNNIE", "JASMINE", "JEANNIE", "JOHANNA", "JANELLE", "JANETTE", "JULIANA", "JUSTINA", "JOSETTE", "JOELLEN", "JENELLE", "JULIETA", "JULIANN", "JULISSA", "JENETTE", "JANETTA", "JOSELYN", "JONELLE", "JESENIA", "JANESSA", "JAZMINE", "JEANENE", "JOANNIE", "JADWIGA", "JOLANDA", "JULIANE", "JANUARY", "JEANICE", "JANELLA", "JEANETT", "JENNINE", "JOHANNE", "JOHNSIE", "JANIECE", "JOHNSON", "JENNELL", "JAMISON", "JANSSEN", "JOHNSEN", "JARDINE", "JAGGERS", "JURGENS", "JOURDAN", "JULIANO", "JOSEPHS", "JHONSON", "JOZWIAK", "JANICKI", "JELINEK", "JANSSON", "JOACHIM", "JANELLE", "JACOBUS", "JENNING", "JANTZEN", "JOHNNIE", "JOSEFINA", "JEANNINE", "JULIANNE", "JULIANNA", "JONATHAN", "JONATHON", "JEANETTE", "JANNETTE", "JEANETTA", "JOHNETTA", "JENNEFER", "JULIENNE", "JOSPHINE", "JEANELLE", "JOHNETTE", "JULIEANN", "JOSEFINE", "JULIETTA", "JOHNSTON", "JACOBSON", "JACOBSEN", "JOHANSEN", "JOHANSON", "JAWORSKI", "JENNETTE", "JELLISON", "JOHANNES", "JASINSKI", "JUERGENS", "JARNAGIN", "JEREMIAH", "JEPPESEN", "JARNIGAN", "JANOUSEK", "JOHNATHAN", "JOHNATHON", "JORGENSEN", "JEANMARIE", "JOSEPHINA", "JEANNETTE", "JOSEPHINE", "JEANNETTA", "JORGENSON", "JANKOWSKI", "JOHNSTONE", "JABLONSKI", "JOSEPHSON", "JOHANNSEN", "JURGENSEN", "JIMMERSON", "JOHANSSON", "JAKUBOWSKI")

    def encodeK(self):
        if not self.encodeSilentK():
            self.metaphAdd('K')


            if self.charAt(1, 'K')  or  self.charAt(1, 'Q'):
                self.idx += 1

    def encodeSilentK(self):
        if self.idx == 0  and  self.stringStart("KN"):
            if not self.stringAt(2, "ISH", "ESSET", "IEVEL"):
                return True


        if (self.stringAt(1, "NOW", "NIT", "NOT", "NOB")  and  not self.stringStart("BANKNOTE"))  or  self.stringAt(1, "NOCK", "NUCK", "NIFE", "NACK", "NIGHT"):


            if self.idx > 0  and  self.charAt(-1, 'N'):
                self.idx += 1

            return True

        return False

    def encodeL(self):


        saveIdx = self.idx

        self.interpolateVowelWhenConsLAtEnd()

        if self.encodeLelyToL()  or  self.encodeColonel()  or  self.encodeFrenchAult()  or  self.encodeFrenchEuil()  or  self.encodeFrenchOulx()  or  self.encodeSilentLInLm()  or  self.encodeSilentLInLkLv()  or  self.encodeSilentLInOuld():
            return

        if self.encodeLlAsVowelCases():
            return

        self.encodeLeCases(saveIdx)



    def interpolateVowelWhenConsLAtEnd(self):

        if self.encode_vowels  and  self.stringAtEnd(-1, "DL", "GL", "TL"):
            self.metaphAdd('A')

    def encodeLelyToL(self):

        if self.stringAtEnd(-1, "ILELY"):
            self.metaphAdd('L')
            self.idx += 2
            return True
        return False

    def encodeColonel(self):
        if self.stringAt(-2, "COLONEL"):
            self.metaphAdd('R')
            self.idx += 1
            return True
        return False

    def encodeFrenchAult(self):

        if self.idx > 3  and  (self.stringAt(-3, "RAULT", "NAULT", "BAULT", "SAULT", "GAULT", "CAULT")  or  self.stringAt(-4, "REAULT", "RIAULT", "NEAULT", "BEAULT"))  and  not (rootOrInflections(self.word, "ASSAULT")  or  self.stringAt(-8, "SOMERSAULT")  or  self.stringAt(-9, "SUMMERSAULT")):

            self.idx += 1
            return True

        return False

    def encodeFrenchEuil(self):

        if self.stringAtEnd(-3, "EUIL"):
            return True
        return False

    def encodeFrenchOulx(self):

        if self.stringAtEnd(-2, "OULX"):
            self.idx += 1
            return True
        return False

    def encodeSilentLInLm(self):
        if self.stringAt(0, "LM", "LN"):

            if (self.stringAt(-2, "COLN", "CALM", "BALM", "MALM", "PALM")  or  self.stringAtEnd(-1, "OLM")  or  self.stringAt(-3, "PSALM", "QUALM")  or  self.stringAt(-2, "SALMON", "HOLMES")  or  self.stringAt(-1, "ALMOND")  or  self.stringAtStart(-1, "ALMS"))  and  (not self.stringAt(2, "A")  and  not self.stringAt(-2, "BALMO", "PALMER", "PALMOR", "BALMER")  and  not self.stringAt(-3, "THALM")):
                pass

            else:
                self.metaphAdd('L')

            return True

        return False

    def encodeSilentLInLkLv(self):
        if (self.stringAt(-2, "WALK", "YOLK", "FOLK", "HALF", "TALK", "CALF", "BALK", "CALK")  or  (self.stringAt(-2, "POLK", "HALV", "SALVE", "CALVE", "SOLDER")  and  not self.stringAt(-2, "POLKA", "PALKO", "HALVA", "HALVO", "SALVER", "CALVER"))  or  (self.stringAt(-3, "CAULK", "CHALK", "BAULK", "FAULK")  and  not self.stringAt(-4, "SCHALK")))  and  not self.stringAt(-5, "GONSALVES", "GONCALVES")  and  not self.stringAt(-2, "BALKAN", "TALKAL")  and  not self.stringAt(-3, "PAULK", "CHALF"):

            return True

        return False

    def encodeSilentLInOuld(self):

        if self.stringAt(-3, "WOULD", "COULD")  or  (self.stringAt(-4, "SHOULD")  and  not self.stringAt(-4, "SHOULDER")):
            self.metaphAddExactApprox("D", "T")
            self.idx += 1
            return True
        return False



    def encodeLlAsVowelSpecialCases(self):
        if self.stringAt(-5, "TORTILLA")  or  self.stringAt(-8, "RATATOUILLE")  or  (self.stringStart("GUILL", "VEILL", "GAILL")  and  not (self.stringAt(-3, "GUILLOT", "GUILLOR", "GUILLEN")  or  self.stringExact("GUILL")))  or  self.stringStart("ROBILL", "BROUILL", "GREMILL")  or  (self.stringAtEnd(-2, "EILLE")  and  not self.stringAt(-5, "REVEILLE")):

            self.idx += 1
            return True

        return False

    def encodeLlAsVowel(self):



        if self.stringAtEnd(-1, "ILLO", "ILLA", "ALLE")  or  (self.stringEnd("A", "O", "AS", "OS")  and  self.stringAt(-1, "AL", "IL")  and  not self.stringAt(-1, "ALLA"))  or  self.stringStart("LLA", "VILLE", "VILLA", "GALLARDO", "VALLADAR", "MAGALLAN", "CAVALLAR", "BALLASTE"):

            self.metaphAddAlt('L', REPLACEMENT_CHAR)
            self.idx += 1
            return True
        return False

    def encodeLlAsVowelCases(self):
        if self.charNextIs('L'):
            if self.encodeLlAsVowelSpecialCases():
                return True
            elif self.encodeLlAsVowel():
                return True
            self.idx += 1

        return False

    def encodeVowelLeTransposition(self, idx):


        offset = self.idx - idx
        if self.encode_vowels  and  idx > 1  and  not self.isVowelAt(offset-1)  and  self.charAt(offset+1, 'E')  and  not self.charAt(offset-1, 'L')  and  not self.charAt(offset-1, 'R')  and  not self.isVowelAt(offset+2)  and  not self.stringStart("MCCLE", "MCLEL", "EMBLEM", "KADLEC", "ECCLESI", "COMPLEC", "COMPLEJ", "ROBLEDO")  and  not (idx+2 == self.last_idx  and  self.stringAt(offset, "LET"))  and  not self.stringAt(offset, "LEG", "LER", "LEX", "LESS", "LESQ", "LECT", "LEDG", "LETE", "LETH", "LETS", "LETT", "LETUS", "LETIV", "LETELY", "LETTER", "LETION", "LETIAN", "LETING", "LETORY", "LETTING")  and  not (self.stringAt(offset, "LEMENT")  and  not (self.stringAt(-4, "BATTLE", "TANGLE", "PUZZLE", "RABBLE", "BABBLE")  or  self.stringAt(-3, "TABLE")))  and  not (idx+2 == self.last_idx  and  self.stringAt(offset-2, "OCLES", "ACLES", "AKLES"))  and  not self.stringAt(offset-3, "LISLE", "AISLE")  and  not self.stringStart("ISLE")  and  not self.stringStart("ROBLES")  and  not self.stringAt(offset-4, "PROBLEM", "RESPLEN")  and  not self.stringAt(offset-3, "REPLEN")  and  not self.stringAt(offset-2, "SPLE")  and  not self.charAt(offset-1, 'H')  and  not self.charAt(offset-1, 'W'):

            self.metaphAddStr("AL", "AL")
            self.flag_al_inversion = True


            if self.charAt(offset+2, 'L'):
                self.idx = idx + 2
            return True

        return False

    def encodeVowelPreserveVowelAfterL(self, idx):
        offset = idx - self.idx

        if self.encode_vowels  and  not self.isVowelAt(offset-1)  and  self.charAt(offset+1, 'E')  and  idx > 1  and  idx+1 != self.last_idx  and  not (self.stringAt(offset+1, "ES", "ED")  and  idx+2 == self.last_idx)  and  not self.stringAt(offset-1, "RLEST"):

            self.metaphAddStr("LA", "LA")
            self.idx = self.skipVowels(self.idx + 1)
            return True

        return False

    def encodeLeCases(self, idx):
        if self.encodeVowelLeTransposition(idx):
            return

        if self.encodeVowelPreserveVowelAfterL(idx):
            return
        self.metaphAdd('L')

    def encodeM(self):
        if self.encodeSilentMAtBeginning()  or  self.encodeMrAndMrs()  or  self.encodeMac()  or  self.encodeMpt():
            return



        self.encodeMb()

        self.metaphAdd('M')

    def encodeSilentMAtBeginning(self):
        return self.stringAtStart(0, "MN")

    def encodeMrAndMrs(self):
        if self.stringExact("MR"):
            if self.encode_vowels:
                self.metaphAddStr("MASTAR", "MASTAR")
            else:
                self.metaphAddStr("MSTR", "MSTR")
            self.idx += 1
            return True
        elif self.stringExact("MRS"):
            if self.encode_vowels:
                self.metaphAddStr("MASAS", "MASAS")
            else:
                self.metaphAddStr("MSS", "MSS")
            self.idx += 2
            return True

        return False

    def encodeMac(self):


        if self.stringAtStart(0, "MC", "MACIVER", "MACEWEN", "MACELROY", "MACILROY", "MACINTOSH"):
            if self.encode_vowels:
                self.metaphAddStr("MAK", "MAK")
            else:
                self.metaphAddStr("MK", "MK")

            if self.stringStart("MC"):

                if self.stringAt(2, "K", "G", "Q")  and  not self.stringAt(2, "GEOR"):
                    self.idx += 2
                else:
                    self.idx += 1
            else:
                self.idx += 2

            return True

        return False

    def encodeMpt(self):
        if self.stringAt(-2, "COMPTROL")  or  self.stringAt(-4, "ACCOMPT"):
            self.metaphAdd('N')
            self.idx += 1
            return True

        return False

    def testSilentMb1(self):


        return self.stringAtStart(-3, "THUMB")  or  self.stringAtStart(-2, "DUMB", "BOMB", "DAMN", "LAMB", "NUMB", "TOMB")

    def testPronouncedMb(self):
        return self.stringAt(-2, "NUMBER")  or  (self.stringAt(2, "A", "O")  and  not self.stringAt(-2, "DUMBASS"))  or  self.stringAt(-2, "LAMBEN", "LAMBER", "LAMBET", "TOMBIG", "LAMBRE")

    def testSilentMb2(self):

        return self.charNextIs('B')  and  self.idx > 1  and  (self.idx+1 == self.last_idx  or self.stringAt(2, "ING", "ABL", "LIKE")  or  self.stringAtEnd(2, "S")  or  self.stringAt(-5, "BUNCOMB")  or (self.stringAtEnd(2, "ED", "ER")  and  (self.stringStart("CLIMB", "PLUMB")  or  not self.stringAt(-1, "IMBER", "AMBER", "EMBER", "UMBER"))  and  not self.stringAt(-2, "CUMBER", "SOMBER")))

    def testPronouncedMb2(self):

        return self.stringAt(-1, "OMBAS", "OMBAD", "UMBRA")  or  self.stringAt(-3, "FLAM")

    def testMn(self):
        return self.charNextIs('N')  and  (self.idx+1 == self.last_idx  or self.stringAtEnd(2, "S", "LY", "ER", "ED", "ING", "EST")  or  self.stringAt(-2, "DAMNEDEST")  or  self.stringAt(-5, "GODDAMNIT"))

    def encodeMb(self):
        if self.testSilentMb1():
            if not self.testPronouncedMb():
                self.idx += 1
        elif self.testSilentMb2():
            if not self.testPronouncedMb2():
                self.idx += 1
        elif self.testMn()  or  self.charNextIs('M'):
            self.idx += 1

    def encodeN(self):
        if self.encodeNce():
            return


        if self.charNextIs('N'):
            self.idx += 1


        if not self.stringAt(-2, "MONSIEUR")  and  not self.stringAt(-2, "NENESS"):
            self.metaphAdd('N')



    def encodeNce(self):

        if self.stringAt(1, "C", "S")  and  self.stringAt(2, "E", "Y", "I")  and  (self.idx+2 == self.last_idx  or  (self.idx+3 == self.last_idx  and  self.charAt(3, 'S'))):

            self.metaphAddStr("NTS", "NTS")
            self.idx += 1
            return True

        return False

    def encodeP(self):
        if self.encodeSilentPAtBeginning()  or  self.encodePt()  or  self.encodePh()  or  self.encodePph()  or  self.encodeRps()  or  self.encodeCoup()  or  self.encodePneum()  or  self.encodePsych()  or  self.encodePsalm():
            return

        self.encodePb()

        self.metaphAdd('P')

    def encodeSilentPAtBeginning(self):
        return self.stringAtStart(0, "PN", "PF", "PS", "PT")

    def encodePt(self):

        if self.charNextIs('T')  and  (self.stringAtStart(0, "PTERO")  or  self.stringAt(-5, "RECEIPT")  or  self.stringAt(-4, "ASYMPTOT")):

            self.metaphAdd('T')
            self.idx += 1
            return True

        return False




    def encodePh(self):
        if self.charNextIs('H'):

            if self.stringAt(0, "PHTHALEIN")  or  self.stringAtStart(0, "PHTH")  or  self.stringAt(-3, "APOPHTHEGM"):
                self.metaphAdd('0')
                self.idx += 3
            elif self.idx > 0  and  (self.stringAt(2, "AM", "EAD", "OLE", "ELD", "ILL", "OLD", "EAP", "ERD", "ARD", "ANG", "ORN", "EAV", "ART", "OUSE", "AMMER", "AZARD", "UGGER", "OLSTER")  and  not self.stringAt(-1, "LPHAM"))  and  not self.stringAt(-3, "LYMPH", "NYMPH"):


                self.metaphAdd('P')
                self.advanceCounter(2, 1)
            else:
                self.metaphAdd('F')
                self.idx += 1

            return True

        return False

    def encodePph(self):

        if self.charNextIs('P')  and  self.idx+2 < len(self.word)  and  self.charAt(2, 'H'):
            self.metaphAdd('F')
            self.idx += 2
            return True
        return False

    def encodeRps(self):

        if self.stringAt(-3, "CORPS")  and  not self.stringAt(-3, "CORPSE"):
            self.idx += 1
            return True
        return False

    def encodeCoup(self):

        return self.stringAtEnd(-3, "COUP")  and  not self.stringAt(-5, "RECOUP")

    def encodePneum(self):

        if self.stringAt(1, "NEUM"):
            self.metaphAdd('N')
            self.idx += 1
            return True
        return False

    def encodePsych(self):

        if self.stringAt(1, "SYCH"):
            if self.encode_vowels:
                self.metaphAddStr("SAK", "SAK")
            else:
                self.metaphAddStr("SK", "SK")
            self.idx += 4
            return True
        return False

    def encodePsalm(self):
        if self.stringAt(1, "SALM"):
            if self.encode_vowels:
                self.metaphAddStr("SAM", "SAM")
            else:
                self.metaphAddStr("SM", "SM")
            self.idx += 4
            return True
        return False

    def encodePb(self):


        if self.stringAt(1, "P", "B"):
            self.idx += 1

    def encodeQ(self):

        if self.stringAt(0, "QIN"):
            self.metaphAdd('X')
            return


        if self.charNextIs('Q'):
            self.idx += 1
        self.metaphAdd('K')

    def encodeR(self):
        if self.encodeRz():
            return

        if not self.testSilentR()  and  not self.encodeVowelReTransposition():
            self.metaphAdd('R')


        if self.charNextIs('R')  or  self.stringAt(-6, "POITIERS"):
            self.idx += 1


    def encodeRz(self):
        if self.stringAt(-2, "GARZ", "KURZ", "MARZ", "MERZ", "HERZ", "PERZ", "WARZ")  or  self.stringAt(0, "RZANO", "RZOLA")  or  self.stringAt(-1, "ARZA", "ARZN"):
            return False



        if self.stringAt(-4, "YASTRZEMSKI"):
            self.metaphAddAlt('R', 'X')
            self.idx += 1
            return True




        if self.stringAt(-1, "BRZEZINSKI"):
            self.metaphAddStr("RS", "RJ")

            self.idx += 3
            return True



        if self.stringAt(-1, "TRZ", "PRZ", "KRZ")  or  (self.stringAt(0, "RZ")  and  (self.isVowelAt(-1)  or  self.idx == 0)):
            self.metaphAddStr("RS", "X")
            self.idx += 1
            return True



        if self.stringAt(-1, "BRZ", "DRZ", "GRZ"):
            self.metaphAddStr("RS", "J")
            self.idx += 1
            return True

        return False

    def testSilentR(self):



        if (self.idx == self.last_idx  and  self.stringAt(-2, "IER")  and  (self.stringAt(-5, "MET", "VIV", "LUC")  or  self.stringAt(-6, "CART", "DOSS", "FOUR", "OLIV", "BUST", "DAUM", "ATEL", "SONN", "CORM", "MERC", "PELT", "POIR", "BERN", "FORT", "GREN", "SAUC", "GAGN", "GAUT", "GRAN", "FORC", "MESS", "LUSS", "MEUN", "POTH", "HOLL", "CHEN")  or  self.stringAt(-7, "CROUP", "TORCH", "CLOUT", "FOURN", "GAUTH", "TROTT", "DEROS", "CHART")  or  self.stringAt(-8, "CHEVAL", "LAVOIS", "PELLET", "SOMMEL", "TREPAN", "LETELL", "COLOMB")  or  self.stringAt(-9, "CHARCUT")  or  self.stringAt(-10, "CHARPENT")))  or  self.stringAt(-2, "SURBURB", "WORSTED", "WORCESTER")  or  self.stringAt(-7, "MONSIEUR")  or  self.stringAt(-6, "POITIERS"):

            return True

        return False


    def encodeVowelReTransposition(self):



        if self.encode_vowels  and  self.charNextIs('E')  and  len(self.word) > 3  and  not self.stringStart("OUTRE", "LIBRE", "ANDRE")  and  not self.stringExact("FRED", "TRES")  and  not self.stringAt(-2, "LDRED", "LFRED", "NDRED", "NFRED", "NDRES", "IFRED")  and  not self.isVowelAt(-1)  and  (self.idx+1 == self.last_idx  or  self.stringAtEnd(2, "D", "S")):

            self.metaphAddStr("AR", "AR")
            return True

        return False


    def encodeS(self):
        if self.encodeSkj()  or  self.encodeSpecialSw()  or  self.encodeSj()  or  self.encodeSilentFrenchSFinal()  or  self.encodeSilentFrenchSInternal()  or  self.encodeIsl()  or  self.encodeStl()  or  self.encodeChristmas()  or  self.encodeSthm()  or  self.encodeIsten()  or  self.encodeSugar()  or  self.encodeSh()  or  self.encodeSch()  or  self.encodeSur()  or  self.encodeSu()  or  self.encodeSsio()  or  self.encodeSs()  or  self.encodeSia()  or  self.encodeSio()  or  self.encodeAnglicisations()  or  self.encodeSc()  or  self.encodeSeiSuiSier()  or  self.encodeSea():
            return

        self.metaphAdd('S')

        if self.stringAt(1, "S", "Z")  and  not self.stringAt(1, "SH"):
            self.idx += 1

    def encodeSkj(self):
        if self.stringAt(0, "SKJO", "SKJU")  and  self.isVowelAt(3):
            self.metaphAdd('X')
            self.idx += 2
            return True
        return False

    def encodeSpecialSw(self):
        if self.idx == 0:
            if self.namesBeginningWithSwThatGetAltSv():
                self.metaphAddStr("S", "SV")
                self.idx += 1
                return True

            if self.namesBeginningWithSwThatGetAlvXV():
                self.metaphAddStr("S", "XV")
                self.idx += 1
                return True
        return False

    def namesBeginningWithSwThatGetAltSv(self):
        return self.stringStart("SWANSON", "SWENSON", "SWINSON", "SWENSEN", "SWOBODA", "SWIDERSKI", "SWARTHOUT", "SWEARENGIN")

    def namesBeginningWithSwThatGetAlvXV(self):
        return self.stringStart("SWART", "SWARTZ", "SWARTS", "SWIGER", "SWITZER", "SWANGER", "SWIGERT", "SWIGART", "SWIHART", "SWEITZER", "SWATZELL", "SWINDLER", "SWINEHART", "SWEARINGEN")

    def encodeSj(self):
        if self.stringStart("SJ"):
            self.metaphAdd('X')
            self.idx += 1
            return True
        return False

    def encodeSilentFrenchSFinal(self):

        if self.stringStart("LOUIS")  and  self.idx == self.last_idx:
            self.metaphAddAlt('S', REPLACEMENT_CHAR)
            return True

        if self.idx == self.last_idx  and  ((self.stringStart("YVES", "ARKANSAS", "FRANCAIS", "CRUDITES", "BRUYERES", "DESCARTES", "DESCHUTES", "DESCHAMPS", "DESROCHES", "DESCHENES", "RENDEZVOUS", "CONTRETEMPS", "DESLAURIERS")  or  self.stringExact("HORS")  or  self.stringEnd("CAMUS", "YPRES", "MESNES", "DEBRIS", "BLANCS", "INGRES", "CANNES", "CHABLIS", "APROPOS", "JACQUES", "ELYSEES", "OEUVRES", "GEORGES", "DESPRES"))  or  (self.stringAt(-2, "AI", "OI", "UI")  and  not self.stringStart("LOIS", "LUIS"))):

            return True
        return False

    def encodeSilentFrenchSInternal(self):

        return self.stringAt(-2, "MESNES", "DESCHAM", "DESPRES", "DESROCH", "DESROSI", "DESJARD", "DESMARA", "DESCHEN", "DESHOTE", "DESLAUR", "DESCARTES")  or  self.stringAt(-5, "DUQUESNE", "DUCHESNE")  or  self.stringAt(-3, "FRESNEL", "GROSVENOR")  or  self.stringAt(-4, "LOUISVILLE")  or  self.stringAt(-7, "BEAUCHESNE", "ILLINOISAN")

    def encodeIsl(self):

        return (self.stringAt(-2, "LISL", "LYSL", "AISL")  and  not self.stringAt(-3, "PAISLEY", "BAISLEY", "ALISLAM", "ALISLAH", "ALISLAA"))  or  (self.idx == 1  and  (self.stringAt(-1, "ISLE", "ISLAN")  and  not self.stringAt(-1, "ISLEY", "ISLER")))

    def encodeStl(self):

        if (self.stringAt(0, "STLE", "STLI")  and  not self.stringAt(2, "LESS", "LIKE", "LINE"))  or  self.stringAt(-3, "THISTLY", "BRISTLY", "GRISTLY")  or  self.stringAt(-1, "USCLE"):



            if self.stringStart("KRISTEN", "KRYSTLE", "CRYSTLE", "KRISTLE", "CHRISTENSEN", "CHRISTENSON")  or  self.stringAt(-3, "FIRSTLING")  or  self.stringAt(-2, "NESTLING", "WESTLING"):
                self.metaphAddStr("ST", "ST")
                self.idx += 1
            else:
                if self.encode_vowels  and  self.charAt(3, 'E')  and  not self.charAt(4, 'R')  and  not self.stringAt(3, "EY", "ETTE", "ETTA"):

                    self.metaphAddStr("SAL", "SAL")
                    self.flag_al_inversion = True
                else:
                    self.metaphAddStr("SL", "SL")
                self.idx += 2
            return True

        return False

    def encodeChristmas(self):
        if self.stringAt(-4, "CHRISTMA"):
            self.metaphAddStr("SM", "SM")
            self.idx += 2
            return True
        return False

    def encodeSthm(self):

        if self.stringAt(0, "STHM"):
            self.metaphAddStr("SM", "SM")
            self.idx += 3
            return True
        return False

    def encodeIsten(self):

        if self.stringStart("CHRISTEN"):
            if rootOrInflections(self.word, "CHRISTEN")  or  self.stringStart("CHRISTENDOM"):
                self.metaphAddStr("S", "ST")
            else:

                self.metaphAddStr("ST", "ST")
            self.idx += 1
            return True


        if self.stringAt(-2, "LISTEN", "RISTEN", "HASTEN", "FASTEN", "MUSTNT")  or  self.stringAt(-3, "MOISTEN"):
            self.metaphAdd('S')
            self.idx += 1
            return True

        return False

    def encodeSugar(self):
        if self.stringAt(0, "SUGAR"):
            self.metaphAdd('X')
            return True
        return False

    def encodeSh(self):
        if self.stringAt(0, "SH"):

            if self.stringAt(-2, "CASHMERE"):
                self.metaphAdd('J')
                self.idx += 1
                return True


            if self.idx > 0  and  (self.stringAtEnd(1, "HAP")  or  self.stringAt(1, "HEIM", "HOEK", "HOLM", "HOLZ", "HOOD", "HEAD", "HEID", "HAAR", "HORS", "HOLE", "HUND", "HELM", "HAWK", "HILL", "HEART", "HATCH", "HOUSE", "HOUND", "HONOR")  or  self.stringAtEnd(2, "EAR")  or  (self.stringAt(2, "ORN")  and  not self.stringAt(-2, "UNSHORN"))  or  (self.stringAt(1, "HOUR")  and  not self.stringStart("ASHOUR", "BASHOUR", "MANSHOUR"))  or  self.stringAt(2, "ARMON", "ONEST", "ALLOW", "OLDER", "OPPER", "EIMER", "ANDLE", "ONOUR", "ABILLE", "UMANCE", "ABITUA")):
                if not self.stringAt(-1, "S"):
                    self.metaphAdd('S')
            else:
                self.metaphAdd('X')

            self.idx += 1
            return True

        return False

    def encodeSch(self):

        if self.stringAt(1, "CH"):
            if self.idx > 0  and  (self.stringAt(3, "IEF", "EAT", "ANCE", "ARGE")  or  self.stringStart("ESCHEW")):

                self.metaphAdd('S')
                return True




            if (self.stringAt(3, "OO", "ER", "EN", "UY", "ED", "EM", "IA", "IZ", "IS", "OL")  and  not self.stringAt(0, "SCHOLT", "SCHISL", "SCHERR"))  or  self.stringAt(3, "ISZ")  or  (self.stringAt(-1, "ESCHAT", "ASCHIN", "ASCHAL", "ISCHAE", "ISCHIA")  and  not self.stringAt(-2, "FASCHING"))  or  self.stringAtEnd(-1, "ESCHI")  or  self.charAt(3, 'Y'):


                if self.stringAt(3, "ER", "EN", "IS")  and  (self.idx+4 == self.last_idx  or  self.stringAt(3, "ENK", "ENB", "IST")):

                    self.metaphAddStr("X", "SK")
                else:
                    self.metaphAddStr("SK", "SK")
            else:
                self.metaphAdd('X')

            self.idx += 2
            return True

        return False

    def encodeSur(self):

        if self.stringAt(1, "URE", "URA", "URY"):

            if self.idx == 0  or  self.stringAt(-1, "N", "K")  or  self.stringAt(-2, "NO"):
                self.metaphAdd('X')
            else:
                self.metaphAdd('J')

            self.advanceCounter(1, 0)
            return True
        return False

    def encodeSu(self):

        if self.stringAt(1, "UO", "UA")  and  self.idx != 0:

            if self.stringAt(-1, "RSUA"):
                self.metaphAdd('S')
            elif self.isVowelAt(-1):

                self.metaphAddAlt('J', 'S')
            else:
                self.metaphAddAlt('X', 'S')

            self.advanceCounter(2, 0)
            return True
        return False

    def encodeSsio(self):
        if self.stringAt(1, "SION"):

            if self.stringAt(-2, "CI"):
                self.metaphAdd('J')
            elif self.isVowelAt(-1):

                self.metaphAdd('X')

            self.advanceCounter(3, 1)
            return True
        return False

    def encodeSs(self):


        if self.stringAt(-1, "USSIA", "ESSUR", "ISSUR", "ISSUE", "ESSIAN", "ASSURE", "ASSURA", "ISSUAB", "ISSUAN", "ASSIUS"):
            self.metaphAdd('X')
            self.advanceCounter(2, 1)
            return True
        return False

    def encodeSia(self):

        if self.stringAt(-2, "CHSIA")  or  self.stringAt(-1, "RSIAL"):
            self.metaphAdd('X')
            self.advanceCounter(2, 0)
            return True


        if (self.stringAtStart(-3, "ALESIA", "ALYSIA", "ALISIA", "STASIA")  and  not self.stringStart("ANASTASIA"))  or  self.stringAt(-5, "THERESIA", "DIONYSIAN"):

            self.metaphAddAlt('X', 'S')
            self.advanceCounter(2, 0)
            return True

        if self.stringAtEnd(0, "SIA", "SIAN")  or  self.stringAt(-5, "AMBROSIAL"):
            if (self.isVowelAt(-1)  or  self.stringAt(-1, "R"))  and  not (self.stringStart("JAMES", "NICOS", "PEGAS", "PEPYS", "HOBBES", "HOLMES", "JAQUES", "KEYNES", "MALTHUS", "HOMOOUS", "MAGLEMOS", "HOMOIOUS", "LEVALLOIS", "TARDENOIS")  or  self.stringAt(-4, "ALGES")):

                self.metaphAdd('J')
            else:
                self.metaphAdd('S')

            self.advanceCounter(1, 0)
            return True

        return False

    def encodeSio(self):

        if self.stringStart("SIOBHAN"):
            self.metaphAdd('X')
            self.advanceCounter(2, 0)
            return True
        if self.stringAt(1, "ION"):

            if self.isVowelAt(-1)  or  self.stringAt(-2, "ER", "UR"):
                self.metaphAdd('J')
            else:

                self.metaphAdd('X')
            self.advanceCounter(2, 0)
            return True
        return False

    def encodeAnglicisations(self):




        if self.stringAtStart(0, "SM", "SN", "SL")  or  self.stringAt(1, "Z"):
            self.metaphAddAlt('S', 'X')


            if self.stringAt(1, "Z"):
                self.idx += 1

            return True

        return False

    def encodeSc(self):
        if self.stringAt(0, "SC"):

            if self.stringAt(-2, "VISCOUNT"):
                return True


            if self.stringAt(2, "I", "E", "Y"):


                if self.stringAt(2, "IUT", "IOUS")  or  self.stringAt(-2, "FASCIS")  or  self.stringAt(-3, "CONSCIEN", "CRESCEND", "CONSCION")  or  self.stringAt(-4, "OMNISCIEN"):
                    self.metaphAdd('X')
                elif self.stringAt(0, "SCIVV", "SCIRO", "SCIPIO", "SCEPTIC", "SCEPSIS")  or  self.stringAt(-2, "PISCITELLI"):
                    self.metaphAddStr("SK", "SK")
                else:
                    self.metaphAdd('S')

                self.idx += 1
                return True

            self.metaphAddStr("SK", "SK")
            self.idx += 1
            return True
        return False

    def encodeSeiSuiSier(self):



        if self.stringAtEnd(-3, "NAUSEA")  or  self.stringAt(-2, "CASUI")  or  (self.stringAt(-1, "OSIER", "ASIER")  and  not (self.stringStart("OSIER", "EASIER")  or  self.stringAt(-2, "ROSIER", "MOSIER"))):

            self.metaphAddAlt('J', 'X')
            self.advanceCounter(2, 0)
            return True

        return False

    def encodeSea(self):

        if self.stringExact("SEAN")  or  (self.stringAt(-3, "NAUSEO")  and  not self.stringAt(-3, "NAUSEAT")):
            self.metaphAdd('X')
            self.advanceCounter(2, 0)
            return True
        return False

    def encodeT(self):
        if self.encodeTInitial()  or  self.encodeTch()  or  self.encodeSilentFrenchT()  or  self.encodeTunTulTuaTuo()  or  self.encodeTueTeuTeouTulTie()  or  self.encodeTurTiuSuffixes()  or  self.encodeTi()  or  self.encodeTient()  or  self.encodeTsch()  or  self.encodeTzsch()  or  self.encodeThPronouncedSeparately()  or  self.encodeTth()  or  self.encodeTh():
            return

        if self.stringAt(1, "T", "D"):
            self.idx += 1
        self.metaphAdd('T')

    def encodeTInitial(self):
        if self.idx == 0:

            if self.stringAt(1, "SAR", "ZAR"):
                return True


            if self.stringExact("TSO", "TSA", "TSU", "TSAO", "TSAI", "TSING", "TSANG"):
                self.metaphAdd('X')
                self.advanceCounter(2, 1)
                return True


            if self.charNextIs('S')  and  self.isVowelAt(2):
                self.metaphAddStr("TS", "S")
                self.advanceCounter(2, 1)
                return True


            if self.charNextIs('J'):
                self.metaphAdd('X')
                self.advanceCounter(2, 1)
                return True

            if self.stringExact("THU")  or  self.stringAt(1, "HAI", "HUY", "HAO", "HYME", "HYMY", "HANH", "HERES"):
                self.metaphAdd('T')
                self.advanceCounter(2, 1)
                return True

        return False

    def encodeTch(self):
        if self.stringAt(1, "CH"):
            self.metaphAdd('X')
            self.idx += 2
            return True
        return False

    def encodeSilentFrenchT(self):

        return (self.stringAtEnd(-4, "MONET", "GENET", "CHAUT")  or  self.stringAt(-2, "POTPOURRI")  or  self.stringAt(-3, "MORTGAGE", "BOATSWAIN")  or  self.stringAt(-4, "BERET", "BIDET", "FILET", "DEBUT", "DEPOT", "PINOT", "TAROT")  or  self.stringAt(-5, "BALLET", "BUFFET", "CACHET", "CHALET", "ESPRIT", "RAGOUT", "GOULET", "CHABOT", "BENOIT")  or  self.stringAt(-6, "GOURMET", "BOUQUET", "CROCHET", "CROQUET", "PARFAIT", "PINCHOT", "CABARET", "PARQUET", "RAPPORT", "TOUCHET", "COURBET", "DIDEROT")  or  self.stringAt(-7, "ENTREPOT", "CABERNET", "DUBONNET", "MASSENET", "MUSCADET", "RICOCHET", "ESCARGOT")  or  self.stringAt(-8, "SOBRIQUET", "CABRIOLET", "CASSOULET", "OUBRIQUET", "CAMEMBERT"))  and  not self.stringAt(1, "AN", "RY", "IC", "OM", "IN")

    def encodeTunTulTuaTuo(self):

        if self.stringAt(-3, "FORTUN")  or  (self.stringAt(0, "TUL")  and  self.isVowelAt(-1)  and  self.isVowelAt(3))  or  self.stringAt(-2, "BITUA", "BITUE")  or  (self.idx > 1  and  self.stringAt(0, "TUA", "TUO")):

            self.metaphAddAlt('X', 'T')
            return True
        return False

    def encodeTueTeuTeouTulTie(self):
        if self.stringAt(1, "UENT")  or  self.stringAt(-4, "RIGHTEOUS")  or  self.stringAt(-3, "STATUTE", "AMATEUR", "STATUTOR")  or  self.stringAt(-1, "NTULE", "NTULA", "STULE", "STULA", "STEUR")  or  self.stringAtEnd(0, "TUE")  or  self.stringAt(0, "TUENC")  or  self.stringAtEnd(0, "TIENCE"):

            self.metaphAddAlt('X', 'T')
            self.advanceCounter(1, 0)
            return True

        return False

    def encodeTurTiuSuffixes(self):

        if self.idx > 0  and  self.stringAt(1, "URE", "URA", "URI", "URY", "URO", "IUS"):

            if (self.stringAtEnd(1, "URA", "URO")  and  not self.stringAt(-3, "VENTURA"))  or  self.stringAt(1, "URIA"):

                self.metaphAdd('T')
            else:
                self.metaphAddAlt('X', 'T')

            self.advanceCounter(1, 0)
            return True
        return False

    def encodeTi(self):


        if (self.stringAt(1, "IO")  and  not self.stringAt(-1, "ETIOL"))  or  self.stringAt(1, "IAL")  or  self.stringAt(-1, "RTIUM", "ATIUM")  or  ((self.stringAt(1, "IAN")  and  self.idx > 0)  and  not (self.stringAt(-4, "FAUSTIAN")  or  self.stringAt(-5, "PROUSTIAN")  or  self.stringAt(-2, "TATIANA")  or  self.stringAt(-3, "KANTIAN", "GENTIAN")  or  self.stringAt(-8, "ROOSEVELTIAN"))  or  (self.stringAtEnd(0, "TIA")  and  not (self.stringAt(-3, "HESTIA", "MASTIA")  or  self.stringAt(-2, "OSTIA")  or  self.stringStart("TIA")  or  self.stringAt(-5, "IZVESTIA")))  or  self.stringAt(1, "IATE", "IATI", "IABL", "IATO", "IARY")  or  self.stringAt(-5, "CHRISTIAN")):

            if self.stringAtStart(-2, "ANTI")  or  self.stringStart("PATIO", "PITIA", "DUTIA"):
                self.metaphAdd('T')
            elif self.stringAt(-4, "EQUATION"):
                self.metaphAdd('J')
            elif self.stringAt(0, "TION"):
                self.metaphAdd('X')
            elif self.stringStart("KATIA", "LATIA"):
                self.metaphAddAlt('T', 'X')
            else:
                self.metaphAddAlt('X', 'T')

            self.advanceCounter(2, 0)
            return True

        return False

    def encodeTient(self):

        if self.stringAt(1, "IENT"):
            self.metaphAddAlt('X', 'T')
            self.advanceCounter(2, 0)
            return True
        return False

    def encodeTsch(self):

        if self.stringAt(0, "TSCH")  and  not self.stringAt(-3, "WELT", "KLAT", "FEST"):


            self.metaphAdd('X')
            self.idx += 3
            return True
        return False

    def encodeTzsch(self):

        if self.stringAt(0, "TZSCH"):
            self.metaphAdd('X')
            self.idx += 4
            return True
        return False

    def encodeThPronouncedSeparately(self):

        if (self.idx > 0  and  self.stringAt(1, "HOOD", "HEAD", "HEID", "HAND", "HILL", "HOLD", "HAWK", "HEAP", "HERD", "HOLE", "HOOK", "HUNT", "HUMO", "HAUS", "HOFF", "HARD")  and  not self.stringAt(-3, "SOUTH", "NORTH"))  or  self.stringAt(1, "HOUSE", "HEART", "HASTE", "HYPNO", "HEQUE")  or  (self.stringAtEnd(1, "HALL")  and  not self.stringAt(-3, "SOUTH", "NORTH"))  or  (self.stringAtEnd(1, "HAM")  and  not self.stringStart("GOTHAM", "WITHAM", "LATHAM", "BENTHAM", "WALTHAM", "WORTHAM", "GRANTHAM"))  or  (self.stringAt(1, "HATCH")  and  not (self.idx == 0  or  self.stringAt(-2, "UNTHATCH")))  or  self.stringAt(-3, "GOETHE", "WARTHOG")  or  self.stringAt(-2, "ESTHER", "NATHALIE"):


            if self.stringAt(-3, "POSTHUM"):
                self.metaphAdd('X')
            else:
                self.metaphAdd('T')
            self.idx += 1
            return True

        return False

    def encodeTth(self):

        if self.stringAt(0, "TTH"):
            if self.stringAt(-2, "MATTH"):
                self.metaphAdd('0')
            else:
                self.metaphAddStr("T0", "T0")
            self.idx += 2
            return True

        return False

    def encodeTh(self):
        if self.stringAt(0, "TH"):

            if self.stringAt(-3, "CLOTHES"):

                self.idx += 2
                return True


            if self.stringAt(2, "OMAS", "OMPS", "OMPK", "OMSO", "OMSE", "AMES", "OVEN", "OFEN", "ILDA", "ILDE")  or  self.stringExact("THOM", "THOMS")  or  self.stringStart("SCH", "VAN ", "VON "):

                self.metaphAdd('T')
            else:


                if self.stringStart("SM"):
                    self.metaphAddAlt('0', 'T')
                else:
                    self.metaphAdd('0')

            self.idx += 1
            return True
        return False

    def encodeV(self):
        if self.charNextIs('V'):
            self.idx += 1
        self.metaphAddExactApprox("V", "F")

    def encodeW(self):
        if self.encodeSilentWAtBeginning()  or  self.encodeWitzWicz()  or  self.encodeWr()  or  self.encodeInitialWVowel()  or  self.encodeWh()  or  self.encodeEasternEuropeanW():
            return


        if self.encode_vowels  and  self.stringAtEnd(0, "WE"):
            self.metaphAdd('A')

    def encodeSilentWAtBeginning(self):
        return self.stringAtStart(0, "WR")

    def encodeWitzWicz(self):

        if self.stringAtEnd(0, "WICZ", "WITZ"):
            if self.encode_vowels:

                if len(self.prim_buf) > 0  and  self.prim_buf[len(self.prim_buf)-1] == 'A':
                    self.metaphAddStr("TS", "FAX")
                else:
                    self.metaphAddStr("ATS", "FAX")
            else:
                self.metaphAddStr("TS", "FX")

            self.idx += 3
            return True
        return False

    def encodeWr(self):

        if self.stringAt(0, "WR"):
            self.metaphAdd('R')
            self.idx += 1
            return True
        return False

    def encodeInitialWVowel(self):
        if self.idx == 0  and  self.isVowelAt(1):

            if self.germanicOrSlavicNameBeginningWithW():
                if self.encode_vowels:
                    self.metaphAddExactApproxAlt("A", "VA", "A", "FA")
                else:
                    self.metaphAddExactApproxAlt("A", "V", "A", "F")
            else:
                self.metaphAdd('A')

            self.idx = self.skipVowels(self.idx + 1)
            return True

        return False

    def encodeWh(self):
        if self.stringAt(0, "WH"):


            if self.charAt(2, 'O')  and  not self.stringAt(2, "OA", "OP", "OOP", "OMP", "ORL", "ORT", "OOSH"):
                self.metaphAdd('H')
                self.advanceCounter(2, 1)
                return True


            if self.stringAt(2, "IDE", "ARD", "EAD", "AWK", "ERD", "OOK", "AND", "OLE", "OOD", "EART", "OUSE", "OUND", "AMMER"):
                self.metaphAdd('H')
                self.idx += 1
                return True

            if self.idx == 0:
                self.metaphAdd('A')
                self.idx = self.skipVowels(self.idx + 2)
                return True

            self.idx += 1
            return True

        return False

    def encodeEasternEuropeanW(self):

        if (self.idx == self.last_idx  and  self.isVowelAt(-1))  or  self.stringAt(-1, "EWSKI", "EWSKY", "OWSKI", "OWSKY")  or  self.stringAtEnd(0, "WIAK", "WICKI", "WACKI")  or  self.stringStart("SCH"):

            self.metaphAddExactApproxAlt("", "V", "", "F")
            return True
        return False

    def germanicOrSlavicNameBeginningWithW(self):
        return self.stringStart("WEE", "WIX", "WAX", "WOLF", "WEIS", "WAHL", "WALZ", "WEIL", "WERT", "WINE", "WILK", "WALT", "WOLL", "WADA", "WULF", "WEHR", "WURM", "WYSE", "WENZ", "WIRT", "WOLK", "WEIN", "WYSS", "WASS", "WANN", "WINT", "WINK", "WILE", "WIKE", "WIER", "WELK", "WISE", "WIRTH", "WIESE", "WITTE", "WENTZ", "WOLFF", "WENDT", "WERTZ", "WILKE", "WALTZ", "WEISE", "WOOLF", "WERTH", "WEESE", "WURTH", "WINES", "WARGO", "WIMER", "WISER", "WAGER", "WILLE", "WILDS", "WAGAR", "WERTS", "WITTY", "WIENS", "WIEBE", "WIRTZ", "WYMER", "WULFF", "WIBLE", "WINER", "WIEST", "WALKO", "WALLA", "WEBRE", "WEYER", "WYBLE", "WOMAC", "WILTZ", "WURST", "WOLAK", "WELKE", "WEDEL", "WEIST", "WYGAN", "WUEST", "WEISZ", "WALCK", "WEITZ", "WYDRA", "WANDA", "WILMA", "WEBER", "WETZEL", "WEINER", "WENZEL", "WESTER", "WALLEN", "WENGER", "WALLIN", "WEILER", "WIMMER", "WEIMER", "WYRICK", "WEGNER", "WINNER", "WESSEL", "WILKIE", "WEIGEL", "WOJCIK", "WENDEL", "WITTER", "WIENER", "WEISER", "WEXLER", "WACKER", "WISNER", "WITMER", "WINKLE", "WELTER", "WIDMER", "WITTEN", "WINDLE", "WASHER", "WOLTER", "WILKEY", "WIDNER", "WARMAN", "WEYANT", "WEIBEL", "WANNER", "WILKEN", "WILTSE", "WARNKE", "WALSER", "WEIKEL", "WESNER", "WITZEL", "WROBEL", "WAGNON", "WINANS", "WENNER", "WOLKEN", "WILNER", "WYSONG", "WYCOFF", "WUNDER", "WINKEL", "WIDMAN", "WELSCH", "WEHNER", "WEIGLE", "WETTER", "WUNSCH", "WHITTY", "WAXMAN", "WILKER", "WILHAM", "WITTIG", "WITMAN", "WESTRA", "WEHRLE", "WASSER", "WILLER", "WEGMAN", "WARFEL", "WYNTER", "WERNER", "WAGNER", "WISSER", "WISEMAN", "WINKLER", "WILHELM", "WELLMAN", "WAMPLER", "WACHTER", "WALTHER", "WYCKOFF", "WEIDNER", "WOZNIAK", "WEILAND", "WILFONG", "WIEGAND", "WILCHER", "WIELAND", "WILDMAN", "WALDMAN", "WORTMAN", "WYSOCKI", "WEIDMAN", "WITTMAN", "WIDENER", "WOLFSON", "WENDELL", "WEITZEL", "WILLMAN", "WALDRUP", "WALTMAN", "WALCZAK", "WEIGAND", "WESSELS", "WIDEMAN", "WOLTERS", "WIREMAN", "WILHOIT", "WEGENER", "WOTRING", "WINGERT", "WIESNER", "WAYMIRE", "WHETZEL", "WENTZEL", "WINEGAR", "WESTMAN", "WYNKOOP", "WALLICK", "WURSTER", "WINBUSH", "WILBERT", "WALLACH", "WYNKOOP", "WALLICK", "WURSTER", "WINBUSH", "WILBERT", "WALLACH", "WEISSER", "WEISNER", "WINDERS", "WILLMON", "WILLEMS", "WIERSMA", "WACHTEL", "WARNICK", "WEIDLER", "WALTRIP", "WHETSEL", "WHELESS", "WELCHER", "WALBORN", "WILLSEY", "WEINMAN", "WAGAMAN", "WOMMACK", "WINGLER", "WINKLES", "WIEDMAN", "WHITNER", "WOLFRAM", "WARLICK", "WEEDMAN", "WHISMAN", "WINLAND", "WEESNER", "WARTHEN", "WETZLER", "WENDLER", "WALLNER", "WOLBERT", "WITTMER", "WISHART", "WILLIAM", "WESTPHAL", "WICKLUND", "WEISSMAN", "WESTLUND", "WOLFGANG", "WILLHITE", "WEISBERG", "WALRAVEN", "WOLFGRAM", "WILHOITE", "WECHSLER", "WENDLING", "WESTBERG", "WENDLAND", "WININGER", "WHISNANT", "WESTRICK", "WESTLING", "WESTBURY", "WEITZMAN", "WEHMEYER", "WEINMANN", "WISNESKI", "WHELCHEL", "WEISHAAR", "WAGGENER", "WALDROUP", "WESTHOFF", "WIEDEMAN", "WASINGER", "WINBORNE", "WHISENANT", "WEINSTEIN", "WESTERMAN", "WASSERMAN", "WITKOWSKI", "WEINTRAUB", "WINKELMAN", "WINKFIELD", "WANAMAKER", "WIECZOREK", "WIECHMANN", "WOJTOWICZ", "WALKOWIAK", "WEINSTOCK", "WILLEFORD", "WARKENTIN", "WEISINGER", "WINKLEMAN", "WILHEMINA", "WISNIEWSKI", "WUNDERLICH", "WHISENHUNT", "WEINBERGER", "WROBLEWSKI", "WAGUESPACK", "WEISGERBER", "WESTERVELT", "WESTERLUND", "WASILEWSKI", "WILDERMUTH", "WESTENDORF", "WESOLOWSKI", "WEINGARTEN", "WINEBARGER", "WESTERBERG", "WANNAMAKER", "WEISSINGER", "WALDSCHMIDT", "WEINGARTNER", "WINEBRENNER", "WOLFENBARGER", "WOJCIECHOWSKI")

    def encodeX(self):
        if self.encodeInitialX()  or  self.encodeGreekX()  or  self.encodeXSpecialCases()  or  self.encodeXToH()  or  self.encodeXVowel()  or  self.encodeFrenchXFinal():
            return



        if self.stringAt(1, "X", "Z", "S", "CI", "CE"):
            self.idx += 1

    def encodeInitialX(self):

        if self.stringStart("XU", "XIA", "XIO", "XIE"):
            self.metaphAdd('X')
            return True

        if self.idx == 0:
            self.metaphAdd('S')
            return True

        return False


    def encodeGreekX(self):
        if self.stringAt(1, "YLO", "YLE", "ENO", "ANTH"):
            self.metaphAdd('S')
            return True
        return False


    def encodeXSpecialCases(self):
        if self.stringAt(-2, "LUXUR"):
            self.metaphAddExactApprox("GJ", "KJ")
            return True

        if self.stringStart("TEXEIRA", "TEIXEIRA"):
            self.metaphAdd('X')
            return True
        return False



    def encodeXToH(self):
        if self.stringAt(-2, "OAXACA")  or  self.stringAt(-3, "QUIXOTE"):
            self.metaphAdd('H')
            return True
        return False

    def encodeXVowel(self):

        if self.stringAt(1, "UAL", "ION", "IOU"):
            self.metaphAddStr("KX", "KS")
            self.advanceCounter(2, 0)
            return True
        return False

    def encodeFrenchXFinal(self):
        if not (self.idx == self.last_idx  and  (self.stringAt(-3, "IAU", "EAU", "IEU")  or  self.stringAt(-2, "AI", "AU", "OU", "OI", "EU"))):

            self.metaphAddStr("KS", "KS")

        return False

    def encodeZ(self):
        if self.encodeZz()  or  self.encodeZuZierZs()  or  self.encodeFrenchEz()  or  self.encodeGermanZ()  or  self.encodeZh():
            return

        self.metaphAdd('S')


        if self.charNextIs('Z'):
            self.idx += 1



    def encodeZz(self):

        if self.charNextIs('Z')  and  (self.stringAtEnd(2, "I", "O", "A")  or  self.stringAt(-2, "MOZZARELL", "PIZZICATO", "PUZZONLAN")):

            self.metaphAddStr("TS", "S")
            self.idx += 1
            return True
        return False

    def encodeZuZierZs(self):
        if (self.idx == 1  and  self.stringAt(-1, "AZUR"))  or  (self.stringAt(0, "ZIER")  and  not self.stringAt(-2, "VIZIER"))  or  self.stringAt(0, "ZSA"):

            self.metaphAddAlt('J', 'S')

            if self.stringAt(0, "ZSA"):
                self.idx += 1
            return True
        return False



    def encodeFrenchEz(self):
        if (self.idx == 3  and  self.stringAt(-3, "CHEZ"))  or  self.stringAt(-5, "RENDEZ"):
            return True

        return False


    def encodeGermanZ(self):
        if self.stringExact("NAZI")  or  self.stringAt(-2, "NAZIFY", "MOZART")  or  self.stringAt(-3, "HOLZ", "HERZ", "MERZ", "FITZ", "HERZOG")  or  (self.stringAt(-3, "GANZ")  and  not self.isVowelAt(1))  or  self.stringAt(-4, "STOLZ", "PRINZ", "VENEZIA")  or  (self.stringContains("SCH")  and  not self.stringEnd("IZE", "OZE", "ZEL"))  or  (self.idx > 0  and  self.stringAt(0, "ZEIT"))  or  self.stringAt(-3, "WEIZ"):

            if self.idx > 0  and  self.charAt(-1, 'T'):
                self.metaphAdd('S')
            else:
                self.metaphAddStr("TS", "TS")
            return True

        return False

    def encodeZh(self):

        if self.charNextIs('H'):
            self.metaphAdd('J')
            self.idx += 1
            return True
        return False

    def encodeVowels(self):

        if self.idx == 0:


            self.metaphAdd('A')
        elif self.encode_vowels:
            if not self.charAt(0, 'E'):
                if self.encodeSkipSilentUe():
                    return
                if self.encodeOSilent():
                    return


                self.metaphAdd('A')

            else:
                self.encodeEPronounced()

        if not (not self.isVowelAt(-2)  and  self.stringAt(-1, "LEWA", "LEWO", "LEWI")):
            self.idx = self.skipVowels(self.idx + 1)

    def encodeSkipSilentUe(self):

        if (self.stringAt(-1, "QUE", "GUE")  and  not self.stringStart("RISQUE", "PIROGUE", "ENRIQUE", "BARBEQUE", "PALENQUE", "APPLIQUE", "COMMUNIQUE")  and  not self.stringAt(-3, "ARGUE", "SEGUE"))  and  self.idx > 1  and  ((self.idx+1 == self.last_idx)  or  self.stringStart("JACQUES")):

            self.idx = self.skipVowels(self.idx)
            return True
        return False




    def encodeEPronounced(self):


        if self.stringExact("LAME", "SAKE", "PATE", "AGAPE")  or  (self.stringStart("RESUME")  and  self.idx == 5):

            self.metaphAddAlt(REPLACEMENT_CHAR, 'A')
            return


        if self.stringExact("INGE"):
            self.metaphAddAlt('A', REPLACEMENT_CHAR)
            return




        if self.idx == 5  and  self.stringStart("BLESSED", "LEARNED"):
            self.metaphAddExactApproxAlt("D", "AD", "T", "AT")
            self.idx += 1
            return


        if (not self.encodeESilent()  and  not self.flag_al_inversion  and  not self.encodeSilentInternalE())  or  self.encodeEPronouncedExceptions():

            self.metaphAdd('A')


        self.flag_al_inversion = False

    def encodeOSilent(self):

        if self.charAt(0, 'O')  and  self.stringAt(-2, "IRON"):
            if (self.stringStart("IRON")  or  self.stringAtEnd(-2, "IRON"))  and  not self.stringAt(-2, "IRONIC"):
                return True

        return False

    def encodeESilent(self):
        if self.encodeEPronouncedAtEnd():
            return False


        if self.idx == self.last_idx  or  (self.idx > 1  and  self.idx+1 == self.last_idx  and  self.stringAt(1, "S", "D")  and  not (self.stringAt(-1, "TED", "SES", "CES")  or  self.stringStart("ABED", "IMED", "JARED", "AHMED", "HAMED", "JAVED", "NORRED", "MEDVED", "MERCED", "ALLRED", "KHALED", "RASHED", "MASJED", "MOHAMED", "MOHAMMED", "MUHAMMED", "MOUHAMED", "ANTIPODES", "ANOPHELES")))  or  self.stringAtEnd(1, "NESS", "LESS")  or  (self.stringAtEnd(1, "LY")  and  not self.stringStart("CICELY")):

            return True
        return False











    def encodeEPronouncedAtEnd(self):
        if self.idx == self.last_idx  and  (self.stringAt(-6, "STROPHE")  or  len(self.word) == 2  or  (len(self.word) == 3  and  not self.isVowelAt(-self.idx))  or  (self.stringAtEnd(-2, "BKE", "DKE", "FKE", "KKE", "LKE", "NKE", "MKE", "PKE", "TKE", "VKE", "ZKE")  and  not self.stringStart("FINKE", "FUNKE", "FRANKE"))  or  self.stringAtEnd(-4, "SCHKE")  or  self.stringExact("ACME", "NIKE", "CAFE", "RENE", "LUPE", "JOSE", "ESME", "LETHE", "CADRE", "TILDE", "SIGNE", "POSSE", "LATTE", "ANIME", "DOLCE", "CROCE", "ADOBE", "OUTRE", "JESSE", "JAIME", "JAFFE", "BENGE", "RUNGE", "CHILE", "DESME", "CONDE", "URIBE", "LIBRE", "ANDRE", "HECATE", "PSYCHE", "DAPHNE", "PENSKE", "CLICHE", "RECIPE", "TAMALE", "SESAME", "SIMILE", "FINALE", "KARATE", "RENATE", "SHANTE", "OBERLE", "COYOTE", "KRESGE", "STONGE", "STANGE", "SWAYZE", "FUENTE", "SALOME", "URRIBE", "ECHIDNE", "ARIADNE", "MEINEKE", "PORSCHE", "ANEMONE", "EPITOME", "SYNCOPE", "SOUFFLE", "ATTACHE", "MACHETE", "KARAOKE", "BUKKAKE", "VICENTE", "ELLERBE", "VERSACE", "PENELOPE", "CALLIOPE", "CHIPOTLE", "ANTIGONE", "KAMIKAZE", "EURIDICE", "YOSEMITE", "FERRANTE", "HYPERBOLE", "GUACAMOLE", "XANTHIPPE", "SYNECDOCHE")):

            return True

        return False

    def encodeSilentInternalE(self):

        if (self.stringStart("OLE")  and  self.encodeESuffix(3))  or  (self.stringStart("BARE", "FIRE", "FORE", "GATE", "HAGE", "HAVE", "HAZE", "HOLE", "CAPE", "HUSE", "LACE", "LINE", "LIVE", "LOVE", "MORE", "MOSE", "MORE", "NICE", "RAKE", "ROBE", "ROSE", "SISE", "SIZE", "WARE", "WAKE", "WISE", "WINE")  and  self.encodeESuffix(4))  or  (self.stringStart("BLAKE", "BRAKE", "BRINE", "CARLE", "CLEVE", "DUNNE", "HEDGE", "HOUSE", "JEFFE", "LUNCE", "STOKE", "STONE", "THORE", "WEDGE", "WHITE")  and  self.encodeESuffix(5))  or  (self.stringStart("BRIDGE", "CHEESE")  and  self.encodeESuffix(6))  or  (self.stringAt(-5, "CHARLES")):
            return True

        return False

    def encodeESuffix(self, at):


        if self.idx == at-1  and  len(self.word) > at+1  and  (self.isVowelAt(-self.idx+at+1)  or  (self.stringAt(-self.idx+at, "ST", "SL")  and  len(self.word) > at+2)):








            if self.stringAtEnd(-self.idx+at, "T", "R", "TA", "TT", "NA", "NO", "NE", "RS", "RE", "LA", "AU", "RO", "RA", "TTE", "LIA", "NOW", "ROS", "RAS", "WOOD", "WATER", "WORTH"):
                return False

            return True

        return False





    def encodeEPronouncedExceptions(self):

        if (self.idx+1 == self.last_idx  and  (self.stringAtEnd(-3, "OCLES", "ACLES", "AKLES")  or  self.stringStart("INES", "LOPES", "ESTES", "GOMES", "NUNES", "ALVES", "ICKES", "INNES", "PERES", "WAGES", "NEVES", "BENES", "DONES", "CORTES", "CHAVES", "VALDES", "ROBLES", "TORRES", "FLORES", "BORGES", "NIEVES", "MONTES", "SOARES", "VALLES", "GEDDES", "ANDRES", "VIAJES", "CALLES", "FONTES", "HERMES", "ACEVES", "BATRES", "MATHES", "DELORES", "MORALES", "DOLORES", "ANGELES", "ROSALES", "MIRELES", "LINARES", "PERALES", "PAREDES", "BRIONES", "SANCHES", "CAZARES", "REVELES", "ESTEVES", "ALVARES", "MATTHES", "SOLARES", "CASARES", "CACERES", "STURGES", "RAMIRES", "FUNCHES", "BENITES", "FUENTES", "PUENTES", "TABARES", "HENTGES", "VALORES", "GONZALES", "MERCEDES", "FAGUNDES", "JOHANNES", "GONSALES", "BERMUDES", "CESPEDES", "BETANCES", "TERRONES", "DIOGENES", "CORRALES", "CABRALES", "MARTINES", "GRAJALES", "CERVANTES", "FERNANDES", "GONCALVES", "BENEVIDES", "CIFUENTES", "SIFUENTES", "SERVANTES", "HERNANDES", "BENAVIDES", "ARCHIMEDES", "CARRIZALES", "MAGALLANES")))  or  self.stringAt(-2, "FRED", "DGES", "DRED", "GNES")  or  self.stringAt(-5, "PROBLEM", "RESPLEN")  or  self.stringAt(-4, "REPLEN")  or  self.stringAt(-3, "SPLE"):

            return True

        return False


class Metaphone3(_Phonetic):
    """Metaphone 3.

    Based on the public OpenRefine 2.1.3 Metaphone 3 implementation by
    Lawrence Philips, via the BSD-licensed Go port by Douglas Clark.

    Parameters
    ----------
    max_length : int
        Maximum length of each returned metaphone key. Values less than 1 fall
        back to the public Metaphone 3 default of 8.
    encode_vowels : bool
        Whether to encode non-initial vowels.
    encode_exact : bool
        Whether to preserve more consonant distinctions.
    """

    def __init__(
        self,
        max_length: int = DEFAULT_MAX_LENGTH,
        encode_vowels: bool = False,
        encode_exact: bool = False,
    ) -> None:
        self._max_length = (
            max_length if max_length > 0 else DEFAULT_MAX_LENGTH
        )
        self._encode_vowels = encode_vowels
        self._encode_exact = encode_exact

    def _encode_pair(self, word: str) -> tuple[str, str]:
        encoder = Encoder(
            encode_vowels=self._encode_vowels,
            encode_exact=self._encode_exact,
            max_length=self._max_length,
        )
        return encoder.Encode(word)

    def encode(self, word: str) -> str:
        """Return the Metaphone 3 code for a word.

        Examples
        --------
        >>> pe = Metaphone3()
        >>> pe.encode('Smith')
        'SM0,XMT'
        >>> pe.encode('Schmidt')
        'XMT,'
        >>> Metaphone3(encode_vowels=True).encode('supernode')
        'SAPARNAT,'
        """
        primary, secondary = self._encode_pair(word)
        return primary + ',' + secondary

    def encode_alpha(self, word: str) -> str:
        """Return the alphabetic Metaphone 3 code for a word."""
        return self.encode(word)



