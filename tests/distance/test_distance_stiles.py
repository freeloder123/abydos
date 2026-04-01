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

"""abydos.tests.distance.test_distance_stiles.

This module contains unit tests for abydos.distance.Stiles
"""


import pytest

from abydos.distance import Stiles


cmp = Stiles()

cmp_no_d = Stiles(alphabet=0)


def test_stiles_sim():
    """Test abydos.distance.Stiles.sim."""
    # Base cases
    assert cmp.sim('', '') == 1.0
    assert cmp.sim('a', '') == 0.760700314616495
    assert cmp.sim('', 'a') == 0.760700314616495
    assert cmp.sim('abc', '') == 0.7416916584588271
    assert cmp.sim('', 'abc') == 0.7416916584588271
    assert cmp.sim('abc', 'abc') == 1.0
    assert cmp.sim('abcd', 'efgh') == 0.4768516719017855

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.5744293838)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.5744293838)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.5744293838)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.5744293838)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.5909028826)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.sim('', '') == 1.0
    assert cmp_no_d.sim('a', '') == pytest.approx(abs=1e-7, expected=0.9511587063686434)
    assert cmp_no_d.sim('', 'a') == pytest.approx(abs=1e-7, expected=0.9511587063686434)
    assert cmp_no_d.sim('abc', '') == pytest.approx(abs=1e-7, expected=0.9309340273884292)
    assert cmp_no_d.sim('', 'abc') == pytest.approx(abs=1e-7, expected=0.9309340273884292)
    assert cmp_no_d.sim('abc', 'abc') == 1.0
    assert cmp_no_d.sim('abcd', 'efgh') == pytest.approx(abs=1e-7, expected=0.47481536969259386)

    assert cmp_no_d.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.5216609379)
    assert cmp_no_d.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.5216609379)
    assert cmp_no_d.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.5216609379)
    assert cmp_no_d.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.5216609379)
    assert cmp_no_d.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.5532905837)

def test_stiles_dist():
    """Test abydos.distance.Stiles.dist."""
    # Base cases
    assert cmp.dist('', '') == 0.0
    assert cmp.dist('a', '') == 0.239299685383505
    assert cmp.dist('', 'a') == 0.239299685383505
    assert cmp.dist('abc', '') == 0.2583083415411729
    assert cmp.dist('', 'abc') == 0.2583083415411729
    assert cmp.dist('abc', 'abc') == 0.0
    assert cmp.dist('abcd', 'efgh') == 0.5231483280982145

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.4255706162)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.4255706162)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.4255706162)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.4255706162)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.4090971174)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.dist('', '') == 0.0
    assert cmp_no_d.dist('a', '') == pytest.approx(abs=1e-7, expected=0.048841293631356586)
    assert cmp_no_d.dist('', 'a') == pytest.approx(abs=1e-7, expected=0.048841293631356586)
    assert cmp_no_d.dist('abc', '') == pytest.approx(abs=1e-7, expected=0.06906597261157077)
    assert cmp_no_d.dist('', 'abc') == pytest.approx(abs=1e-7, expected=0.06906597261157077)
    assert cmp_no_d.dist('abc', 'abc') == 0.0
    assert cmp_no_d.dist('abcd', 'efgh') == pytest.approx(abs=1e-7, expected=0.5251846303074061)

    assert cmp_no_d.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.4783390621)
    assert cmp_no_d.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.4783390621)
    assert cmp_no_d.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.4783390621)
    assert cmp_no_d.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.4783390621)
    assert cmp_no_d.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.4467094163)

