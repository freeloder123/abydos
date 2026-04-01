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

"""abydos.tests.stemmer.test_stemmer_caumanns.

This module contains unit tests for abydos.stemmer.Caumanns
"""


from abydos.stemmer import Caumanns


stmr = Caumanns()


def test_caumanns():
    """Test abydos.stemmer.Caumanns."""
    # base case
    assert stmr.stem('') == ''

    # tests from Caumanns' description of the algorithm
    assert stmr.stem('singt') == 'sing'
    assert stmr.stem('singen') == 'sing'
    assert stmr.stem('beliebt') == 'belieb'
    assert stmr.stem('beliebtester') == 'belieb'
    assert stmr.stem('stören') == 'stor'
    assert stmr.stem('stöhnen') == 'stoh'
    assert stmr.stem('Kuß') == 'kuss'
    assert stmr.stem('Küsse') == 'kuss'
    assert stmr.stem('Verlierer') == 'verlier'
    assert stmr.stem('Verlies') == 'verlie'
    assert stmr.stem('Maus') == 'mau'
    assert stmr.stem('Mauer') == 'mau'
    assert stmr.stem('Störsender') == 'stor'

    # additional tests to achieve full coverage
    assert stmr.stem('Müllerinnen') == 'mullerin'
    assert stmr.stem('Matrix') == 'matrix'
    assert stmr.stem('Matrizen') == 'matrix'

def test_caumanns_lucene():
    """Test abydos.stemmer.Caumanns (Lucene tests).

    Based on tests from
    https://svn.apache.org/repos/asf/lucene.net/trunk/test/contrib/Analyzers/De/data.txt
    This is presumably Apache-licensed.
    """
    # German special characters are replaced:
    assert stmr.stem('häufig') == 'haufig'
    assert stmr.stem('üor') == 'uor'
    assert stmr.stem('björk') == 'bjork'

    # here the stemmer works okay, it maps related words to the same stem:
    assert stmr.stem('abschließen') == 'abschliess'
    assert stmr.stem('abschließender') == 'abschliess'
    assert stmr.stem('abschließendes') == 'abschliess'
    assert stmr.stem('abschließenden') == 'abschliess'

    assert stmr.stem('Tisch') == 'tisch'
    assert stmr.stem('Tische') == 'tisch'
    assert stmr.stem('Tischen') == 'tisch'
    assert stmr.stem('geheimtür') == 'geheimtur'

    assert stmr.stem('Haus') == 'hau'
    assert stmr.stem('Hauses') == 'hau'
    assert stmr.stem('Häuser') == 'hau'
    assert stmr.stem('Häusern') == 'hau'
    # here's a case where overstemming occurs, i.e. a word is
    # mapped to the same stem as unrelated words:
    assert stmr.stem('hauen') == 'hau'

    # here's a case where understemming occurs, i.e. two related words
    # are not mapped to the same stem. This is the case with basically
    # all irregular forms:
    assert stmr.stem('Drama') == 'drama'
    assert stmr.stem('Dramen') == 'dram'

    # replace "ß" with 'ss':
    assert stmr.stem('Ausmaß') == 'ausmass'

    # fake words to test if suffixes are cut off:
    assert stmr.stem('xxxxxe') == 'xxxxx'
    assert stmr.stem('xxxxxs') == 'xxxxx'
    assert stmr.stem('xxxxxn') == 'xxxxx'
    assert stmr.stem('xxxxxt') == 'xxxxx'
    assert stmr.stem('xxxxxem') == 'xxxxx'
    assert stmr.stem('xxxxxer') == 'xxxxx'
    assert stmr.stem('xxxxxnd') == 'xxxxx'
    # the suffixes are also removed when combined:
    assert stmr.stem('xxxxxetende') == 'xxxxx'

    # words that are shorter than four charcters are not changed:
    assert stmr.stem('xxe') == 'xxe'
    # -em and -er are not removed from words shorter than five characters:
    assert stmr.stem('xxem') == 'xxem'
    assert stmr.stem('xxer') == 'xxer'
    # -nd is not removed from words shorter than six characters:
    assert stmr.stem('xxxnd') == 'xxxnd'
