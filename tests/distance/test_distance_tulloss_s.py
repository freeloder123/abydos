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

"""abydos.tests.distance.test_distance_tulloss_s.

This module contains unit tests for abydos.distance.TullossS
"""


import pytest

from abydos.distance import TullossS


cmp = TullossS()


def test_tulloss_s_sim():
    """Test abydos.distance.TullossS.sim."""
    # Base cases
    assert cmp.sim('', '') == 1.0
    assert cmp.sim('a', '') == 1.0
    assert cmp.sim('', 'a') == 1.0
    assert cmp.sim('abc', '') == 1.0
    assert cmp.sim('', 'abc') == 1.0
    assert cmp.sim('abc', 'abc') == 1.0
    assert cmp.sim('abcd', 'efgh') == 0.5968309535438173

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.8277670301)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.8277670301)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.8277670301)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.8277670301)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.8951695896)

def test_tulloss_s_dist():
    """Test abydos.distance.TullossS.dist."""
    # Base cases
    assert cmp.dist('', '') == 0.0
    assert cmp.dist('a', '') == 0.0
    assert cmp.dist('', 'a') == 0.0
    assert cmp.dist('abc', '') == 0.0
    assert cmp.dist('', 'abc') == 0.0
    assert cmp.dist('abc', 'abc') == 0.0
    assert cmp.dist('abcd', 'efgh') == 0.4031690464561827

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.1722329699)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.1722329699)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.1722329699)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.1722329699)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.1048304104)
