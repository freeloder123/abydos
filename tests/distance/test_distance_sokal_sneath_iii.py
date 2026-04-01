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

"""abydos.tests.distance.test_distance_sokal_sneath_iii.

This module contains unit tests for abydos.distance.SokalSneathIII
"""


import pytest

from abydos.distance import SokalSneathIII


cmp = SokalSneathIII()


def test_sokal_sneath_iii_sim_score():
    """Test abydos.distance.SokalSneathIII.sim_score."""
    # Base cases
    assert cmp.sim_score('', '') == float('inf')
    assert cmp.sim_score('a', '') == 391.0
    assert cmp.sim_score('', 'a') == 391.0
    assert cmp.sim_score('abc', '') == 195.0
    assert cmp.sim_score('', 'abc') == 195.0
    assert cmp.sim_score('abc', 'abc') == float('inf')
    assert cmp.sim_score('abcd', 'efgh') == 77.4

    assert cmp.sim_score('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=129.6666666667)
    assert cmp.sim_score('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=129.6666666667)
    assert cmp.sim_score('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=129.6666666667)
    assert cmp.sim_score('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=129.6666666667)
    assert cmp.sim_score('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=111.0)
    assert cmp.sim_score('Kirisits', 'Kiritsis') == float('inf')

def test_sokal_sneath_iii_dist():
    """Test abydos.distance.SokalSneathIII.dist."""
    with pytest.raises(NotImplementedError):
        cmp.dist()

def test_sokal_sneath_iii_sim():
    """Test abydos.distance.SokalSneathIII.sim."""
    with pytest.raises(NotImplementedError):
        cmp.sim()
