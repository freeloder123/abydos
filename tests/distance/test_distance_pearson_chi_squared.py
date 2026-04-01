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

"""abydos.tests.distance.test_distance_pearson_chi_squared.

This module contains unit tests for abydos.distance.PearsonChiSquared
"""


import pytest

from abydos.distance import PearsonChiSquared


cmp = PearsonChiSquared()

cmp_no_d = PearsonChiSquared(alphabet=0)


def test_pearson_chi_squared_sim():
    """Test abydos.distance.PearsonChiSquared.sim."""
    # Base cases
    assert cmp.sim('', '') == 1.0
    assert cmp.sim('a', '') == 0.5
    assert cmp.sim('', 'a') == 0.5
    assert cmp.sim('abc', '') == 0.5
    assert cmp.sim('', 'abc') == 0.5
    assert cmp.sim('abc', 'abc') == 1.0
    assert cmp.sim('abcd', 'efgh') == 0.4999794015236281

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.623079414)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.623079414)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.623079414)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.623079414)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.7197346065)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.sim('', '') == 1.0
    assert cmp_no_d.sim('a', '') == 0.5
    assert cmp_no_d.sim('', 'a') == 0.5
    assert cmp_no_d.sim('abc', '') == 0.5
    assert cmp_no_d.sim('', 'abc') == 0.5
    assert cmp_no_d.sim('abc', 'abc') == 1.0
    assert cmp_no_d.sim('abcd', 'efgh') == 0.0

    assert cmp_no_d.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.375)
    assert cmp_no_d.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.375)
    assert cmp_no_d.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.375)
    assert cmp_no_d.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.375)
    assert cmp_no_d.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.4454545455)

def test_pearson_chi_squared_dist():
    """Test abydos.distance.PearsonChiSquared.dist."""
    # Base cases
    assert cmp.dist('', '') == 0.0
    assert cmp.dist('a', '') == 0.5
    assert cmp.dist('', 'a') == 0.5
    assert cmp.dist('abc', '') == 0.5
    assert cmp.dist('', 'abc') == 0.5
    assert cmp.dist('abc', 'abc') == 0.0
    assert cmp.dist('abcd', 'efgh') == 0.5000205984763719

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.376920586)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.376920586)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.376920586)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.376920586)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.2802653935)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.dist('', '') == 0.0
    assert cmp_no_d.dist('a', '') == 0.5
    assert cmp_no_d.dist('', 'a') == 0.5
    assert cmp_no_d.dist('abc', '') == 0.5
    assert cmp_no_d.dist('', 'abc') == 0.5
    assert cmp_no_d.dist('abc', 'abc') == 0.0
    assert cmp_no_d.dist('abcd', 'efgh') == 1.0

    assert cmp_no_d.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.625)
    assert cmp_no_d.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.625)
    assert cmp_no_d.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.625)
    assert cmp_no_d.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.625)
    assert cmp_no_d.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.5545454545)

def test_pearson_chi_squared_sim_score():
    """Test abydos.distance.PearsonChiSquared.sim_score."""
    # Base cases
    assert cmp.sim_score('', '') == 784.0
    assert cmp.sim_score('a', '') == 0.0
    assert cmp.sim_score('', 'a') == 0.0
    assert cmp.sim_score('abc', '') == 0.0
    assert cmp.sim_score('', 'abc') == 0.0
    assert cmp.sim_score('abc', 'abc') == 784.0
    assert cmp.sim_score('abcd', 'efgh') == 0.032298410951138765

    assert cmp.sim_score('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=192.9885210909)
    assert cmp.sim_score('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=192.9885210909)
    assert cmp.sim_score('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=192.9885210909)
    assert cmp.sim_score('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=192.9885210909)
    assert cmp.sim_score('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=344.5438630111)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.sim_score('', '') == 0.0
    assert cmp_no_d.sim_score('a', '') == 0.0
    assert cmp_no_d.sim_score('', 'a') == 0.0
    assert cmp_no_d.sim_score('abc', '') == 0.0
    assert cmp_no_d.sim_score('', 'abc') == 0.0
    assert cmp_no_d.sim_score('abc', 'abc') == 4.0
    assert cmp_no_d.sim_score('abcd', 'efgh') == 10.0

    assert cmp_no_d.sim_score('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=2.25)
    assert cmp_no_d.sim_score('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=2.25)
    assert cmp_no_d.sim_score('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=2.25)
    assert cmp_no_d.sim_score('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=2.25)
    assert cmp_no_d.sim_score('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=1.5272727273)

def test_pearson_chi_squared_corr():
    """Test abydos.distance.PearsonChiSquared.corr."""
    # Base cases
    assert cmp.corr('', '') == 1.0
    assert cmp.corr('a', '') == 0.0
    assert cmp.corr('', 'a') == 0.0
    assert cmp.corr('abc', '') == 0.0
    assert cmp.corr('', 'abc') == 0.0
    assert cmp.corr('abc', 'abc') == 1.0
    assert cmp.corr('abcd', 'efgh') == -4.1196952743799446e-05

    assert cmp.corr('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.2461588279)
    assert cmp.corr('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.2461588279)
    assert cmp.corr('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.2461588279)
    assert cmp.corr('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.2461588279)
    assert cmp.corr('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.439469213)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.corr('', '') == 1.0
    assert cmp_no_d.corr('a', '') == 0.0
    assert cmp_no_d.corr('', 'a') == 0.0
    assert cmp_no_d.corr('abc', '') == 0.0
    assert cmp_no_d.corr('', 'abc') == 0.0
    assert cmp_no_d.corr('abc', 'abc') == 1.0
    assert cmp_no_d.corr('abcd', 'efgh') == -1.0

    assert cmp_no_d.corr('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=-0.25)
    assert cmp_no_d.corr('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=-0.25)
    assert cmp_no_d.corr('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=-0.25)
    assert cmp_no_d.corr('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=-0.25)
    assert cmp_no_d.corr('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=-0.1090909091)
