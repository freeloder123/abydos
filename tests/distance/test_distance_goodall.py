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

"""abydos.tests.distance.test_distance_goodall.

This module contains unit tests for abydos.distance.Goodall
"""


import pytest

from abydos.distance import Goodall


cmp = Goodall()

cmp_no_d = Goodall(alphabet=0)


def test_goodall_sim():
    """Test abydos.distance.Goodall.sim."""
    # Base cases
    assert cmp.sim('', '') == 1.0
    assert cmp.sim('a', '') == 0.9678321591500222
    assert cmp.sim('', 'a') == 0.9678321591500222
    assert cmp.sim('abc', '') == 0.9544884026871964
    assert cmp.sim('', 'abc') == 0.9544884026871964
    assert cmp.sim('abc', 'abc') == 1.0
    assert cmp.sim('abcd', 'efgh') == 0.9279473952929225

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.9442360891)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.9442360891)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.9442360891)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.9442360891)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.939755208)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.sim('', '') == 1.0
    assert cmp_no_d.sim('a', '') == 0.0
    assert cmp_no_d.sim('', 'a') == 0.0
    assert cmp_no_d.sim('abc', '') == 0.0
    assert cmp_no_d.sim('', 'abc') == 0.0
    assert cmp_no_d.sim('abc', 'abc') == 1.0
    assert cmp_no_d.sim('abcd', 'efgh') == 0.0

    assert cmp_no_d.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.391826552)
    assert cmp_no_d.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.391826552)
    assert cmp_no_d.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.391826552)
    assert cmp_no_d.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.391826552)
    assert cmp_no_d.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.5)

def test_goodall_dist():
    """Test abydos.distance.Goodall.dist."""
    # Base cases
    assert cmp.dist('', '') == 0.0
    assert cmp.dist('a', '') == 0.03216784084997781
    assert cmp.dist('', 'a') == 0.03216784084997781
    assert cmp.dist('abc', '') == 0.04551159731280363
    assert cmp.dist('', 'abc') == 0.04551159731280363
    assert cmp.dist('abc', 'abc') == 0.0
    assert cmp.dist('abcd', 'efgh') == 0.07205260470707753

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.0557639109)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.0557639109)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.0557639109)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.0557639109)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.060244792)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.dist('', '') == 0.0
    assert cmp_no_d.dist('a', '') == 1.0
    assert cmp_no_d.dist('', 'a') == 1.0
    assert cmp_no_d.dist('abc', '') == 1.0
    assert cmp_no_d.dist('', 'abc') == 1.0
    assert cmp_no_d.dist('abc', 'abc') == 0.0
    assert cmp_no_d.dist('abcd', 'efgh') == 1.0

    assert cmp_no_d.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.608173448)
    assert cmp_no_d.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.608173448)
    assert cmp_no_d.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.608173448)
    assert cmp_no_d.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.608173448)
    assert cmp_no_d.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.5)
