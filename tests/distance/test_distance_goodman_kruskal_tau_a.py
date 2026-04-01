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

"""abydos.tests.distance.test_distance_goodman_kruskal_tau_a.

This module contains unit tests for abydos.distance.GoodmanKruskalTauA
"""


import pytest

from abydos.distance import GoodmanKruskalTauA
from abydos.tokenizer import QGrams


cmp = GoodmanKruskalTauA()

cmp_no_d = GoodmanKruskalTauA(alphabet=0)


def test_goodman_kruskal_tau_a_sim():
    """Test abydos.distance.GoodmanKruskalTauA.sim."""
    # Base cases
    assert cmp.sim('', '') == 0.0
    assert cmp.sim('a', '') == 0.0
    assert cmp.sim('', 'a') == 0.0
    assert cmp.sim('abc', '') == 0.0
    assert cmp.sim('', 'abc') == 0.0
    assert cmp.sim('abc', 'abc') == 0.748403575989782
    assert cmp.sim('abcd', 'efgh') == 4.119695274745721e-05

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.3290773882)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.3290773882)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.3290773882)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.3290773882)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.4593665172)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.sim('', '') == 0.0
    assert cmp_no_d.sim('a', '') == 0.0
    assert cmp_no_d.sim('', 'a') == 0.0
    assert cmp_no_d.sim('abc', '') == 0.0
    assert cmp_no_d.sim('', 'abc') == 0.0
    assert cmp_no_d.sim('abc', 'abc') == 0.3333333333333333
    assert cmp_no_d.sim('abcd', 'efgh') == 1.0

    assert cmp_no_d.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.2727272727)
    assert cmp_no_d.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.2727272727)
    assert cmp_no_d.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.2727272727)
    assert cmp_no_d.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.2727272727)
    assert cmp_no_d.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.2437299035)

    assert GoodmanKruskalTauA(
            intersection_type='linkage',
            alphabet=64,
            tokenizer=QGrams(qval=range(2, 4), skip=1),
        ).sim('adhering', 'gilled') == pytest.approx(abs=1e-7, expected=0.08653625551656584)
    assert GoodmanKruskalTauA(
            intersection_type='linkage',
            alphabet=64,
            tokenizer=QGrams(qval=range(2, 4), skip=1),
        ).sim('gilled', 'adhering') == pytest.approx(abs=1e-7, expected=0.10431548499366636)

def test_goodman_kruskal_tau_a_dist():
    """Test abydos.distance.GoodmanKruskalTauA.dist."""
    # Base cases
    assert cmp.dist('', '') == 1.0
    assert cmp.dist('a', '') == 1.0
    assert cmp.dist('', 'a') == 1.0
    assert cmp.dist('abc', '') == 1.0
    assert cmp.dist('', 'abc') == 1.0
    assert cmp.dist('abc', 'abc') == 0.251596424010218
    assert cmp.dist('abcd', 'efgh') == 0.9999588030472526

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.6709226118)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.6709226118)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.6709226118)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.6709226118)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.5406334828)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.dist('', '') == 1.0
    assert cmp_no_d.dist('a', '') == 1.0
    assert cmp_no_d.dist('', 'a') == 1.0
    assert cmp_no_d.dist('abc', '') == 1.0
    assert cmp_no_d.dist('', 'abc') == 1.0
    assert cmp_no_d.dist('abc', 'abc') == 0.6666666666666667
    assert cmp_no_d.dist('abcd', 'efgh') == 0.0

    assert cmp_no_d.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.7272727273)
    assert cmp_no_d.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.7272727273)
    assert cmp_no_d.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.7272727273)
    assert cmp_no_d.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.7272727273)
    assert cmp_no_d.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.7562700965)
