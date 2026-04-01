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

"""abydos.tests.distance.test_distance_flexmetric.

This module contains unit tests for abydos.distance.FlexMetric
"""


import pytest

from abydos.distance import FlexMetric


cmp = FlexMetric()

cmp_custom = FlexMetric(


    indel_costs=[(set('aeiou'), 0.1), (set('bcdfghjklmnpqrstvwxyz'), 0.9)],
    subst_costs=[(set('aeiou'), 0.1), (set('bcdfghjklmnpqrstvwxyz'), 0.9)],
    )

def test_flexmetric_dist():
    """Test abydos.distance.FlexMetric.dist."""
    # Base cases
    assert cmp.dist('', '') == 0.0
    assert cmp.dist('a', '') == 1.0
    assert cmp.dist('', 'a') == 1.0
    assert cmp.dist('abc', '') == pytest.approx(abs=1e-7, expected=0.7999999999999999)
    assert cmp.dist('', 'abc') == pytest.approx(abs=1e-7, expected=0.7999999999999999)
    assert cmp.dist('abc', 'abc') == 0.0
    assert cmp.dist('abcd', 'efgh') == pytest.approx(abs=1e-7, expected=0.925)

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.3)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.3)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.4)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.4)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.26)

def test_flexmetric_sim():
    """Test abydos.distance.FlexMetric.sim."""
    # Base cases
    assert cmp.sim('', '') == 1.0
    assert cmp.sim('a', '') == 0.0
    assert cmp.sim('', 'a') == 0.0
    assert cmp.sim('abc', '') == pytest.approx(abs=1e-7, expected=0.20000000000000007)
    assert cmp.sim('', 'abc') == pytest.approx(abs=1e-7, expected=0.20000000000000007)
    assert cmp.sim('abc', 'abc') == 1.0
    assert cmp.sim('abcd', 'efgh') == pytest.approx(abs=1e-7, expected=0.075)

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.7)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.7)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.6)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.6)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.74)

def test_flexmetric_dist_abs():
    """Test abydos.distance.FlexMetric.dist_abs."""
    # Base cases
    assert cmp.dist_abs('', '') == 0
    assert cmp.dist_abs('a', '') == 1.0
    assert cmp.dist_abs('', 'a') == 1.0
    assert cmp.dist_abs('abc', '') == 2.4
    assert cmp.dist_abs('', 'abc') == 2.4
    assert cmp.dist_abs('abc', 'abc') == 0
    assert cmp.dist_abs('abcd', 'efgh') == pytest.approx(abs=1e-7, expected=3.6999999999999997)

    assert cmp.dist_abs('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=1.5)
    assert cmp.dist_abs('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=1.5)
    assert cmp.dist_abs('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=2.0)
    assert cmp.dist_abs('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=2.0)
    assert cmp.dist_abs('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=2.6)

    assert cmp_custom.dist_abs('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=1.0)
    assert cmp_custom.dist_abs('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=1.0)
    assert cmp_custom.dist_abs('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.2)
    assert cmp_custom.dist_abs('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.2)
    assert cmp_custom.dist_abs('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=3.7)
