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

"""abydos.tests.distance.test_distance_ample.

This module contains unit tests for abydos.distance.AMPLE
"""


import pytest

from abydos.distance import AMPLE


cmp = AMPLE()

cmp_no_d = AMPLE(alphabet=0)

cmp_dna = AMPLE(qval=1, alphabet='CGAT')


def test_ample_sim():
    """Test abydos.distance.AMPLE.sim."""
    # Base cases
    assert cmp.sim('', '') == 1.0
    assert cmp.sim('a', '') == 0.0
    assert cmp.sim('', 'a') == 0.002551020408163265
    assert cmp.sim('abc', '') == 0.0
    assert cmp.sim('', 'abc') == 0.00510204081632653
    assert cmp.sim('abc', 'abc') == 1.0
    assert cmp.sim('abcd', 'efgh') == 0.006418485237483954

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.4961439589)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.4961439589)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.4961439589)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.4961439589)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.6324826532)
    assert cmp_dna.sim('CGAT', 'CGA') == pytest.approx(abs=1e-7, expected=0.75)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.sim('', '') == 1.0
    assert cmp_no_d.sim('a', '') == 0.0
    assert cmp_no_d.sim('', 'a') == 1.0
    assert cmp_no_d.sim('abc', '') == 0.0
    assert cmp_no_d.sim('', 'abc') == 1.0
    assert cmp_no_d.sim('abc', 'abc') == 1.0
    assert cmp_no_d.sim('abcd', 'efgh') == 1.0

    assert cmp_no_d.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.5)
    assert cmp_no_d.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.5)
    assert cmp_no_d.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.5)
    assert cmp_no_d.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.5)
    assert cmp_no_d.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.3636363636)
