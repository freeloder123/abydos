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

"""abydos.tests.distance.test_distance_andres_marzo_delta.

This module contains unit tests for abydos.distance.AndresMarzoDelta
"""


import pytest

from abydos.distance import AndresMarzoDelta


cmp = AndresMarzoDelta()

cmp_no_d = AndresMarzoDelta(alphabet=0)


def test_andres_marzo_delta_sim():
    """Test abydos.distance.AndresMarzoDelta.sim."""
    # Base cases
    assert cmp.sim('', '') == 1.0
    assert cmp.sim('a', '') == 0.9987244897959184
    assert cmp.sim('', 'a') == 0.9987244897959184
    assert cmp.sim('abc', '') == 0.9974489795918368
    assert cmp.sim('', 'abc') == 0.9974489795918368
    assert cmp.sim('abc', 'abc') == 1.0
    assert cmp.sim('abcd', 'efgh') == 0.9872448979591837

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.9923469388)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.9923469388)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.9923469388)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.9923469388)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.9911172173)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.sim('', '') == 1.0
    assert cmp_no_d.sim('a', '') == 0.5
    assert cmp_no_d.sim('', 'a') == 0.5
    assert cmp_no_d.sim('abc', '') == 0.5
    assert cmp_no_d.sim('', 'abc') == 0.5
    assert cmp_no_d.sim('abc', 'abc') == 1.0
    assert cmp_no_d.sim('abcd', 'efgh') == 0.0

    assert cmp_no_d.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.3333333333)
    assert cmp_no_d.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.3333333333)
    assert cmp_no_d.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.3333333333)
    assert cmp_no_d.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.3333333333)
    assert cmp_no_d.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.5025641703)

def test_andres_marzo_delta_corr():
    """Test abydos.distance.AndresMarzoDelta.corr."""
    # Base cases
    assert cmp.corr('', '') == 1.0
    assert cmp.corr('a', '') == 0.9974489795918368
    assert cmp.corr('', 'a') == 0.9974489795918368
    assert cmp.corr('abc', '') == 0.9948979591836735
    assert cmp.corr('', 'abc') == 0.9948979591836735
    assert cmp.corr('abc', 'abc') == 1.0
    assert cmp.corr('abcd', 'efgh') == 0.9744897959183674

    assert cmp.corr('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.9846938776)
    assert cmp.corr('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.9846938776)
    assert cmp.corr('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.9846938776)
    assert cmp.corr('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.9846938776)
    assert cmp.corr('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.9822344347)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.corr('', '') == 1.0
    assert cmp_no_d.corr('a', '') == 0.0
    assert cmp_no_d.corr('', 'a') == 0.0
    assert cmp_no_d.corr('abc', '') == 0.0
    assert cmp_no_d.corr('', 'abc') == 0.0
    assert cmp_no_d.corr('abc', 'abc') == 1.0
    assert cmp_no_d.corr('abcd', 'efgh') == -1.0

    assert cmp_no_d.corr('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=-0.3333333333)
    assert cmp_no_d.corr('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=-0.3333333333)
    assert cmp_no_d.corr('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=-0.3333333333)
    assert cmp_no_d.corr('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=-0.3333333333)
    assert cmp_no_d.corr('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.0051283407)
