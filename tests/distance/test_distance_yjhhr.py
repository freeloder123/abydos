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

"""abydos.tests.distance.test_distance_yjhhr.

This module contains unit tests for abydos.distance.YJHHR
"""


import pytest

from abydos.distance import YJHHR


cmp = YJHHR()

cmp_p3 = YJHHR(pval=3)


def test_yjhhr_dist():
    """Test abydos.distance.YJHHR.dist."""
    # Base cases
    assert cmp.dist('', '') == 0.0
    assert cmp.dist('a', '') == 1.0
    assert cmp.dist('', 'a') == 1.0
    assert cmp.dist('abc', '') == 1.0
    assert cmp.dist('', 'abc') == 1.0
    assert cmp.dist('abc', 'abc') == 0.0
    assert cmp.dist('abcd', 'efgh') == 1.0

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.6666666666)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.6666666666)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.6666666666)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.6666666666)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.5)

    # Base cases
    assert cmp_p3.dist('', '') == 0.0
    assert cmp_p3.dist('a', '') == 1.0
    assert cmp_p3.dist('', 'a') == 1.0
    assert cmp_p3.dist('abc', '') == 1.0
    assert cmp_p3.dist('', 'abc') == 1.0
    assert cmp_p3.dist('abc', 'abc') == 0.0
    assert cmp_p3.dist('abcd', 'efgh') == 0.6299605249474369

    assert cmp_p3.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.4199736833)
    assert cmp_p3.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.4199736833)
    assert cmp_p3.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.4199736833)
    assert cmp_p3.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.4199736833)
    assert cmp_p3.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.32128153180538643)

def test_yjhhr_sim():
    """Test abydos.distance.YJHHR.sim."""
    # Base cases
    assert cmp.sim('', '') == 1.0
    assert cmp.sim('a', '') == 0.0
    assert cmp.sim('', 'a') == 0.0
    assert cmp.sim('abc', '') == 0.0
    assert cmp.sim('', 'abc') == 0.0
    assert cmp.sim('abc', 'abc') == 1.0
    assert cmp.sim('abcd', 'efgh') == 0.0

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.3333333333)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.3333333333)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.3333333333)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.3333333333)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.5)

    # Base cases
    assert cmp_p3.sim('', '') == 1.0
    assert cmp_p3.sim('a', '') == 0.0
    assert cmp_p3.sim('', 'a') == 0.0
    assert cmp_p3.sim('abc', '') == 0.0
    assert cmp_p3.sim('', 'abc') == 0.0
    assert cmp_p3.sim('abc', 'abc') == 1.0
    assert cmp_p3.sim('abcd', 'efgh') == 0.37003947505256307

    assert cmp_p3.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.5800263167)
    assert cmp_p3.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.5800263167)
    assert cmp_p3.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.5800263167)
    assert cmp_p3.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.5800263167)
    assert cmp_p3.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.6787184681946136)

def test_yjhhr_dist_abs():
    """Test abydos.distance.YJHHR.dist_abs."""
    # Base cases
    assert cmp.dist_abs('', '') == 0.0
    assert cmp.dist_abs('a', '') == 2.0
    assert cmp.dist_abs('', 'a') == 2.0
    assert cmp.dist_abs('abc', '') == 4.0
    assert cmp.dist_abs('', 'abc') == 4.0
    assert cmp.dist_abs('abc', 'abc') == 0.0
    assert cmp.dist_abs('abcd', 'efgh') == 10.0

    assert cmp.dist_abs('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=6.0)
    assert cmp.dist_abs('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=6.0)
    assert cmp.dist_abs('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=6.0)
    assert cmp.dist_abs('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=6.0)
    assert cmp.dist_abs('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=7.0)

    # Base cases
    assert cmp_p3.dist_abs('', '') == 0.0
    assert cmp_p3.dist_abs('a', '') == 2.0
    assert cmp_p3.dist_abs('', 'a') == 2.0
    assert cmp_p3.dist_abs('abc', '') == 4.0
    assert cmp_p3.dist_abs('', 'abc') == 4.0
    assert cmp_p3.dist_abs('abc', 'abc') == 0.0
    assert cmp_p3.dist_abs('abcd', 'efgh') == 6.29960524947437

    assert cmp_p3.dist_abs('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=3.77976314968462)
    assert cmp_p3.dist_abs('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=3.77976314968462)
    assert cmp_p3.dist_abs('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=3.77976314968462)
    assert cmp_p3.dist_abs('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=3.77976314968462)
    assert cmp_p3.dist_abs('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=4.49794144527541)
