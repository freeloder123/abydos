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

"""abydos.tests.distance.test_distance_hamming.

This module contains unit tests for abydos.distance.Hamming
"""


import pytest

from abydos.distance import Hamming


cmp = Hamming()

cmp_no_diff = Hamming(False)


def test_hamming_dist_abs():
    """Test abydos.distance.Hamming.dist_abs."""
    assert cmp.dist_abs('', '') == 0
    assert cmp_no_diff.dist_abs('', '') == 0

    assert cmp.dist_abs('a', '') == 1
    assert cmp.dist_abs('a', 'a') == 0
    assert cmp_no_diff.dist_abs('a', 'a') == 0
    assert cmp.dist_abs('a', 'b') == 1
    assert cmp_no_diff.dist_abs('a', 'b') == 1
    assert cmp.dist_abs('abc', 'cba') == 2
    assert cmp_no_diff.dist_abs('abc', 'cba') == 2
    assert cmp.dist_abs('abc', '') == 3
    assert cmp.dist_abs('bb', 'cbab') == 3

    # test exception
    with pytest.raises(ValueError):
        cmp_no_diff.dist_abs('ab', 'a')

    # https://en.wikipedia.org/wiki/Hamming_distance
    assert cmp.dist_abs('karolin', 'kathrin') == 3
    assert cmp.dist_abs('karolin', 'kerstin') == 3
    assert cmp.dist_abs('1011101', '1001001') == 2
    assert cmp.dist_abs('2173896', '2233796') == 3

def test_hamming_dist():
    """Test abydos.distance.Hamming.dist."""
    assert cmp.dist('', '') == 0
    assert cmp_no_diff.dist('', '') == 0

    assert cmp.dist('a', '') == 1
    assert cmp.dist('a', 'a') == 0
    assert cmp_no_diff.dist('a', 'a') == 0
    assert cmp.dist('a', 'b') == 1
    assert cmp_no_diff.dist('a', 'b') == 1
    assert cmp.dist('abc', 'cba') == pytest.approx(abs=1e-7, expected=2 / 3)
    assert cmp_no_diff.dist('abc', 'cba') == pytest.approx(abs=1e-7, expected=2 / 3)
    assert cmp.dist('abc', '') == 1
    assert cmp.dist('bb', 'cbab') == pytest.approx(abs=1e-7, expected=3 / 4)

    # test exception
    with pytest.raises(ValueError):
        cmp_no_diff.dist('ab', 'a')

    # https://en.wikipedia.org/wiki/Hamming_distance
    assert cmp.dist('karolin', 'kathrin') == pytest.approx(abs=1e-7, expected=3 / 7)
    assert cmp.dist('karolin', 'kerstin') == pytest.approx(abs=1e-7, expected=3 / 7)
    assert cmp.dist('1011101', '1001001') == pytest.approx(abs=1e-7, expected=2 / 7)
    assert cmp.dist('2173896', '2233796') == pytest.approx(abs=1e-7, expected=3 / 7)

def test_hamming_sim():
    """Test abydos.distance.Hamming.sim."""
    assert cmp.sim('', '') == 1
    assert cmp_no_diff.sim('', '') == 1

    assert cmp.sim('a', '') == 0
    assert cmp.sim('a', 'a') == 1
    assert cmp_no_diff.sim('a', 'a') == 1
    assert cmp.sim('a', 'b') == 0
    assert cmp_no_diff.sim('a', 'b') == 0
    assert cmp.sim('abc', 'cba') == pytest.approx(abs=1e-7, expected=1 / 3)
    assert cmp_no_diff.sim('abc', 'cba') == pytest.approx(abs=1e-7, expected=1 / 3)
    assert cmp.sim('abc', '') == 0
    assert cmp.sim('bb', 'cbab') == pytest.approx(abs=1e-7, expected=1 / 4)

    # test exception
    with pytest.raises(ValueError):
        cmp_no_diff.sim('ab', 'a')

    # https://en.wikipedia.org/wiki/Hamming_distance
    assert cmp.sim('karolin', 'kathrin') == pytest.approx(abs=1e-7, expected=4 / 7)
    assert cmp.sim('karolin', 'kerstin') == pytest.approx(abs=1e-7, expected=4 / 7)
    assert cmp.sim('1011101', '1001001') == pytest.approx(abs=1e-7, expected=5 / 7)
    assert cmp.sim('2173896', '2233796') == pytest.approx(abs=1e-7, expected=4 / 7)
