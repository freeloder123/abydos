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

"""abydos.tests.distance.test_distance_hellinger.

This module contains unit tests for abydos.distance.Hellinger
"""


import pytest

from abydos.distance import Hellinger


cmp = Hellinger()


def test_hellinger_dist():
    """Test abydos.distance.Hellinger.dist."""
    # Base cases
    assert cmp.dist('', '') == 0.0
    assert cmp.dist('a', '') == 1.0
    assert cmp.dist('', 'a') == 1.0
    assert cmp.dist('abc', '') == 1.0
    assert cmp.dist('', 'abc') == 1.0
    assert cmp.dist('abc', 'abc') == 0.0
    assert cmp.dist('abcd', 'efgh') == 1.0

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.8164965809)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.8164965809)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.8164965809)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.8164965809)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.7071067812)

def test_hellinger_sim():
    """Test abydos.distance.Hellinger.sim."""
    # Base cases
    assert cmp.sim('', '') == 1.0
    assert cmp.sim('a', '') == 0.0
    assert cmp.sim('', 'a') == 0.0
    assert cmp.sim('abc', '') == 0.0
    assert cmp.sim('', 'abc') == 0.0
    assert cmp.sim('abc', 'abc') == 1.0
    assert cmp.sim('abcd', 'efgh') == 0.0

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.1835034191)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.1835034191)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.1835034191)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.1835034191)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.2928932188)

def test_hellinger_dist_abs():
    """Test abydos.distance.Hellinger.dist_abs."""
    # Base cases
    assert cmp.dist_abs('', '') == 0.0
    assert cmp.dist_abs('a', '') == 2.0
    assert cmp.dist_abs('', 'a') == 2.0
    assert cmp.dist_abs('abc', '') == 2.8284271247461903
    assert cmp.dist_abs('', 'abc') == 2.8284271247461903
    assert cmp.dist_abs('abc', 'abc') == 0.0
    assert cmp.dist_abs('abcd', 'efgh') == 4.47213595499958

    assert cmp.dist_abs('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=3.4641016151)
    assert cmp.dist_abs('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=3.4641016151)
    assert cmp.dist_abs('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=3.4641016151)
    assert cmp.dist_abs('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=3.4641016151)
    assert cmp.dist_abs('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=3.7416573868)
