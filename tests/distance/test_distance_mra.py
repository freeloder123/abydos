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

"""abydos.tests.distance.test_distance_mra.

This module contains unit tests for abydos.distance.MRA
"""


import pytest

from abydos.distance import MRA


cmp = MRA()


def test_mra_dist_abs():
    """Test abydos.distance.MRA.dist_abs."""
    assert cmp.dist_abs('', '') == 6
    assert cmp.dist_abs('a', 'a') == 6
    assert cmp.dist_abs('abcdefg', 'abcdefg') == 6
    assert cmp.dist_abs('abcdefg', '') == 0
    assert cmp.dist_abs('', 'abcdefg') == 0

    # https://en.wikipedia.org/wiki/Match_rating_approach
    assert cmp.dist_abs('Byrne', 'Boern') == 5
    assert cmp.dist_abs('Smith', 'Smyth') == 5
    assert cmp.dist_abs('Catherine', 'Kathryn') == 4

    assert cmp.dist_abs('ab', 'abcdefgh') == 0
    assert cmp.dist_abs('ab', 'ac') == 5
    assert cmp.dist_abs('abcdefik', 'abcdefgh') == 3
    assert cmp.dist_abs('xyz', 'abc') == 0

def test_mra_sim():
    """Test abydos.distance.MRA.sim."""
    assert cmp.sim('', '') == 1
    assert cmp.sim('a', 'a') == 1
    assert cmp.sim('abcdefg', 'abcdefg') == 1
    assert cmp.sim('abcdefg', '') == 0
    assert cmp.sim('', 'abcdefg') == 0

    # https://en.wikipedia.org/wiki/Match_rating_approach
    assert cmp.sim('Byrne', 'Boern') == 5 / 6
    assert cmp.sim('Smith', 'Smyth') == 5 / 6
    assert cmp.sim('Catherine', 'Kathryn') == 4 / 6

    assert cmp.sim('ab', 'abcdefgh') == 0
    assert cmp.sim('ab', 'ac') == 5 / 6
    assert cmp.sim('abcdefik', 'abcdefgh') == 3 / 6
    assert cmp.sim('xyz', 'abc') == 0

def test_mra_dist():
    """Test abydos.distance.MRA.dist."""
    assert cmp.dist('', '') == 0
    assert cmp.dist('a', 'a') == 0
    assert cmp.dist('abcdefg', 'abcdefg') == 0
    assert cmp.dist('abcdefg', '') == 1
    assert cmp.dist('', 'abcdefg') == 1

    # https://en.wikipedia.org/wiki/Match_rating_approach
    assert cmp.dist('Byrne', 'Boern') == pytest.approx(abs=1e-7, expected=1 / 6)
    assert cmp.dist('Smith', 'Smyth') == pytest.approx(abs=1e-7, expected=1 / 6)
    assert cmp.dist('Catherine', 'Kathryn') == pytest.approx(abs=1e-7, expected=2 / 6)

    assert cmp.dist('ab', 'abcdefgh') == 1
    assert cmp.dist('ab', 'ac') == pytest.approx(abs=1e-7, expected=1 / 6)
    assert cmp.dist('abcdefik', 'abcdefgh') == pytest.approx(abs=1e-7, expected=3 / 6)
    assert cmp.dist('xyz', 'abc') == 1
