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

"""abydos.tests.phonetic.test_phonetic_lein.

This module contains unit tests for abydos.phonetic.LEIN
"""

from abydos.phonetic import LEIN


pa = LEIN()

pa_n0 = LEIN(zero_pad=False)

def test_lein():
    """Test abydos.phonetic.LEIN."""
    assert pa.encode('') == '0000'

    # https://naldc.nal.usda.gov/download/27833/PDF
    assert pa.encode('Dubose') == 'D450'
    assert pa.encode('Dubs') == 'D450'
    assert pa.encode('Dubbs') == 'D450'
    assert pa.encode('Doviak') == 'D450'
    assert pa.encode('Dubke') == 'D450'
    assert pa.encode('Dubus') == 'D450'
    assert pa.encode('Dubois') == 'D450'
    assert pa.encode('Duboise') == 'D450'
    assert pa.encode('Doubek') == 'D450'
    assert pa.encode('Defigh') == 'D450'
    assert pa.encode('Defazio') == 'D450'
    assert pa.encode('Debaca') == 'D450'
    assert pa.encode('Dabbs') == 'D450'
    assert pa.encode('Davies') == 'D450'
    assert pa.encode('Dubukey') == 'D450'
    assert pa.encode('Debus') == 'D450'
    assert pa.encode('Debose') == 'D450'
    assert pa.encode('Daves') == 'D450'
    assert pa.encode('Dipiazza') == 'D450'
    assert pa.encode('Dobbs') == 'D450'
    assert pa.encode('Dobak') == 'D450'
    assert pa.encode('Dobis') == 'D450'
    assert pa.encode('Dobish') == 'D450'
    assert pa.encode('Doepke') == 'D450'
    assert pa.encode('Divish') == 'D450'
    assert pa.encode('Dobosh') == 'D450'
    assert pa.encode('Dupois') == 'D450'
    assert pa.encode('Dufek') == 'D450'
    assert pa.encode('Duffek') == 'D450'
    assert pa.encode('Dupuis') == 'D450'
    assert pa.encode('Dupas') == 'D450'
    assert pa.encode('Devese') == 'D450'
    assert pa.encode('Devos') == 'D450'
    assert pa.encode('Deveaux') == 'D450'
    assert pa.encode('Devies') == 'D450'

    assert pa.encode('Sand') == 'S210'
    assert pa.encode('Sandau') == 'S210'
    assert pa.encode('Sande') == 'S210'
    assert pa.encode('Sandia') == 'S210'
    assert pa.encode('Sando') == 'S210'
    assert pa.encode('Sandoe') == 'S210'
    assert pa.encode('Sandy') == 'S210'
    assert pa.encode('Santee') == 'S210'
    assert pa.encode('Santi') == 'S210'
    assert pa.encode('Santo') == 'S210'
    assert pa.encode('Send') == 'S210'
    assert pa.encode('Sennet') == 'S210'
    assert pa.encode('Shemoit') == 'S210'
    assert pa.encode('Shenot') == 'S210'
    assert pa.encode('Shumate') == 'S210'
    assert pa.encode('Simmet') == 'S210'
    assert pa.encode('Simot') == 'S210'
    assert pa.encode('Sineath') == 'S210'
    assert pa.encode('Sinnott') == 'S210'
    assert pa.encode('Sintay') == 'S210'
    assert pa.encode('Smead') == 'S210'
    assert pa.encode('Smeda') == 'S210'
    assert pa.encode('Smit') == 'S210'

    # Additional tests from @Yomguithereal's talisman
    # https://github.com/Yomguithereal/talisman/blob/master/test/phonetics/lein.js
    assert pa.encode('Guillaume') == 'G320'
    assert pa.encode('Arlène') == 'A332'
    assert pa.encode('Lüdenscheidt') == 'L125'

    # Coverage
    assert pa_n0.encode('Lüdenscheidt') == 'L125'
    assert pa_n0.encode('Smith') == 'S21'

    # encode_alpha
    assert pa.encode_alpha('Deveaux') == 'DPK'
    assert pa.encode_alpha('Devies') == 'DPK'
    assert pa.encode_alpha('Sand') == 'SNT'
    assert pa.encode_alpha('Sandau') == 'SNT'