def test_stiles_sim_score():
    """Test abydos.distance.Stiles.sim_score."""
    # Base cases
    assert cmp.sim_score('', '') == pytest.approx(abs=1e-7, expected=16.292255897915638)
    assert cmp.sim_score('a', '') == pytest.approx(abs=1e-7, expected=8.992335212208333)
    assert cmp.sim_score('', 'a') == pytest.approx(abs=1e-7, expected=8.992335212208333)
    assert cmp.sim_score('abc', '') == pytest.approx(abs=1e-7, expected=8.692417367356594)
    assert cmp.sim_score('', 'abc') == pytest.approx(abs=1e-7, expected=8.692417367356594)
    assert cmp.sim_score('abc', 'abc') == pytest.approx(abs=1e-7, expected=17.98245215160657)
    assert cmp.sim_score('abcd', 'efgh') == pytest.approx(abs=1e-7, expected=-0.8426334527850912)

    assert cmp.sim_score('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=2.7352860243)
    assert cmp.sim_score('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=2.7352860243)
    assert cmp.sim_score('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=2.7352860243)
    assert cmp.sim_score('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=2.7352860243)
    assert cmp.sim_score('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=3.4428002638)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.sim_score('', '') == pytest.approx(abs=1e-7, expected=13.647817481888637)
    assert cmp_no_d.sim_score('a', '') == pytest.approx(abs=1e-7, expected=13.22184890168726)
    assert cmp_no_d.sim_score('', 'a') == pytest.approx(abs=1e-7, expected=13.22184890168726)
    assert cmp_no_d.sim_score('abc', '') == pytest.approx(abs=1e-7, expected=13.522878821349728)
    assert cmp_no_d.sim_score('', 'abc') == pytest.approx(abs=1e-7, expected=13.522878821349728)
    assert cmp_no_d.sim_score('abc', 'abc') == pytest.approx(abs=1e-7, expected=15.69019612345796)
    assert cmp_no_d.sim_score('abcd', 'efgh') == pytest.approx(abs=1e-7, expected=-0.8061799153541304)

    assert cmp_no_d.sim_score('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.7043650362)
    assert cmp_no_d.sim_score('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.7043650362)
    assert cmp_no_d.sim_score('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.7043650362)
    assert cmp_no_d.sim_score('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.7043650362)
    assert cmp_no_d.sim_score('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=1.8208082871)

def test_stiles_corr():
    """Test abydos.distance.Stiles.corr."""
    # Base cases
    assert cmp.corr('', '') == 1.0
    assert cmp.corr('a', '') == pytest.approx(abs=1e-7, expected=0.5214006292329901)
    assert cmp.corr('', 'a') == pytest.approx(abs=1e-7, expected=0.5214006292329901)
    assert cmp.corr('abc', '') == pytest.approx(abs=1e-7, expected=0.48338331691765435)
    assert cmp.corr('', 'abc') == pytest.approx(abs=1e-7, expected=0.48338331691765435)
    assert cmp.corr('abc', 'abc') == 1.0
    assert cmp.corr('abcd', 'efgh') == pytest.approx(abs=1e-7, expected=-0.046296656196428934)

    assert cmp.corr('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.1488587676)
    assert cmp.corr('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.1488587676)
    assert cmp.corr('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.1488587676)
    assert cmp.corr('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.1488587676)
    assert cmp.corr('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.1818057652)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.corr('', '') == 1.0
    assert cmp_no_d.corr('a', '') == pytest.approx(abs=1e-7, expected=0.9023174127372868)
    assert cmp_no_d.corr('', 'a') == pytest.approx(abs=1e-7, expected=0.9023174127372868)
    assert cmp_no_d.corr('abc', '') == pytest.approx(abs=1e-7, expected=0.8618680547768583)
    assert cmp_no_d.corr('', 'abc') == pytest.approx(abs=1e-7, expected=0.8618680547768583)
    assert cmp_no_d.corr('abc', 'abc') == 1.0
    assert cmp_no_d.corr('abcd', 'efgh') == pytest.approx(abs=1e-7, expected=-0.05036926061481227)

    assert cmp_no_d.corr('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.0433218759)
    assert cmp_no_d.corr('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.0433218759)
    assert cmp_no_d.corr('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.0433218759)
    assert cmp_no_d.corr('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.0433218759)
    assert cmp_no_d.corr('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.1065811673)
