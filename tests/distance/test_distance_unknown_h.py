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

"""abydos.tests.distance.test_distance_unknown_h.

This module contains unit tests for abydos.distance.UnknownH
"""


import pytest

from abydos.distance import UnknownH


cmp = UnknownH()

cmp_no_d = UnknownH(alphabet=0)


def test_unknown_h_sim():
    """Test abydos.distance.UnknownH.sim."""
    # Base cases
    assert cmp.sim('', '') == 0.0
    assert cmp.sim('a', '') == 0.0
    assert cmp.sim('', 'a') == 0.0
    assert cmp.sim('abc', '') == 0.0
    assert cmp.sim('', 'abc') == 0.0
    assert cmp.sim('abc', 'abc') == 0.75
    assert cmp.sim('abcd', 'efgh') == 0.0

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.2958758548)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.2958758548)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.2958758548)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.2958758548)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.5093099295)

def test_unknown_h_dist():
    """Test abydos.distance.UnknownH.dist."""
    # Base cases
    assert cmp.dist('', '') == 1.0
    assert cmp.dist('a', '') == 1.0
    assert cmp.dist('', 'a') == 1.0
    assert cmp.dist('abc', '') == 1.0
    assert cmp.dist('', 'abc') == 1.0
    assert cmp.dist('abc', 'abc') == 0.25
    assert cmp.dist('abcd', 'efgh') == 1.0

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.7041241452)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.7041241452)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.7041241452)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.7041241452)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.4906900705)

def test_unknown_h_sim_score():
    """Test abydos.distance.UnknownH.sim_score."""
    # Base cases
    assert cmp.sim_score('', '') == 0.0
    assert cmp.sim_score('a', '') == 0.0
    assert cmp.sim_score('', 'a') == 0.0
    assert cmp.sim_score('abc', '') == 0.0
    assert cmp.sim_score('', 'abc') == 0.0
    assert cmp.sim_score('abc', 'abc') == 0.75
    assert cmp.sim_score('abcd', 'efgh') == -0.22360679774997896

    assert cmp.sim_score('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.2958758548)
    assert cmp.sim_score('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.2958758548)
    assert cmp.sim_score('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.2958758548)
    assert cmp.sim_score('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.2958758548)
    assert cmp.sim_score('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.5093099295)
