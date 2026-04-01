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

"""abydos.tests.phonetic.test_phonetic_phonetic_spanish.

This module contains unit tests for abydos.phonetic.PhoneticSpanish
"""

from abydos.phonetic import PhoneticSpanish


pa = PhoneticSpanish()

def test_phonetic_spanish():
    """Test abydos.phonetic.PhoneticSpanish."""
    # Base case
    assert pa.encode('') == ''

    # Examples given in
    assert pa.encode('Giraldo') == '8953'
    assert pa.encode('Jiraldo') == '8953'
    assert pa.encode('Halla') == '25'
    assert pa.encode('Haya') == '25'
    assert pa.encode('Cielo') == '45'
    assert pa.encode('Sielo') == '45'

    # Test to maximize coverage
    assert PhoneticSpanish(max_length=2).encode('Giraldo') == '89'

    # encode_alpha
    assert pa.encode_alpha('Giraldo') == 'GRLT'
    assert pa.encode_alpha('Jiraldo') == 'GRLT'
    assert pa.encode_alpha('Halla') == 'FL'
    assert pa.encode_alpha('Haya') == 'FL'
    assert pa.encode_alpha('Cielo') == 'SL'
    assert pa.encode_alpha('Sielo') == 'SL'
