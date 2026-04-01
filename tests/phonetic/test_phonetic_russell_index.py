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

"""abydos.tests.phonetic.test_phonetic_russell_index.

This module contains unit tests for abydos.phonetic.RussellIndex
"""

from abydos.phonetic import RussellIndex


pa = RussellIndex()

def test_russel_index():
    """Test abydos.phonetic.RussellIndex."""
    assert pa.encode('') == ''
    assert pa.encode('H') == ''
    assert pa.encode('Hoppa') == '12'
    assert pa.encode('Hopley') == '125'
    assert pa.encode('Highfield') == '1254'
    assert pa.encode('Wright') == '814'
    assert pa.encode('Carter') == '31848'
    assert pa.encode('Hopf') == '12'
    assert pa.encode('Hay') == '1'
    assert pa.encode('Haas') == '1'
    assert pa.encode('Meyers') == '618'
    assert pa.encode('Myers') == '618'
    assert pa.encode('Meyer') == '618'
    assert pa.encode('Myer') == '618'
    assert pa.encode('Mack') == '613'
    assert pa.encode('Knack') == '3713'

def test_russel_index_alpha():
    """Test abydos.phonetic.RussellIndex.encode_alpha."""
    assert pa.encode_alpha('') == ''
    assert pa.encode_alpha('H') == ''
    assert pa.encode_alpha('Hoppa') == 'AB'
    assert pa.encode_alpha('Hopley') == 'ABL'
    assert pa.encode_alpha('Highfield') == 'ABLD'
    assert pa.encode_alpha('Wright') == 'RAD'
    assert pa.encode_alpha('Carter') == 'CARDR'
    assert pa.encode_alpha('Hopf') == 'AB'
    assert pa.encode_alpha('Hay') == 'A'
    assert pa.encode_alpha('Haas') == 'A'
    assert pa.encode_alpha('Meyers') == 'MAR'
    assert pa.encode_alpha('Myers') == 'MAR'
    assert pa.encode_alpha('Meyer') == 'MAR'
    assert pa.encode_alpha('Myer') == 'MAR'
    assert pa.encode_alpha('Mack') == 'MAC'
    assert pa.encode_alpha('Knack') == 'CNAC'
