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

"""abydos.tests.distance.test_distance_baulieu_xi.

This module contains unit tests for abydos.distance.BaulieuXI
"""


import pytest

from abydos.distance import BaulieuXI


cmp = BaulieuXI()

cmp_no_d = BaulieuXI(alphabet=0)


def test_baulieu_xi_dist():
    """Test abydos.distance.BaulieuXI.dist."""
    # Base cases
    assert cmp.dist('', '') == 0.0
    assert cmp.dist('a', '') == 0.002551020408163265
    assert cmp.dist('', 'a') == 0.002551020408163265
    assert cmp.dist('abc', '') == 0.00510204081632653
    assert cmp.dist('', 'abc') == 0.00510204081632653
    assert cmp.dist('abc', 'abc') == 0.0
    assert cmp.dist('abcd', 'efgh') == 0.012755102040816327

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.0076824584)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.0076824584)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.0076824584)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.0076824584)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.009009009)

def test_baulieu_xi_sim():
    """Test abydos.distance.BaulieuXI.sim."""
    # Base cases
    assert cmp.sim('', '') == 1.0
    assert cmp.sim('a', '') == 0.9974489795918368
    assert cmp.sim('', 'a') == 0.9974489795918368
    assert cmp.sim('abc', '') == 0.9948979591836735
    assert cmp.sim('', 'abc') == 0.9948979591836735
    assert cmp.sim('abc', 'abc') == 1.0
    assert cmp.sim('abcd', 'efgh') == 0.9872448979591837

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.9923175416)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.9923175416)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.9923175416)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.9923175416)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.990990991)
