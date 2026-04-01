# Copyright 2014-2020 by Christopher C. Little.
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

"""abydos.tests.phonetic.test_phonetic_phonet.

This module contains unit tests for abydos.phonetic.Phonet
"""

from abydos.phonetic import Phonet

from .. import ALLOW_RANDOM, _corpus_file, _one_in


pa = Phonet()

pa_1 = Phonet(1)

pa_2 = Phonet(2)

pa_1none = Phonet(1, 'none')

pa_2none = Phonet(2, 'none')

def test_phonet_german():
    """Test abydos.phonetic.Phonet (German)."""
    assert pa.encode('') == ''

    # https://code.google.com/p/phonet4java/source/browse/trunk/src/test/java/com/googlecode/phonet4java/Phonet1Test.java
    assert pa_1.encode('') == ''
    assert pa_1.encode('Zedlitz') == 'ZETLIZ'
    assert pa_1.encode('Bremerhaven') == 'BREMAHAFN'
    assert pa_1.encode('Hamburger Hafen') == 'HAMBURGA HAFN'
    assert pa_1.encode('Jesper') == 'IESPA'
    assert pa_1.encode('elisabeth') == 'ELISABET'
    assert pa_1.encode('elisabet') == 'ELISABET'
    assert pa_1.encode('Ziegler') == 'ZIKLA'
    assert pa_1.encode('Scherer') == 'SHERA'
    assert pa_1.encode('Bartels') == 'BARTLS'
    assert pa_1.encode('Jansen') == 'IANSN'
    assert pa_1.encode('Sievers') == 'SIWAS'
    assert pa_1.encode('Michels') == 'MICHLS'
    assert pa_1.encode('Ewers') == 'EWERS'
    assert pa_1.encode('Evers') == 'EWERS'
    assert pa_1.encode('Wessels') == 'WESLS'
    assert pa_1.encode('Gottschalk') == 'GOSHALK'
    assert pa_1.encode('Brückmann') == 'BRÜKMAN'
    assert pa_1.encode('Blechschmidt') == 'BLECHSHMIT'
    assert pa_1.encode('Kolodziej') == 'KOLOTZI'
    assert pa_1.encode('Krauße') == 'KRAUSE'
    assert pa_1.encode('Cachel') == 'KESHL'

    assert pa_2.encode('') == ''
    assert pa_2.encode('Zedlitz') == 'ZETLIZ'
    assert pa_2.encode('Bremerhaven') == 'BRENAFN'
    assert pa_2.encode('Schönberg') == 'ZÖNBAK'
    assert pa_2.encode('Hamburger Hafen') == 'ANBURKA AFN'
    assert pa_2.encode('Ziegler') == 'ZIKLA'
    assert pa_2.encode('Scherer') == 'ZERA'
    assert pa_2.encode('Jansen') == 'IANZN'
    assert pa_2.encode('Eberhardt') == 'EBART'
    assert pa_2.encode('Gottschalk') == 'KUZALK'
    assert pa_2.encode('Brückmann') == 'BRIKNAN'
    assert pa_2.encode('Blechschmidt') == 'BLEKZNIT'
    assert pa_2.encode('Kolodziej') == 'KULUTZI'
    assert pa_2.encode('Krauße') == 'KRAUZE'

    # etc. (for code coverage)
    assert pa_1.encode('Jesper') == 'IESPA'
    assert pa_1.encode('Glacéhandschuh') == 'GLAZANSHU'
    assert pa_1.encode('Blechschmidt') == 'BLECHSHMIT'
    assert pa_1.encode('Burgdorf') == 'BURKDORF'
    assert pa_1.encode('Holzschuh') == 'HOLSHU'
    assert pa_1.encode('Aachen') == 'ACHN'
    assert pa_1.encode('Abendspaziergang') == 'ABENTSPAZIRGANK'

def test_phonet_nolang():
    """Test abydos.phonetic.Phonet (no language)."""
    assert Phonet(lang='none').encode('') == ''

    # https://code.google.com/p/phonet4java/source/browse/trunk/src/test/java/com/googlecode/phonet4java/Phonet1Test.java
    assert pa_1none.encode('') == ''
    assert pa_1none.encode('Zedlitz') == 'ZEDLITZ'
    assert pa_1none.encode('Bremerhaven') == 'BREMERHAVEN'
    assert pa_2none.encode('Schönberg') == 'SCHOENBERG'
    assert pa_1none.encode('Brückmann') == 'BRUECKMAN'
    assert pa_1none.encode('Krauße') == 'KRAUSE'

    assert pa_2none.encode('') == ''
    assert pa_2none.encode('Zedlitz') == 'ZEDLITZ'
    assert pa_2none.encode('Bremerhaven') == 'BREMERHAVEN'
    assert pa_2none.encode('Schönberg') == 'SCHOENBERG'
    assert pa_2none.encode('Brückmann') == 'BRUECKMAN'
    assert pa_2none.encode('Krauße') == 'KRAUSE'

def test_phonet_nachnamen():
    """Test abydos.phonetic.Phonet (Nachnamen set)."""
    if not ALLOW_RANDOM:
        return
    with open(
        _corpus_file('nachnamen.csv'), encoding='utf-8'
    ) as nachnamen_testset:
        for nn_line in nachnamen_testset:
            if nn_line[0] != '#':
                nn_line = nn_line.strip().split(',')
                # This test set is very large (~10000 entries)
                # so let's just randomly select about 100 for testing
                if len(nn_line) >= 3 and _one_in(100):
                    (term, ph1, ph2) = nn_line
                    assert pa_1.encode(term) == ph1
                    assert pa_2.encode(term) == ph2

def test_phonet_ngerman():
    """Test abydos.phonetic.Phonet (ngerman set)."""
    if not ALLOW_RANDOM:
        return
    with open(
        _corpus_file('ngerman.csv'), encoding='utf-8'
    ) as ngerman_testset:
        for ng_line in ngerman_testset:
            if ng_line[0] != '#':
                ng_line = ng_line.strip().split(',')
                # This test set is very large (~3000000 entries)
                # so let's just randomly select about 30 for testing
                if len(ng_line) >= 3 and _one_in(10000):
                    (term, ph1, ph2) = ng_line
                    assert pa_1.encode(term) == ph1
                    assert pa_2.encode(term) == ph2
