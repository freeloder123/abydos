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

"""abydos.tests.distance.test_distance_tichy.

This module contains unit tests for abydos.distance.Tichy
"""


import pytest

from abydos.distance import Tichy


cmp = Tichy()


def test_tichy_dist():
    """Test abydos.distance.Tichy.dist."""
    # Base cases
    assert cmp.dist('', '') == 0.0
    assert cmp.dist('a', '') == 0.0
    assert cmp.dist('', 'a') == 1.0
    assert cmp.dist('abc', '') == 0.0
    assert cmp.dist('', 'abc') == 1.0
    assert cmp.dist('abc', 'abc') == 0.0
    assert cmp.dist('abcd', 'efgh') == 1.0

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.8)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.8)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.8)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.8)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.4444444444)

def test_tichy_sim():
    """Test abydos.distance.Tichy.sim."""
    # Base cases
    assert cmp.sim('', '') == 1.0
    assert cmp.sim('a', '') == 1.0
    assert cmp.sim('', 'a') == 0.0
    assert cmp.sim('abc', '') == 1.0
    assert cmp.sim('', 'abc') == 0.0
    assert cmp.sim('abc', 'abc') == 1.0
    assert cmp.sim('abcd', 'efgh') == 0.0

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.2)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.2)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.2)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.2)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.5555555556)

def test_tichy_dist_abs():
    """Test abydos.distance.Tichy.dist_abs."""
    # Base cases
    assert cmp.dist_abs('', '') == 0
    assert cmp.dist_abs('a', '') == 0
    assert cmp.dist_abs('', 'a') == 1
    assert cmp.dist_abs('abc', '') == 0
    assert cmp.dist_abs('', 'abc') == 3
    assert cmp.dist_abs('abc', 'abc') == 0
    assert cmp.dist_abs('abcd', 'efgh') == 4

    assert cmp.dist_abs('Nigel', 'Niall') == 4
    assert cmp.dist_abs('Niall', 'Nigel') == 4
    assert cmp.dist_abs('Colin', 'Coiln') == 4
    assert cmp.dist_abs('Coiln', 'Colin') == 4
    assert cmp.dist_abs('ATCAACGAGT', 'AACGATTAG') == 4

    # Examples from paper

    assert cmp.dist_abs('abda', 'abcab') == 3
    assert cmp.dist_abs('shanghai', 'sakhalin') == 7
    assert cmp.dist_abs('abcde', 'deabc') == 2
    assert cmp.dist_abs('abc', 'abcabc') == 2
    assert cmp.dist_abs('abcdea', 'cdab') == 2
    assert cmp.dist_abs('abcdefdeab', 'cdeabc') == 2
