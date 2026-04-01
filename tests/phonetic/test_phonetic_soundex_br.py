# Copyright 2018-2020 by Christopher C. Little.
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

"""abydos.tests.phonetic.test_phonetic_soundex_br.

This module contains unit tests for abydos.phonetic.SoundexBR
"""

from abydos.phonetic import SoundexBR


pa = SoundexBR()

def test_soundex_br():
    """Test abydos.phonetic.SoundexBR."""
    # Base case
    assert pa.encode('') == '0000'

    # Examples given at https://github.com/danielmarcelino/SoundexBR
    assert pa.encode('Ana Karolina Kuhnen') == 'A526'
    assert pa.encode('Ana Carolina Kuhnen') == 'A526'
    assert pa.encode('Ana Karolina') == 'A526'
    assert pa.encode('João Souza') == 'J220'
    assert pa.encode('Dilma Vana Rousseff') == 'D451'
    assert pa.encode('Dilma Rousef') == 'D456'
    assert pa.encode('Aécio Neves') == 'A251'
    assert pa.encode('Aecio Neves') == 'A251'
    assert pa.encode('HILBERT') == 'I416'
    assert pa.encode('Heilbronn') == 'E416'
    assert pa.encode('Gauss') == 'G200'
    assert pa.encode('Kant') == 'C530'

    # Tests to complete coverage
    assert pa.encode('Wasser') == 'V260'
    assert pa.encode('Cici') == 'S200'
    assert pa.encode('Gerard') == 'J663'
    assert pa.encode('Yglesias') == 'I242'
    assert SoundexBR(zero_pad=False).encode('Cici') == 'S2'

    # encode_alpha
    assert pa.encode_alpha('Aecio Neves') == 'AKNP'
    assert pa.encode_alpha('HILBERT') == 'ILPR'
    assert pa.encode_alpha('Heilbronn') == 'ELPR'
    assert pa.encode_alpha('Gauss') == 'GK'
