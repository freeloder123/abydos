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

"""abydos.tests.stemmer.test_stemmer_clef_swedish.

This module contains unit tests for abydos.stemmer.CLEFSwedish
"""


from abydos.stemmer import CLEFSwedish


stmr = CLEFSwedish()


def test_clef_swedish():
    """Test abydos.stemmer.CLEFSwedish."""
    # base case
    assert stmr.stem('') == ''

    # unstemmed
    assert stmr.stem('konung') == 'konung'

    # len <= 3
    assert stmr.stem('km') == 'km'
    assert stmr.stem('ja') == 'ja'
    assert stmr.stem('de') == 'de'
    assert stmr.stem('in') == 'in'
    assert stmr.stem('a') == 'a'
    assert stmr.stem('mer') == 'mer'
    assert stmr.stem('s') == 's'
    assert stmr.stem('e') == 'e'
    assert stmr.stem('oss') == 'oss'
    assert stmr.stem('hos') == 'hos'

    # genitive
    assert stmr.stem('svenskars') == 'svensk'
    assert stmr.stem('stadens') == 'stad'
    assert stmr.stem('kommuns') == 'kommu'
    assert stmr.stem('aftonbladets') == 'aftonblad'

    # len > 7
    assert stmr.stem('fängelser') == 'fäng'
    assert stmr.stem('möjligheten') == 'möjlig'

    # len > 6
    assert stmr.stem('svenskar') == 'svensk'
    assert stmr.stem('myndigheterna') == 'myndighet'
    assert stmr.stem('avgörande') == 'avgör'
    assert stmr.stem('fängelse') == 'fäng'
    assert stmr.stem('viktigaste') == 'viktig'
    assert stmr.stem('kvinnorna') == 'kvinn'
    assert stmr.stem('åklagaren') == 'åklag'

    # len > 5
    assert stmr.stem('tidigare') == 'tidig'
    assert stmr.stem('senast') == 'sen'
    assert stmr.stem('möjlighet') == 'möjlig'

    # len > 4
    assert stmr.stem('svenskar') == 'svensk'
    assert stmr.stem('skriver') == 'skriv'
    assert stmr.stem('människor') == 'människ'
    assert stmr.stem('staden') == 'stad'
    assert stmr.stem('kunnat') == 'kunn'
    assert stmr.stem('samarbete') == 'samarbe'
    assert stmr.stem('aftonbladet') == 'aftonblad'

    # len > 3
    assert stmr.stem('allt') == 'all'
    assert stmr.stem('vilka') == 'vilk'
    assert stmr.stem('länge') == 'läng'
    assert stmr.stem('kommun') == 'kommu'
