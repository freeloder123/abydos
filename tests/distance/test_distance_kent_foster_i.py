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

"""abydos.tests.distance.test_distance_kent_foster_i.

This module contains unit tests for abydos.distance.KentFosterI
"""


import pytest

from abydos.distance import KentFosterI


cmp = KentFosterI()

cmp_no_d = KentFosterI(alphabet=0)


def test_kent_foster_i_sim():
    """Test abydos.distance.KentFosterI.sim."""
    # Base cases
    assert cmp.sim('', '') == 1.0
    assert cmp.sim('a', '') == 1.0
    assert cmp.sim('', 'a') == 1.0
    assert cmp.sim('abc', '') == 1.0
    assert cmp.sim('', 'abc') == 1.0
    assert cmp.sim('abc', 'abc') == 1.0
    assert cmp.sim('abcd', 'efgh') == 0.6666666666666667

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.8)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.8)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.8)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.8)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.8604651163)

def test_kent_foster_i_dist():
    """Test abydos.distance.KentFosterI.dist."""
    # Base cases
    assert cmp.dist('', '') == 0.0
    assert cmp.dist('a', '') == 0.0
    assert cmp.dist('', 'a') == 0.0
    assert cmp.dist('abc', '') == 0.0
    assert cmp.dist('', 'abc') == 0.0
    assert cmp.dist('abc', 'abc') == 0.0
    assert cmp.dist('abcd', 'efgh') == 0.33333333333333326

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.2)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.2)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.2)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.2)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.1395348837)

def test_kent_foster_i_sim_score():
    """Test abydos.distance.KentFosterI.sim_score."""
    # Base cases
    assert cmp.sim_score('', '') == 0.0
    assert cmp.sim_score('a', '') == 0.0
    assert cmp.sim_score('', 'a') == 0.0
    assert cmp.sim_score('abc', '') == 0.0
    assert cmp.sim_score('', 'abc') == 0.0
    assert cmp.sim_score('abc', 'abc') == 0.0
    assert cmp.sim_score('abcd', 'efgh') == -0.3333333333333333

    assert cmp.sim_score('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=-0.2)
    assert cmp.sim_score('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=-0.2)
    assert cmp.sim_score('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=-0.2)
    assert cmp.sim_score('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=-0.2)
    assert cmp.sim_score('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=-0.1395348837)
