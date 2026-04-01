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

"""abydos.tests.distance.test_distance_morisita.

This module contains unit tests for abydos.distance.Morisita
"""


import pytest

from abydos.distance import Morisita


cmp = Morisita()


def test_morisita_sim_score():
    """Test abydos.distance.Morisita.sim_score."""
    # Base cases
    assert cmp.sim_score('', '') == 0.0
    assert cmp.sim_score('a', '') == 0.0
    assert cmp.sim_score('', 'a') == 0.0
    assert cmp.sim_score('a', 'a') == 1.0
    assert cmp.sim_score('abc', '') == 0.0
    assert cmp.sim_score('', 'abc') == 0.0
    assert cmp.sim_score('abc', 'abc') == 0.5
    assert cmp.sim_score('abcd', 'efgh') == 0.0

    assert cmp.sim_score('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.1666666666)
    assert cmp.sim_score('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.1666666666)
    assert cmp.sim_score('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.1666666666)
    assert cmp.sim_score('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.1666666666)
    assert cmp.sim_score('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.12727272727)

    assert cmp.sim_score('sadklsalkdhsa', 'slksajdlkasj') == pytest.approx(abs=1e-7, expected=1.44)

def test_morisita_dist():
    """Test abydos.distance.Morisita.dist."""
    with pytest.raises(NotImplementedError):
        cmp.dist()

def test_morisita_sim():
    """Test abydos.distance.Morisita.sim."""
    with pytest.raises(NotImplementedError):
        cmp.sim()
