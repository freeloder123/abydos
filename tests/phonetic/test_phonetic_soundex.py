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

"""abydos.tests.phonetic.test_phonetic_soundex.

This module contains unit tests for abydos.phonetic.Soundex
"""

import pytest

from abydos.phonetic import Soundex


pa = Soundex()

def test_soundex():
    """Test abydos.phonetic.Soundex."""
    assert pa.encode('') == '0000'

    # https://archive.org/stream/accessingindivid00moor#page/14/mode/2up
    assert pa.encode('Euler') == 'E460'
    assert pa.encode('Gauss') == 'G200'
    assert pa.encode('Hilbert') == 'H416'
    assert pa.encode('Knuth') == 'K530'
    assert pa.encode('Lloyd') == 'L300'
    assert pa.encode('Lukasieicz') == 'L222'
    assert pa.encode('Ellery') == 'E460'
    assert pa.encode('Ghosh') == 'G200'
    assert pa.encode('Heilbronn') == 'H416'
    assert pa.encode('Kant') == 'K530'
    assert pa.encode('Ladd') == 'L300'
    assert pa.encode('Lissajous') == 'L222'
    assert pa.encode('Rogers') == 'R262'
    assert pa.encode('Rodgers') == 'R326'
    assert pa.encode('Rogers') != pa.encode('Rodgers')
    assert pa.encode('Sinclair') != pa.encode('St. Clair')
    assert pa.encode('Tchebysheff') != pa.encode('Chebyshev')

    # http://creativyst.com/Doc/Articles/SoundEx1/SoundEx1.htm#Related
    assert pa.encode('Htacky') == 'H320'
    assert pa.encode('Atacky') == 'A320'
    assert pa.encode('Schmit') == 'S530'
    assert pa.encode('Schneider') == 'S536'
    assert pa.encode('Pfister') == 'P236'
    assert pa.encode('Ashcroft') == 'A261'
    assert pa.encode('Asicroft') == 'A226'

    # https://en.wikipedia.org/wiki/Soundex
    assert pa.encode('Robert') == 'R163'
    assert pa.encode('Rupert') == 'R163'
    assert pa.encode('Rubin') == 'R150'
    assert pa.encode('Tymczak') == 'T522'

    # https://en.wikipedia.org/wiki/Daitch%E2%80%93Mokotoff_Soundex
    assert pa.encode('Peters') == 'P362'
    assert pa.encode('Peterson') == 'P362'
    assert pa.encode('Moskowitz') == 'M232'
    assert pa.encode('Moskovitz') == 'M213'
    assert pa.encode('Auerbach') == 'A612'
    assert pa.encode('Uhrbach') == 'U612'
    assert pa.encode('Jackson') == 'J250'
    assert pa.encode('Jackson-Jackson') == 'J252'

    # max_length tests
    assert Soundex(10).encode('Lincoln') == 'L524500000'
    assert Soundex(5).encode('Lincoln') == 'L5245'
    assert Soundex(6).encode('Christopher') == 'C62316'

    # max_length bounds tests
    assert (
        Soundex(max_length=-1).encode('Niall')
        == 'N4000000000000000000000000000000000000000000000000'
        + '00000000000000'
    )
    assert Soundex(max_length=0).encode('Niall') == 'N400'

    # reverse tests
    assert Soundex(reverse=True).encode('Rubin') == 'N160'
    assert Soundex(reverse=True).encode('Llyod') == 'D400'
    assert Soundex(reverse=True).encode('Lincoln') == 'N425'
    assert Soundex(reverse=True).encode('Knuth') == 'H352'

    # zero_pad tests
    assert Soundex(max_length=-1, zero_pad=False).encode('Niall') == 'N4'
    assert Soundex(max_length=0, zero_pad=False).encode('Niall') == 'N4'
    assert Soundex(max_length=0, zero_pad=True).encode('Niall') == 'N400'
    assert Soundex(max_length=4, zero_pad=False).encode('') == '0'
    assert Soundex(max_length=4, zero_pad=True).encode('') == '0000'

    # encode_alpha
    assert pa.encode_alpha('Euler') == 'ELR'
    assert pa.encode_alpha('Gauss') == 'GK'
    assert pa.encode_alpha('Hilbert') == 'HLPR'
    assert pa.encode_alpha('Knuth') == 'KNT'

def test_soundex_special():
    """Test abydos.phonetic.Soundex (special 1880-1910 variant method)."""
    pa_special = Soundex(var='special')
    assert pa_special.encode('Ashcroft') == 'A226'
    assert pa_special.encode('Asicroft') == 'A226'
    assert pa_special.encode('AsWcroft') == 'A226'
    assert pa_special.encode('Rupert') == 'R163'
    assert pa_special.encode('Rubin') == 'R150'

def test_soundex_census():
    """Test abydos.phonetic.Soundex(Census variant method)."""
    pa_census = Soundex(var='Census')
    assert pa_census.encode('Vandeusen') == 'V532,D250'
    assert pa_census.encode('van Deusen') == 'V532,D250'
    assert pa_census.encode('McDonald') == 'M235'
    assert pa_census.encode('la Cruz') == 'L262,C620'
    assert pa_census.encode('vanDamme') == 'V535,D500'


def test_soundex_validation():
    """Test input validation for Soundex."""
    pa = Soundex()
    with pytest.raises(TypeError):
        pa.encode(123)
    with pytest.raises(TypeError):
        pa.encode(None)
    with pytest.raises(TypeError):
        pa.encode(['Smith'])
    with pytest.raises(ValueError):
        Soundex(var='invalid')
    with pytest.raises(TypeError):
        Soundex(max_length='4')
    with pytest.raises(TypeError):
        Soundex(max_length=4.0)
