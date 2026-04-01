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

"""abydos.tests.phonetic.test_phonetic_ONCA.

This module contains unit tests for abydos.phonetic.ONCA
"""

from abydos.phonetic import ONCA


pa = ONCA()

def test_onca():
    """Test abydos.phonetic.ONCA."""
    # https://nces.ed.gov/FCSM/pdf/RLT97.pdf
    assert pa.encode('HALL') == 'H400'
    assert pa.encode('SMITH') == 'S530'

    # http://nchod.uhce.ox.ac.uk/NCHOD%20Oxford%20E5%20Report%201st%20Feb_VerAM2.pdf
    assert pa.encode('HAWTON') == 'H350'
    assert pa.encode('HORTON') == 'H635'
    assert pa.encode('HOUGHTON') == 'H235'

    # encode_alpha
    assert pa.encode_alpha('HALL') == 'HL'
    assert pa.encode_alpha('SMITH') == 'SNT'
    assert pa.encode_alpha('HOUGHTON') == 'HKTN'
