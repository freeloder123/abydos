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

"""abydos.tests.distance.test_distance_unknown_k.

This module contains unit tests for abydos.distance.UnknownK
"""


import pytest

from abydos.distance import UnknownK


cmp = UnknownK()

cmp_no_d = UnknownK(alphabet=0)


def test_unknown_k_dist():
    """Test abydos.distance.UnknownK.dist."""
    # Base cases
    assert cmp.dist('', '') == 1.0
    assert cmp.dist('a', '') == 1.0
    assert cmp.dist('', 'a') == 1.0
    assert cmp.dist('abc', '') == 1.0
    assert cmp.dist('', 'abc') == 1.0
    assert cmp.dist('abc', 'abc') == 0.9948979591836735
    assert cmp.dist('abcd', 'efgh') == 1.0

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.9961734694)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.9961734694)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.9961734694)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.9961734694)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.9910714286)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.dist('', '') == 0.0
    assert cmp_no_d.dist('a', '') == 1.0
    assert cmp_no_d.dist('', 'a') == 1.0
    assert cmp_no_d.dist('abc', '') == 1.0
    assert cmp_no_d.dist('', 'abc') == 1.0
    assert cmp_no_d.dist('abc', 'abc') == 0.0
    assert cmp_no_d.dist('abcd', 'efgh') == 1.0

    assert cmp_no_d.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.6666666667)
    assert cmp_no_d.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.6666666667)
    assert cmp_no_d.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.6666666667)
    assert cmp_no_d.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.6666666667)
    assert cmp_no_d.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.5)

def test_unknown_k_sim():
    """Test abydos.distance.UnknownK.sim."""
    # Base cases
    assert cmp.sim('', '') == 0.0
    assert cmp.sim('a', '') == 0.0
    assert cmp.sim('', 'a') == 0.0
    assert cmp.sim('abc', '') == 0.0
    assert cmp.sim('', 'abc') == 0.0
    assert cmp.sim('abc', 'abc') == 0.005102040816326481
    assert cmp.sim('abcd', 'efgh') == 0.0

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.0038265306)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.0038265306)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.0038265306)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.0038265306)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.0089285714)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.sim('', '') == 1.0
    assert cmp_no_d.sim('a', '') == 0.0
    assert cmp_no_d.sim('', 'a') == 0.0
    assert cmp_no_d.sim('abc', '') == 0.0
    assert cmp_no_d.sim('', 'abc') == 0.0
    assert cmp_no_d.sim('abc', 'abc') == 1.0
    assert cmp_no_d.sim('abcd', 'efgh') == 0.0

    assert cmp_no_d.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.3333333333)
    assert cmp_no_d.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.3333333333)
    assert cmp_no_d.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.3333333333)
    assert cmp_no_d.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.3333333333)
    assert cmp_no_d.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.5)

def test_unknown_k_dist_abs():
    """Test abydos.distance.UnknownK.dist_abs."""
    # Base cases
    assert cmp.dist_abs('', '') == 784.0
    assert cmp.dist_abs('a', '') == 784.0
    assert cmp.dist_abs('', 'a') == 784.0
    assert cmp.dist_abs('abc', '') == 784.0
    assert cmp.dist_abs('', 'abc') == 784.0
    assert cmp.dist_abs('abc', 'abc') == 780.0
    assert cmp.dist_abs('abcd', 'efgh') == 784.0

    assert cmp.dist_abs('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=781.0)
    assert cmp.dist_abs('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=781.0)
    assert cmp.dist_abs('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=781.0)
    assert cmp.dist_abs('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=781.0)
    assert cmp.dist_abs('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=777.0)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.dist_abs('', '') == 0.0
    assert cmp_no_d.dist_abs('a', '') == 2.0
    assert cmp_no_d.dist_abs('', 'a') == 2.0
    assert cmp_no_d.dist_abs('abc', '') == 4.0
    assert cmp_no_d.dist_abs('', 'abc') == 4.0
    assert cmp_no_d.dist_abs('abc', 'abc') == 0.0
    assert cmp_no_d.dist_abs('abcd', 'efgh') == 10.0

    assert cmp_no_d.dist_abs('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=6.0)
    assert cmp_no_d.dist_abs('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=6.0)
    assert cmp_no_d.dist_abs('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=6.0)
    assert cmp_no_d.dist_abs('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=6.0)
    assert cmp_no_d.dist_abs('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=7.0)
