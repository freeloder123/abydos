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

"""abydos.tests.distance.test_distance_unknown_i.

This module contains unit tests for abydos.distance.UnknownI
"""


import pytest

from abydos.distance import UnknownI


cmp = UnknownI()


def test_unknown_i_sim():
    """Test abydos.distance.UnknownI.sim."""
    # Base cases
    assert cmp.sim('', '') == 0.5
    assert cmp.sim('a', '') == 0.2
    assert cmp.sim('', 'a') == 0.2
    assert cmp.sim('abc', '') == 0.125
    assert cmp.sim('', 'abc') == 0.125
    assert cmp.sim('abc', 'abc') == 0.8333333333333334
    assert cmp.sim('abcd', 'efgh') == 0.023809523809523808

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.125)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.125)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.125)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.125)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.1428571429)

def test_unknown_i_dist():
    """Test abydos.distance.UnknownI.dist."""
    # Base cases
    assert cmp.dist('', '') == 0.5
    assert cmp.dist('a', '') == 0.8
    assert cmp.dist('', 'a') == 0.8
    assert cmp.dist('abc', '') == 0.875
    assert cmp.dist('', 'abc') == 0.875
    assert cmp.dist('abc', 'abc') == 0.16666666666666663
    assert cmp.dist('abcd', 'efgh') == 0.9761904761904762

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.875)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.875)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.875)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.875)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.8571428571)
