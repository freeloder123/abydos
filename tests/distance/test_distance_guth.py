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

"""abydos.tests.distance.test_distance_guth.

This module contains unit tests for abydos.distance.Guth
"""


import pytest

from abydos.distance import Guth


cmp = Guth()


def test_guth_sim_score():
    """Test abydos.distance.Guth.sim_score."""
    # Base cases
    assert cmp.sim_score('', '') == 1.0
    assert cmp.sim_score('a', '') == 0.0
    assert cmp.sim_score('', 'a') == 0.0
    assert cmp.sim_score('a', 'a') == 1.0
    assert cmp.sim_score('abc', '') == 0.0
    assert cmp.sim_score('', 'abc') == 0.0
    assert cmp.sim_score('abc', 'abc') == 1.0
    assert cmp.sim_score('abcd', 'efgh') == 0.0

    # Testcases from paper
    assert cmp.sim_score('Glawyn', 'Glavin') == 1.0
    assert cmp.sim_score('Smears', 'Smares') == 1.0
    assert cmp.sim_score('Giddings', 'Gittins') == 1.0
    assert cmp.sim_score('Bokenham', 'Buckingham') == 0.0

    # coverage
    assert Guth(qval=2).sim_score('Giddings', 'Gittins') == pytest.approx(abs=1e-7, expected=0.0)

def test_guth_sim():
    """Test abydos.distance.Guth.sim."""
    # Base cases
    assert cmp.sim('', '') == 1.0
    assert cmp.sim('a', '') == 0.0
    assert cmp.sim('', 'a') == 0.0
    assert cmp.sim('a', 'a') == 1.0
    assert cmp.sim('abc', '') == 0.0
    assert cmp.sim('', 'abc') == 0.0
    assert cmp.sim('abc', 'abc') == 1.0
    assert cmp.sim('abcd', 'efgh') == 0.0

    # Testcases from paper
    assert cmp.sim('Glawyn', 'Glavin') == pytest.approx(abs=1e-7, expected=0.8)
    assert cmp.sim('Smears', 'Smares') == pytest.approx(abs=1e-7, expected=0.86666666666)
    assert cmp.sim('Giddings', 'Gittins') == pytest.approx(abs=1e-7, expected=0.8)
    assert cmp.sim('Bokenham', 'Buckingham') == pytest.approx(abs=1e-7, expected=0.65)

    # coverage
    assert Guth(qval=2).sim('Giddings', 'Gittins') == pytest.approx(abs=1e-7, expected=0.6)
    assert cmp.sim('abcfefed', 'abcfed') == pytest.approx(abs=1e-7, expected=0.7)
