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

"""abydos.tests.distance.test_distance_average_linkage.

This module contains unit tests for abydos.distance.AverageLinkage
"""


import pytest

from abydos.distance import AverageLinkage, Prefix
from abydos.tokenizer import QGrams


cmp = AverageLinkage()

cmp1 = AverageLinkage(tokenizer=QGrams(1))

cmp_pfx = AverageLinkage(metric=Prefix())


def test_average_linkage_dist():
    """Test abydos.distance.AverageLinkage.dist."""
    # Base cases
    assert cmp.dist('', '') == 0.0
    assert cmp.dist('a', '') == 1.0
    assert cmp.dist('', 'a') == 1.0
    assert cmp.dist('abc', '') == 1.0
    assert cmp.dist('', 'abc') == 1.0
    assert cmp.dist('abc', 'abc') == 0.75
    assert cmp.dist('abcd', 'efgh') == 0.96

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.8611111111)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.8611111111)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.8333333333)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.8333333333)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.7545454545)

    assert cmp1.dist('aaa', 'aaa') == 0.0
    assert cmp_pfx.dist('ababab', 'ab') == pytest.approx(abs=1e-7, expected=0.714285714)
