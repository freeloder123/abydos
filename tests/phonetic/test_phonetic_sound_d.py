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

"""abydos.tests.phonetic.test_phonetic_sound_d.

This module contains unit tests for abydos.phonetic.SoundD
"""

from abydos.phonetic import SoundD


pa = SoundD()

def test_sound_d():
    """Test abydos.phonetic.SoundD."""
    # Base cases
    assert pa.encode('') == '0000'
    assert SoundD(max_length=6).encode('') == '000000'

    assert pa.encode('knight') == '5300'
    assert pa.encode('accept') == '2130'
    assert pa.encode('pneuma') == '5500'
    assert pa.encode('ax') == '2000'
    assert pa.encode('wherever') == '6160'
    assert pa.encode('pox') == '1200'
    assert pa.encode('anywhere') == '5600'
    assert pa.encode('adenosine') == '3525'
    assert pa.encode('judge') == '2200'
    assert pa.encode('rough') == '6000'
    assert pa.encode('x-ray') == '2600'
    assert SoundD(max_length=-1).encode('acetylcholine') == '234245'
    assert SoundD(max_length=-1).encode('rough') == '6'

    # encode_alpha
    assert pa.encode_alpha('pox') == 'PK'
    assert pa.encode_alpha('anywhere') == 'NR'
    assert pa.encode_alpha('adenosine') == 'TNKN'
    assert pa.encode_alpha('judge') == 'KK'
