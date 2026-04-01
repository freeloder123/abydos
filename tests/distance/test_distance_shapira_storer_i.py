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

"""abydos.tests.distance.test_distance_shapira_storer_i.

This module contains unit tests for abydos.distance.ShapiraStorerI
"""


import pytest

from abydos.distance import ShapiraStorerI


cmp = ShapiraStorerI()

cmp_prime = ShapiraStorerI(prime=True)


def test_shapira_storer_i_dist():
    """Test abydos.distance.ShapiraStorerI.dist."""
    # Base cases
    assert cmp.dist('', '') == 0.0
    assert cmp.dist('a', '') == 1.0
    assert cmp.dist('', 'a') == 1.0
    assert cmp.dist('abc', '') == 1.0
    assert cmp.dist('', 'abc') == 1.0
    assert cmp.dist('abc', 'abc') == 0.0
    assert cmp.dist('abcd', 'efgh') == 1.0

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.4)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.4)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.1)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.1)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.2105263158)

    assert cmp.dist('AABAACADAB', 'AABAABAACADABADABAABAABAACADABADAB') == pytest.approx(abs=1e-7, expected=0.3409090909090909)
    assert cmp_prime.dist(
            'AABAACADAB', 'AABAABAACADABADABAABAABAACADABADAB'
        ) == pytest.approx(abs=1e-7, expected=0.5454545454545454)
    assert cmp.dist('AABAABAACADABADABAABAABAACADABADAB', 'AABAACADAB') == pytest.approx(abs=1e-7, expected=0.3409090909090909)
    assert cmp_prime.dist(
            'AABAABAACADABADABAABAABAACADABADAB', 'AABAACADAB'
        ) == pytest.approx(abs=1e-7, expected=0.5454545454545454)

def test_shapira_storer_i_sim():
    """Test abydos.distance.ShapiraStorerI.sim."""
    # Base cases
    assert cmp.sim('', '') == 1.0
    assert cmp.sim('a', '') == 0.0
    assert cmp.sim('', 'a') == 0.0
    assert cmp.sim('abc', '') == 0.0
    assert cmp.sim('', 'abc') == 0.0
    assert cmp.sim('abc', 'abc') == 1.0
    assert cmp.sim('abcd', 'efgh') == 0.0

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.6)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.6)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.9)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.9)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.7894736842)

    assert cmp.sim('AABAACADAB', 'AABAABAACADABADABAABAABAACADABADAB') == pytest.approx(abs=1e-7, expected=0.6590909090909092)
    assert cmp_prime.sim(
            'AABAACADAB', 'AABAABAACADABADABAABAABAACADABADAB'
        ) == pytest.approx(abs=1e-7, expected=0.4545454545454546)
    assert cmp.sim('AABAABAACADABADABAABAABAACADABADAB', 'AABAACADAB') == pytest.approx(abs=1e-7, expected=0.6590909090909092)
    assert cmp_prime.sim(
            'AABAABAACADABADABAABAABAACADABADAB', 'AABAACADAB'
        ) == pytest.approx(abs=1e-7, expected=0.4545454545454546)

def test_shapira_storer_i_dist_abs():
    """Test abydos.distance.ShapiraStorerI.dist_abs."""
    # Base cases
    assert cmp.dist_abs('', '') == 0
    assert cmp.dist_abs('a', '') == 1
    assert cmp.dist_abs('', 'a') == 1
    assert cmp.dist_abs('abc', '') == 3
    assert cmp.dist_abs('', 'abc') == 3
    assert cmp.dist_abs('abc', 'abc') == 0
    assert cmp.dist_abs('abcd', 'efgh') == 8

    assert cmp.dist_abs('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=4)
    assert cmp.dist_abs('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=4)
    assert cmp.dist_abs('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=1)
    assert cmp.dist_abs('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=1)
    assert cmp.dist_abs('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=4)

    assert cmp.dist_abs(
            'AABAACADAB', 'AABAABAACADABADABAABAABAACADABADAB'
        ) == pytest.approx(abs=1e-7, expected=15)
    assert cmp_prime.dist_abs(
            'AABAACADAB', 'AABAABAACADABADABAABAABAACADABADAB'
        ) == pytest.approx(abs=1e-7, expected=24)
    assert cmp.dist_abs(
            'AABAABAACADABADABAABAABAACADABADAB', 'AABAACADAB'
        ) == pytest.approx(abs=1e-7, expected=15)
    assert cmp_prime.dist_abs(
            'AABAABAACADABADABAABAABAACADABADAB', 'AABAACADAB'
        ) == pytest.approx(abs=1e-7, expected=24)
