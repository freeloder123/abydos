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

"""abydos.tests.phonetic.test_phonetic_pshp_soundex_first.

This module contains unit tests for abydos.phonetic.PSHPSoundexFirst
"""

from abydos.phonetic import PSHPSoundexFirst


pa = PSHPSoundexFirst()

pa_german = PSHPSoundexFirst(german=True)

pa_unl = PSHPSoundexFirst(max_length=-1)

def test_pshp_soundex_first():
    """Test abydos.phonetic.PSHPSoundexFirst."""
    # Base case
    assert pa.encode('') == '0000'

    # Examples given in defining paper (Hershberg, et al. 1976)
    assert pa.encode('JAMES') == 'J700'
    assert pa.encode('JOHN') == 'J500'
    assert pa.encode('PAT') == 'P700'
    assert pa.encode('PETER') == 'P300'

    # Additions for coverage
    assert pa.encode('Giles') == 'J400'
    assert pa.encode('Cy') == 'S000'
    assert pa.encode('Chris') == 'K500'
    assert pa.encode('Caleb') == 'K400'
    assert pa.encode('Knabe') == 'N100'
    assert pa.encode('Phil') == 'F400'
    assert pa.encode('Wieland') == 'V400'
    assert pa_german.encode('Wayne') == 'V500'
    assert pa_unl.encode('Christopher') == 'K5'
    assert pa_unl.encode('Asdaananndsjsjasd') == 'A23553223'
    assert pa.encode('Asdaananndsjsjasd') == 'A235'

    # encode_alpha
    assert pa.encode_alpha('JAMES') == 'JN'
    assert pa.encode_alpha('JOHN') == 'JN'
    assert pa.encode_alpha('PAT') == 'PT'
    assert pa.encode_alpha('PETER') == 'PT'
    assert pa.encode_alpha('Knabe') == 'NP'
    assert pa.encode_alpha('Phil') == 'FL'
    assert pa.encode_alpha('Wieland') == 'VL'
