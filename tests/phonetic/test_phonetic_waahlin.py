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

"""abydos.tests.phonetic.test_phonetic_waahlin.

This module contains unit tests for abydos.phonetic.Waahlin
"""

from abydos.phonetic import Soundex, Waahlin


pa = Waahlin()

pa_sdx = Waahlin(Soundex())

def test_waahlin():
    """Test abydos.phonetic.Waahlin."""
    assert pa.encode('') == ''

    assert pa.encode('kjol') == '+OL'
    assert pa.encode('stråken') == 'STRÅ+EN'
    assert pa.encode('skytten') == '*YTTEN'
    assert pa.encode('ljuden') == 'JUDEN'
    assert pa.encode('högre') == 'HÖGRE'
    assert pa.encode('först') == 'FÖRST'
    assert pa.encode('hval') == 'VAL'
    assert pa.encode('hrothgar') == 'ROTHGAR'
    assert pa.encode('denna') == 'DENNA'
    assert pa.encode('djur') == 'JUR'
    assert pa.encode('hjärta') == 'JERTA'
    assert pa.encode('STIEN') == '*EN'
    assert pa.encode('SKJERN') == '*ERN'
    assert pa.encode('HIELPA') == 'JELPA'
    assert pa.encode('CEILA') == 'SEILA'
    assert pa.encode('GELD') == 'JELD'
    assert pa.encode('IERN') == 'JERN'

    # encode_alpha
    assert pa.encode_alpha('kjol') == 'ÇOL'
    assert pa.encode_alpha('stråken') == 'STRÅÇEN'
    assert pa.encode_alpha('skytten') == 'ŠYTTEN'
    assert pa.encode_alpha('ljuden') == 'JUDEN'

def test_waahlin_soundex():
    """Test abydos.phonetic.Waahlin with Soundex."""
    assert pa_sdx.encode('') == ''

    assert pa_sdx.encode('kjol') == '+O400'
    assert pa_sdx.encode('stråken') == 'ST625'
    assert pa_sdx.encode('skytten') == '*Y350'
    assert pa_sdx.encode('ljuden') == 'JU350'
    assert pa_sdx.encode('högre') == 'HO260'
    assert pa_sdx.encode('först') == 'FO623'
    assert pa_sdx.encode('hval') == 'VA400'
    assert pa_sdx.encode('hrothgar') == 'RO326'
    assert pa_sdx.encode('denna') == 'DE500'
    assert pa_sdx.encode('djur') == 'JU600'
    assert pa_sdx.encode('hjärta') == 'JA630'
