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

"""abydos.tests.phonetic.test_phonetic_pshp_soundex_last.

This module contains unit tests for abydos.phonetic.PSHPSoundexLast
"""

from abydos.phonetic import PSHPSoundexLast


pa = PSHPSoundexLast()

pa_german = PSHPSoundexLast(german=True)

pa_unl = PSHPSoundexLast(max_length=-1)

def test_pshp_soundex_last():
    """Test abydos.phonetic.PSHPSoundexLast."""
    # Base case
    assert pa.encode('') == '0000'

    assert pa.encode('JAMES') == 'J500'
    assert pa.encode('JOHN') == 'J500'
    assert pa.encode('PAT') == 'P300'
    assert pa.encode('PETER') == 'P350'

    assert pa.encode('Smith') == 'S530'
    assert pa.encode('van Damme') == 'D500'
    assert pa.encode('MacNeil') == 'M400'
    assert pa.encode('McNeil') == 'M400'
    assert pa.encode('Edwards') == 'A353'
    assert pa.encode('Gin') == 'J500'
    assert pa.encode('Cillian') == 'S450'
    assert pa.encode('Christopher') == 'K523'
    assert pa.encode('Carme') == 'K500'
    assert pa.encode('Knight') == 'N230'
    assert pa.encode('Phillip') == 'F410'
    assert pa.encode('Wein') == 'V500'
    assert pa_german.encode('Wagner') == 'V255'
    assert pa.encode('Pence') == 'P500'
    assert pa.encode('Less') == 'L000'
    assert pa.encode('Simpson') == 'S525'
    assert pa.encode('Samson') == 'S250'
    assert pa.encode('Lang') == 'L500'
    assert pa.encode('Hagan') == 'H500'
    assert pa_german.encode('Cartes') == 'K500'
    assert pa_german.encode('Kats') == 'K000'
    assert pa_german.encode('Schultze') == 'S400'
    assert pa_german.encode('Alze') == 'A400'
    assert pa_german.encode('Galz') == 'G400'
    assert pa_german.encode('Alte') == 'A400'
    assert pa_unl.encode('Alte') == 'A43'
    assert pa_unl.encode('Altemaier') == 'A4355'

    # encode_alpha
    assert pa.encode_alpha('Simpson') == 'SNKN'
    assert pa.encode_alpha('Samson') == 'SKN'
    assert pa.encode_alpha('Lang') == 'LN'
    assert pa.encode_alpha('Hagan') == 'HN'
    assert pa_german.encode_alpha('Cartes') == 'KN'
    assert pa_german.encode_alpha('Kats') == 'K'
