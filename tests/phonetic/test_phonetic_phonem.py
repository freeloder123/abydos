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

"""abydos.tests.phonetic.test_phonetic_phonem.

This module contains unit tests for abydos.phonetic.Phonem
"""

from abydos.phonetic import Phonem


pa = Phonem()

def test_phonem():
    """Test abydos.phonetic.Phonem."""
    assert pa.encode('') == ''

    # http://phonetik.phil-fak.uni-koeln.de/fileadmin/home/ritters/Allgemeine_Dateien/Martin_Wilz.pdf
    assert pa.encode('müller') == 'MYLR'
    assert pa.encode('schmidt') == 'CMYD'
    assert pa.encode('schneider') == 'CNAYDR'
    assert pa.encode('fischer') == 'VYCR'
    assert pa.encode('weber') == 'VBR'
    assert pa.encode('meyer') == 'MAYR'
    assert pa.encode('wagner') == 'VACNR'
    assert pa.encode('schulz') == 'CULC'
    assert pa.encode('becker') == 'BCR'
    assert pa.encode('hoffmann') == 'OVMAN'
    assert pa.encode('schäfer') == 'CVR'

    # http://cpansearch.perl.org/src/MAROS/Text-Phonetic-2.05/t/008_phonem.t
    assert pa.encode('mair') == 'MAYR'
    assert pa.encode('bäker') == 'BCR'
    assert pa.encode('schaeffer') == 'CVR'
    assert pa.encode('computer') == 'COMBUDR'
    assert pa.encode('pfeifer') == 'VAYVR'
    assert pa.encode('pfeiffer') == 'VAYVR'
