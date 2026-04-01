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

"""abydos.tests.distance.test_distance_yates_chi_squared.

This module contains unit tests for abydos.distance.YatesChiSquared
"""


import pytest

from abydos.distance import YatesChiSquared


cmp = YatesChiSquared()

cmp_no_d = YatesChiSquared(alphabet=0)

cmp_4q1 = YatesChiSquared(qval=1, alphabet=6)


def test_yates_chi_squared_sim():
    """Test abydos.distance.YatesChiSquared.sim."""
    # Base cases
    assert cmp.sim('', '') == 1.0
    assert cmp.sim('a', '') == 0.0
    assert cmp.sim('', 'a') == 0.0
    assert cmp.sim('abc', '') == 0.0
    assert cmp.sim('', 'abc') == 0.0
    assert cmp.sim('abc', 'abc') == 1.0
    assert cmp.sim('abcd', 'efgh') == 0.0

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.2024579068)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.2024579068)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.2024579068)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.2024579068)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.415132719)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.sim('', '') == 1.0
    assert cmp_no_d.sim('a', '') == 0.0
    assert cmp_no_d.sim('', 'a') == 0.0
    assert cmp_no_d.sim('abc', '') == 0.0
    assert cmp_no_d.sim('', 'abc') == 0.0
    assert cmp_no_d.sim('abc', 'abc') == 1.0
    assert cmp_no_d.sim('abcd', 'efgh') == 0.0

    assert cmp_no_d.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.0)
    assert cmp_no_d.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.0)
    assert cmp_no_d.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.0)
    assert cmp_no_d.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.0)
    assert cmp_no_d.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.0)

def test_yates_chi_squared_dist():
    """Test abydos.distance.YatesChiSquared.dist."""
    # Base cases
    assert cmp.dist('', '') == 0.0
    assert cmp.dist('a', '') == 1.0
    assert cmp.dist('', 'a') == 1.0
    assert cmp.dist('abc', '') == 1.0
    assert cmp.dist('', 'abc') == 1.0
    assert cmp.dist('abc', 'abc') == 0.0
    assert cmp.dist('abcd', 'efgh') == 1.0

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.7975420932)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.7975420932)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.7975420932)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.7975420932)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.584867281)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.dist('', '') == 0.0
    assert cmp_no_d.dist('a', '') == 1.0
    assert cmp_no_d.dist('', 'a') == 1.0
    assert cmp_no_d.dist('abc', '') == 1.0
    assert cmp_no_d.dist('', 'abc') == 1.0
    assert cmp_no_d.dist('abc', 'abc') == 0.0
    assert cmp_no_d.dist('abcd', 'efgh') == 1.0

    assert cmp_no_d.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=1.0)
    assert cmp_no_d.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=1.0)
    assert cmp_no_d.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=1.0)
    assert cmp_no_d.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=1.0)
    assert cmp_no_d.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=1.0)

def test_yates_chi_squared_sim_score():
    """Test abydos.distance.YatesChiSquared.sim_score."""
    # Base cases
    assert cmp.sim_score('', '') == 0.0
    assert cmp.sim_score('a', '') == 0.0
    assert cmp.sim_score('', 'a') == 0.0
    assert cmp.sim_score('abc', '') == 0.0
    assert cmp.sim_score('', 'abc') == 0.0
    assert cmp.sim_score('abc', 'abc') == 599.3708349769888
    assert cmp.sim_score('abcd', 'efgh') == 6.960385076156687

    assert cmp.sim_score('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=133.1878178031)
    assert cmp.sim_score('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=133.1878178031)
    assert cmp.sim_score('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=133.1878178031)
    assert cmp.sim_score('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=133.1878178031)
    assert cmp.sim_score('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=296.1470911771)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.sim_score('', '') == 0.0
    assert cmp_no_d.sim_score('a', '') == 0.0
    assert cmp_no_d.sim_score('', 'a') == 0.0
    assert cmp_no_d.sim_score('abc', '') == 0.0
    assert cmp_no_d.sim_score('', 'abc') == 0.0
    assert cmp_no_d.sim_score('abc', 'abc') == 1.0
    assert cmp_no_d.sim_score('abcd', 'efgh', signed=True) == -6.4

    assert cmp_no_d.sim_score('Nigel', 'Niall', signed=True) == pytest.approx(abs=1e-7, expected=-0.5625)
    assert cmp_no_d.sim_score('Niall', 'Nigel', signed=True) == pytest.approx(abs=1e-7, expected=-0.5625)
    assert cmp_no_d.sim_score('Colin', 'Coiln', signed=True) == pytest.approx(abs=1e-7, expected=-0.5625)
    assert cmp_no_d.sim_score('Coiln', 'Colin', signed=True) == pytest.approx(abs=1e-7, expected=-0.5625)
    assert cmp_no_d.sim_score('ATCAACGAGT', 'AACGATTAG', signed=True) == pytest.approx(abs=1e-7, expected=-0.2651515152)

    assert cmp_4q1.sim_score('tab', 'tac') == 0.0
