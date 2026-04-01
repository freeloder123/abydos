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

"""abydos.tests.distance.test_distance_indel.

This module contains unit tests for abydos.distance.Indel
"""


import pytest

from abydos.distance import Indel


cmp = Indel()


def test_indel_sim():
    """Test abydos.distance.Indel.sim."""
    # Base cases
    assert cmp.sim('', '') == 1
    assert cmp.sim('a', '') == 0
    assert cmp.sim('', 'a') == 0
    assert cmp.sim('abc', '') == 0
    assert cmp.sim('', 'abc') == 0
    assert cmp.sim('abcd', 'efgh') == 0

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.6)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.6)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.8)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.8)

def test_indel_dist():
    """Test abydos.distance.Indel.dist."""
    # Base cases
    assert cmp.dist('', '') == 0
    assert cmp.dist('a', '') == 1
    assert cmp.dist('', 'a') == 1
    assert cmp.dist('abc', '') == 1
    assert cmp.dist('', 'abc') == 1
    assert cmp.dist('abcd', 'efgh') == 1

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.4)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.4)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.2)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.2)

def test_indel_dist_abs():
    """Test abydos.distance.Indel.dist_abs."""
    # Base cases
    assert cmp.dist_abs('', '') == 0
    assert cmp.dist_abs('a', '') == 1
    assert cmp.dist_abs('', 'a') == 1
    assert cmp.dist_abs('abc', '') == 3
    assert cmp.dist_abs('', 'abc') == 3
    assert cmp.dist_abs('abcd', 'efgh') == 8

    assert cmp.dist_abs('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=4)
    assert cmp.dist_abs('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=4)
    assert cmp.dist_abs('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=2)
    assert cmp.dist_abs('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=2)
