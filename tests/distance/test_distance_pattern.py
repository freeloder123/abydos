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

"""abydos.tests.distance.test_distance_pattern.

This module contains unit tests for abydos.distance.Pattern
"""


import pytest

from abydos.distance import Pattern


cmp = Pattern()

cmp_no_d = Pattern(alphabet=0)


def test_pattern_dist():
    """Test abydos.distance.Pattern.dist."""
    # Base cases
    assert cmp.dist('', '') == 0.0
    assert cmp.dist('a', '') == 0.0
    assert cmp.dist('', 'a') == 0.0
    assert cmp.dist('abc', '') == 0.0
    assert cmp.dist('', 'abc') == 0.0
    assert cmp.dist('abc', 'abc') == 0.0
    assert cmp.dist('abcd', 'efgh') == 0.0001626926280716368

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=5.85693e-05)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=5.85693e-05)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=5.85693e-05)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=5.85693e-05)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=7.80925e-05)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.dist('', '') == 0.0
    assert cmp_no_d.dist('a', '') == 0.0
    assert cmp_no_d.dist('', 'a') == 0.0
    assert cmp_no_d.dist('abc', '') == 0.0
    assert cmp_no_d.dist('', 'abc') == 0.0
    assert cmp_no_d.dist('abc', 'abc') == 0.0
    assert cmp_no_d.dist('abcd', 'efgh') == 1.0

    assert cmp_no_d.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.4444444444)
    assert cmp_no_d.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.4444444444)
    assert cmp_no_d.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.4444444444)
    assert cmp_no_d.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.4444444444)
    assert cmp_no_d.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.2448979592)

def test_pattern_sim():
    """Test abydos.distance.Pattern.sim."""
    # Base cases
    assert cmp.sim('', '') == 1.0
    assert cmp.sim('a', '') == 1.0
    assert cmp.sim('', 'a') == 1.0
    assert cmp.sim('abc', '') == 1.0
    assert cmp.sim('', 'abc') == 1.0
    assert cmp.sim('abc', 'abc') == 1.0
    assert cmp.sim('abcd', 'efgh') == 0.9998373073719283

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.9999414307)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.9999414307)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.9999414307)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.9999414307)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.9999219075)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.sim('', '') == 1.0
    assert cmp_no_d.sim('a', '') == 1.0
    assert cmp_no_d.sim('', 'a') == 1.0
    assert cmp_no_d.sim('abc', '') == 1.0
    assert cmp_no_d.sim('', 'abc') == 1.0
    assert cmp_no_d.sim('abc', 'abc') == 1.0
    assert cmp_no_d.sim('abcd', 'efgh') == 0.0

    assert cmp_no_d.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.5555555556)
    assert cmp_no_d.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.5555555556)
    assert cmp_no_d.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.5555555556)
    assert cmp_no_d.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.5555555556)
    assert cmp_no_d.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.7551020408)
