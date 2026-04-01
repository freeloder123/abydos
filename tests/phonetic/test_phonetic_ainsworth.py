# Copyright 2019-2020 by Christopher C. Little.
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

"""abydos.tests.phonetic.test_phonetic_ainsworth.

This module contains unit tests for abydos.phonetic.Ainsworth
"""

from abydos.phonetic import Ainsworth


pa = Ainsworth()

def test_ainsworth_encode():
    """Test abydos.phonetic.Ainsworth.encode."""
    assert pa.encode('') == ''

    assert pa.encode('a') == 'ə'
    assert pa.encode('I') == 'ɑi'
    assert pa.encode('there') == 'ðɛə'
    assert pa.encode('winning') == 'wɪnnɪŋg'
    assert pa.encode('Daniel') == 'dænɑiɛl'
    assert pa.encode('row') == 'rɑʊ'
    assert pa.encode('dole') == 'doəl'
    assert pa.encode('retired') == 'rɛtɜɛd'
    assert pa.encode('Ainsworth') == 'ɛiɪnswɜrð'
    assert pa.encode('snap') == 'snæp'
    assert pa.encode('spinned') == 'spɪnnɛd'
    assert pa.encode('zoo') == 'zu'
    assert pa.encode('ooze') == 'uz'
    assert pa.encode('parallelogram') == 'pɑɔlɛlogræm'

    # Examples showing behavior when encountering unhandled characters
    assert pa.encode('Schluss') == 'sklus'
    assert pa.encode('Schlüsse') == 'sklsɛ'
    assert pa.encode('Schluß') == 'sklu'
