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

"""abydos.tests.distance.test_distance_gilbert_wells.

This module contains unit tests for abydos.distance.GilbertWells
"""


import pytest

from abydos.distance import GilbertWells


cmp = GilbertWells()

cmp_no_d = GilbertWells(alphabet=0)


def test_gilbert_wells_sim():
    """Test abydos.distance.GilbertWells.sim."""
    # Base cases
    assert cmp.sim('', '') == 1.0
    assert cmp.sim('a', '') == 0.0
    assert cmp.sim('', 'a') == 0.0
    assert cmp.sim('abc', '') == 0.0
    assert cmp.sim('', 'abc') == 0.0
    assert cmp.sim('abc', 'abc') == 1.0
    assert cmp.sim('abcd', 'efgh') == 0.028716013247135602

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.3776594411)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.3776594411)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.3776594411)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.3776594411)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.4950086952)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.sim('', '') == 1.0
    assert cmp_no_d.sim('a', '') == 0.0
    assert cmp_no_d.sim('', 'a') == 0.0
    assert cmp_no_d.sim('abc', '') == 0.0
    assert cmp_no_d.sim('', 'abc') == 0.0
    assert cmp_no_d.sim('abc', 'abc') == 1.0
    assert cmp_no_d.sim('abcd', 'efgh') == 0.13486136169765683

    assert cmp_no_d.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.0255856715)
    assert cmp_no_d.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.0255856715)
    assert cmp_no_d.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.0255856715)
    assert cmp_no_d.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.0255856715)
    assert cmp_no_d.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.0153237873)

def test_gilbert_wells_dist():
    """Test abydos.distance.GilbertWells.dist."""
    # Base cases
    assert cmp.dist('', '') == 0.0
    assert cmp.dist('a', '') == 1.0
    assert cmp.dist('', 'a') == 1.0
    assert cmp.dist('abc', '') == 1.0
    assert cmp.dist('', 'abc') == 1.0
    assert cmp.dist('abc', 'abc') == 0.0
    assert cmp.dist('abcd', 'efgh') == 0.9712839867528644

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.6223405589)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.6223405589)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.6223405589)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.6223405589)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.5049913048)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.dist('', '') == 0.0
    assert cmp_no_d.dist('a', '') == 1.0
    assert cmp_no_d.dist('', 'a') == 1.0
    assert cmp_no_d.dist('abc', '') == 1.0
    assert cmp_no_d.dist('', 'abc') == 1.0
    assert cmp_no_d.dist('abc', 'abc') == 0.0
    assert cmp_no_d.dist('abcd', 'efgh') == 0.8651386383023432

    assert cmp_no_d.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.9744143285)
    assert cmp_no_d.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.9744143285)
    assert cmp_no_d.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.9744143285)
    assert cmp_no_d.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.9744143285)
    assert cmp_no_d.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.9846762127)

def test_gilbert_wells_sim_score():
    """Test abydos.distance.GilbertWells.sim_score."""
    # Base cases
    assert cmp.sim_score('', '') == 76.91383873217538
    assert cmp.sim_score('a', '') == 40.179592442305186
    assert cmp.sim_score('', 'a') == 40.179592442305186
    assert cmp.sim_score('abc', '') == 39.4890060826051
    assert cmp.sim_score('', 'abc') == 39.4890060826051
    assert cmp.sim_score('abc', 'abc') == 49.00800898579118
    assert cmp.sim_score('abcd', 'efgh') == 1.6845961909440712

    assert cmp.sim_score('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=25.6938443303)
    assert cmp.sim_score('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=25.6938443303)
    assert cmp.sim_score('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=25.6938443303)
    assert cmp.sim_score('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=25.6938443303)
    assert cmp.sim_score('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=55.2085412384)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.sim_score('', '') == -36.04365338911715
    assert cmp_no_d.sim_score('a', '') == 70.9425768923849
    assert cmp_no_d.sim_score('', 'a') == 70.9425768923849
    assert cmp_no_d.sim_score('abc', '') == 71.63572407294485
    assert cmp_no_d.sim_score('', 'abc') == 71.63572407294485
    assert cmp_no_d.sim_score('abc', 'abc') == 71.63572407294485
    assert cmp_no_d.sim_score('abcd', 'efgh') == 9.690984737859244

    assert cmp_no_d.sim_score('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=1.8432222004)
    assert cmp_no_d.sim_score('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=1.8432222004)
    assert cmp_no_d.sim_score('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=1.8432222004)
    assert cmp_no_d.sim_score('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=1.8432222004)
    assert cmp_no_d.sim_score('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=1.1132321566)
