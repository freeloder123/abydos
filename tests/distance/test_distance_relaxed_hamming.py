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

"""abydos.tests.distance.test_distance_relaxed_hamming.

This module contains unit tests for abydos.distance.RelaxedHamming
"""


import pytest

from abydos.distance import RelaxedHamming


cmp = RelaxedHamming()


def test_relaxed_hamming_dist():
    """Test abydos.distance.RelaxedHamming.dist."""
    # Base cases
    assert cmp.dist('', '') == 0.0
    assert cmp.dist('a', '') == 1.0
    assert cmp.dist('', 'a') == 1.0
    assert cmp.dist('abc', '') == 1.0
    assert cmp.dist('', 'abc') == 1.0
    assert cmp.dist('abc', 'abc') == 0.0
    assert cmp.dist('abcd', 'efgh') == 1.0

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.4)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.24)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.08)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.08)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.36)

    assert cmp.dist('hamming', 'hamstring') == pytest.approx(abs=1e-7, expected=0.37777777777)

    # coverage
    assert RelaxedHamming(qval=2).dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.5)
    assert RelaxedHamming(qval=2).dist('Nigal', 'Niall') == pytest.approx(abs=1e-7, expected=0.3666666666666667)
    assert cmp.dist('Nigel', 'Niall\1') == pytest.approx(abs=1e-7, expected=0.5)

def test_relaxed_hamming_dist_abs():
    """Test abydos.distance.RelaxedHamming.dist_abs."""
    # Base cases
    assert cmp.dist_abs('', '') == 0.0
    assert cmp.dist_abs('a', '') == 1.0
    assert cmp.dist_abs('', 'a') == 1.0
    assert cmp.dist_abs('abc', '') == 3.0
    assert cmp.dist_abs('', 'abc') == 3.0
    assert cmp.dist_abs('abc', 'abc') == 0.0
    assert cmp.dist_abs('abcd', 'efgh') == 4.0

    assert cmp.dist_abs('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=2.0)
    assert cmp.dist_abs('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=1.2)
    assert cmp.dist_abs('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.4)
    assert cmp.dist_abs('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.4)
    assert cmp.dist_abs('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=3.6)

    assert cmp.dist_abs('hamming', 'hamstring') == pytest.approx(abs=1e-7, expected=3.4)
