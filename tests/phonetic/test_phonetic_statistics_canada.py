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

"""abydos.tests.phonetic.test_phonetic_statistics_canada.

This module contains unit tests for abydos.phonetic.StatisticsCanada
"""

from abydos.phonetic import StatisticsCanada


pa = StatisticsCanada()

def test_statistics_canada():
    """Test abydos.phonetic.StatisticsCanada."""
    assert pa.encode('') == ''

    # https://naldc.nal.usda.gov/download/27833/PDF
    assert pa.encode('Daves') == 'DVS'
    assert pa.encode('Davies') == 'DVS'
    assert pa.encode('Devese') == 'DVS'
    assert pa.encode('Devies') == 'DVS'
    assert pa.encode('Devos') == 'DVS'

    assert pa.encode('Smathers') == 'SMTH'
    assert pa.encode('Smithart') == 'SMTH'
    assert pa.encode('Smithbower') == 'SMTH'
    assert pa.encode('Smitherman') == 'SMTH'
    assert pa.encode('Smithey') == 'SMTH'
    assert pa.encode('Smithgall') == 'SMTH'
    assert pa.encode('Smithingall') == 'SMTH'
    assert pa.encode('Smithmyer') == 'SMTH'
    assert pa.encode('Smithpeter') == 'SMTH'
    assert pa.encode('Smithson') == 'SMTH'
    assert pa.encode('Smithy') == 'SMTH'
    assert pa.encode('Smotherman') == 'SMTH'
    assert pa.encode('Smothers') == 'SMTH'
    assert pa.encode('Smyth') == 'SMTH'

    # Additional tests from @Yomguithereal's talisman
    # https://github.com/Yomguithereal/talisman/blob/master/test/phonetics/statcan.js
    assert pa.encode('Guillaume') == 'GLM'
    assert pa.encode('Arlène') == 'ARLN'
    assert pa.encode('Lüdenscheidt') == 'LDNS'
