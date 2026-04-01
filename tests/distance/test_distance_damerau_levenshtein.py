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

"""abydos.tests.distance.test_distance_damerau_levenshtein.

This module contains unit tests for abydos.distance.DamerauLevenshtein
"""


import pytest

from abydos.distance import DamerauLevenshtein


cmp = DamerauLevenshtein()

cmp571010 = DamerauLevenshtein(cost=(5, 7, 10, 10))

cmp1010510 = DamerauLevenshtein(cost=(10, 10, 5, 10))

cmp55105 = DamerauLevenshtein(cost=(5, 5, 10, 5))

cmp1010105 = DamerauLevenshtein(cost=(10, 10, 10, 5))


def test_damerau_levenshtein_dist_abs():
    """Test abydos.distance.DamerauLevenshtein.dist_abs."""
    assert cmp.dist_abs('', '') == 0
    assert cmp.dist_abs('CA', 'CA') == 0
    assert cmp.dist_abs('CA', 'ABC') == 2
    assert cmp571010.dist_abs('', 'b') == 5
    assert cmp571010.dist_abs('a', 'ab') == 5
    assert cmp571010.dist_abs('b', '') == 7
    assert cmp571010.dist_abs('ab', 'a') == 7
    assert cmp1010510.dist_abs('a', 'b') == 5
    assert cmp1010510.dist_abs('ac', 'bc') == 5
    assert cmp55105.dist_abs('ab', 'ba') == 5
    assert cmp55105.dist_abs('abc', 'bac') == 5
    assert cmp55105.dist_abs('cab', 'cba') == 5
    with pytest.raises(ValueError):
        cmp1010105.dist_abs('ab', 'ba')

def test_damerau_dist():
    """Test abydos.distance.DamerauLevenshtein.dist."""
    assert cmp.dist('', '') == 0

    assert cmp.dist('a', 'a') == 0
    assert cmp.dist('ab', 'ab') == 0
    assert cmp.dist('', 'a') == 1
    assert cmp.dist('', 'ab') == 1
    assert cmp.dist('a', 'c') == 1

    assert cmp.dist('abc', 'ac') == pytest.approx(abs=1e-7, expected=1 / 3)
    assert cmp.dist('abbc', 'ac') == pytest.approx(abs=1e-7, expected=1 / 2)
    assert cmp.dist('abbc', 'abc') == pytest.approx(abs=1e-7, expected=1 / 4)

    assert cmp.dist('CA', 'ABC') == pytest.approx(abs=1e-7, expected=2 / 3)
    assert cmp571010.dist('', 'b') == pytest.approx(abs=1e-7, expected=1)
    assert cmp571010.dist('a', 'ab') == pytest.approx(abs=1e-7, expected=1 / 2)
    assert cmp571010.dist('b', '') == pytest.approx(abs=1e-7, expected=1)
    assert cmp571010.dist('ab', 'a') == pytest.approx(abs=1e-7, expected=1 / 2)
    assert cmp1010510.dist('a', 'b') == pytest.approx(abs=1e-7, expected=1 / 2)
    assert cmp1010510.dist('ac', 'bc') == pytest.approx(abs=1e-7, expected=1 / 4)
    assert cmp55105.dist('ab', 'ba') == pytest.approx(abs=1e-7, expected=1 / 2)
    assert cmp55105.dist('abc', 'bac') == pytest.approx(abs=1e-7, expected=1 / 3)
    assert cmp55105.dist('cab', 'cba') == pytest.approx(abs=1e-7, expected=1 / 3)
    with pytest.raises(ValueError):
        cmp1010105.dist('ab', 'ba')

def test_damerau_sim():
    """Test abydos.distance.DamerauLevenshtein.sim."""
    assert cmp.sim('', '') == 1

    assert cmp.sim('a', 'a') == 1
    assert cmp.sim('ab', 'ab') == 1
    assert cmp.sim('', 'a') == 0
    assert cmp.sim('', 'ab') == 0
    assert cmp.sim('a', 'c') == 0

    assert cmp.sim('abc', 'ac') == pytest.approx(abs=1e-7, expected=2 / 3)
    assert cmp.sim('abbc', 'ac') == pytest.approx(abs=1e-7, expected=1 / 2)
    assert cmp.sim('abbc', 'abc') == pytest.approx(abs=1e-7, expected=3 / 4)

    assert cmp.sim('CA', 'ABC') == pytest.approx(abs=1e-7, expected=1 / 3)
    assert cmp571010.sim('', 'b') == pytest.approx(abs=1e-7, expected=0)
    assert cmp571010.sim('a', 'ab') == pytest.approx(abs=1e-7, expected=1 / 2)
    assert cmp571010.sim('b', '') == pytest.approx(abs=1e-7, expected=0)
    assert cmp571010.sim('ab', 'a') == pytest.approx(abs=1e-7, expected=1 / 2)
    assert cmp1010510.sim('a', 'b') == pytest.approx(abs=1e-7, expected=1 / 2)
    assert cmp1010510.sim('ac', 'bc') == pytest.approx(abs=1e-7, expected=3 / 4)
    assert cmp55105.sim('ab', 'ba') == pytest.approx(abs=1e-7, expected=1 / 2)
    assert cmp55105.sim('abc', 'bac') == pytest.approx(abs=1e-7, expected=2 / 3)
    assert cmp55105.sim('cab', 'cba') == pytest.approx(abs=1e-7, expected=2 / 3)
    with pytest.raises(ValueError):
        cmp1010105.sim('ab', 'ba')
