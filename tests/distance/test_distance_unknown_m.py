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

"""abydos.tests.distance.test_distance_unknown_m.

This module contains unit tests for abydos.distance.UnknownM
"""


import pytest

from abydos.distance import UnknownM


cmp = UnknownM()

cmp_no_d = UnknownM(alphabet=0)


def test_unknown_m_sim():
    """Test abydos.distance.UnknownM.sim."""
    # Base cases
    assert cmp.sim('', '') == 0.0
    assert cmp.sim('a', '') == 0.14599478380307845
    assert cmp.sim('', 'a') == 0.14599478380307845
    assert cmp.sim('abc', '') == 0.24935979408619846
    assert cmp.sim('', 'abc') == 0.24935979408619846
    assert cmp.sim('abc', 'abc') == 0.8743589743589744
    assert cmp.sim('abcd', 'efgh') == 0.3993581514762516

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.6650599829)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.6650599829)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.6650599829)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.6650599829)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.7838816809)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.sim('', '') == 0.5
    assert cmp_no_d.sim('a', '') == 0.0
    assert cmp_no_d.sim('', 'a') == 0.0
    assert cmp_no_d.sim('abc', '') == 0.0
    assert cmp_no_d.sim('', 'abc') == 0.0
    assert cmp_no_d.sim('abc', 'abc') == 0.0
    assert cmp_no_d.sim('abcd', 'efgh') == 0.3

    assert cmp_no_d.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.25)
    assert cmp_no_d.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.25)
    assert cmp_no_d.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.25)
    assert cmp_no_d.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.25)
    assert cmp_no_d.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.3073313411)

def test_unknown_m_dist():
    """Test abydos.distance.UnknownM.dist."""
    # Base cases
    assert cmp.dist('', '') == 1.0
    assert cmp.dist('a', '') == 0.8540052161969216
    assert cmp.dist('', 'a') == 0.8540052161969216
    assert cmp.dist('abc', '') == 0.7506402059138015
    assert cmp.dist('', 'abc') == 0.7506402059138015
    assert cmp.dist('abc', 'abc') == 0.12564102564102564
    assert cmp.dist('abcd', 'efgh') == 0.6006418485237484

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.3349400171)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.3349400171)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.3349400171)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.3349400171)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.2161183191)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.dist('', '') == 0.5
    assert cmp_no_d.dist('a', '') == 1.0
    assert cmp_no_d.dist('', 'a') == 1.0
    assert cmp_no_d.dist('abc', '') == 1.0
    assert cmp_no_d.dist('', 'abc') == 1.0
    assert cmp_no_d.dist('abc', 'abc') == 1.0
    assert cmp_no_d.dist('abcd', 'efgh') == 0.7

    assert cmp_no_d.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.75)
    assert cmp_no_d.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.75)
    assert cmp_no_d.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.75)
    assert cmp_no_d.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.75)
    assert cmp_no_d.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.6926686589)

def test_unknown_m_sim_score():
    """Test abydos.distance.UnknownM.sim_score."""
    # Base cases
    assert cmp.sim_score('', '') == 1.0
    assert cmp.sim_score('a', '') == 0.7080104323938431
    assert cmp.sim_score('', 'a') == 0.7080104323938431
    assert cmp.sim_score('abc', '') == 0.5012804118276031
    assert cmp.sim_score('', 'abc') == 0.5012804118276031
    assert cmp.sim_score('abc', 'abc') == -0.7487179487179487
    assert cmp.sim_score('abcd', 'efgh') == 0.2012836970474968

    assert cmp.sim_score('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=-0.3301199657)
    assert cmp.sim_score('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=-0.3301199657)
    assert cmp.sim_score('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=-0.3301199657)
    assert cmp.sim_score('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=-0.3301199657)
    assert cmp.sim_score('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=-0.5677633618)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.sim_score('', '') == 0.0
    assert cmp_no_d.sim_score('a', '') == 1.0
    assert cmp_no_d.sim_score('', 'a') == 1.0
    assert cmp_no_d.sim_score('abc', '') == 1.0
    assert cmp_no_d.sim_score('', 'abc') == 1.0
    assert cmp_no_d.sim_score('abc', 'abc') == 1.0
    assert cmp_no_d.sim_score('abcd', 'efgh') == 0.4

    assert cmp_no_d.sim_score('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.5)
    assert cmp_no_d.sim_score('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.5)
    assert cmp_no_d.sim_score('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.5)
    assert cmp_no_d.sim_score('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.5)
    assert cmp_no_d.sim_score('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.3853373178)
