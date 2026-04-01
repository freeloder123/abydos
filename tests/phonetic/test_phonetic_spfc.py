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

"""abydos.tests.phonetic.test_phonetic_spfc.

This module contains unit tests for abydos.phonetic.SPFC
"""

import pytest

from abydos.phonetic import SPFC


pa = SPFC()

def test_spfc():
    """Test abydos.phonetic.SPFC."""
    assert pa.encode('') == ''

    # https://archive.org/stream/accessingindivid00moor#page/19/mode/1up
    assert pa.encode(('J', 'KUHNS')) == '16760'
    assert pa.encode(('G', 'ALTSHULER')) == '35797'
    assert pa.encode('J KUHNS') == '16760'
    assert pa.encode('G ALTSHULER') == '35797'
    assert pa.encode('J. KUHNS') == '16760'
    assert pa.encode('G. ALTSHULER') == '35797'
    assert pa.encode('J. Kuhns') == '16760'
    assert pa.encode('G. Altshuler') == '35797'
    assert pa.encode('T. Vines') == '16760'
    assert pa.encode('J. Butler') == '35779'
    assert pa.encode('J. Kuhns') != pa.encode('J. Kuntz')
    assert pa.encode('Jon Kuhns') == '16760'
    assert pa.encode('James Kuhns') == '16760'

    with pytest.raises(AttributeError):
        pa.encode(('J', 'A', 'Kuhns'))
    with pytest.raises(AttributeError):
        pa.encode('JKuhns')
    with pytest.raises(AttributeError):
        pa.encode(5)

    # etc. (for code coverage)
    assert pa.encode('James Goldstein') == '77795'
    assert pa.encode('James Hansen') == '57760'
    assert pa.encode('James Hester') == '57700'
    assert pa.encode('James Bardot') == '31745'
    assert pa.encode('James Windsor') == '27765'
    assert pa.encode('James Wenders') == '27760'
    assert pa.encode('James Ventor') == '17760'
    assert pa.encode('þ þ') == '00'

    # encode_alpha
    assert pa.encode_alpha('J. Kuhns') == 'CSGMS'
    assert pa.encode_alpha('G. Altshuler') == 'ARGEG'
    assert pa.encode_alpha('T. Vines') == 'CSGMS'
    assert pa.encode_alpha('James Ventor') == 'CZGMS'
