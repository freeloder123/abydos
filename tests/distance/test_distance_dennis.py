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

"""abydos.tests.distance.test_distance_dennis.

This module contains unit tests for abydos.distance.Dennis
"""


import pytest

from abydos.distance import Dennis


cmp = Dennis()

cmp_no_d = Dennis(alphabet=0)


def test_dennis_sim():
    """Test abydos.distance.Dennis.sim."""
    # Base cases
    assert cmp.sim('', '') == pytest.approx(abs=1e-7, expected=0.3333333333333333)
    assert cmp.sim('a', '') == pytest.approx(abs=1e-7, expected=0.3333333333333333)
    assert cmp.sim('', 'a') == pytest.approx(abs=1e-7, expected=0.3333333333333333)
    assert cmp.sim('abc', '') == pytest.approx(abs=1e-7, expected=0.3333333333333333)
    assert cmp.sim('', 'abc') == pytest.approx(abs=1e-7, expected=0.3333333333333333)
    assert cmp.sim('abc', 'abc') == pytest.approx(abs=1e-7, expected=0.9965986394557826)
    assert cmp.sim('abcd', 'efgh') == pytest.approx(abs=1e-7, expected=0.32908163265306134)

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.6615646259)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.6615646259)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.6615646259)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.6615646259)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.7693640991)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.sim('', '') == pytest.approx(abs=1e-7, expected=0.3333333333333333)
    assert cmp_no_d.sim('a', '') == pytest.approx(abs=1e-7, expected=0.3333333333333333)
    assert cmp_no_d.sim('', 'a') == pytest.approx(abs=1e-7, expected=0.3333333333333333)
    assert cmp_no_d.sim('abc', '') == pytest.approx(abs=1e-7, expected=0.3333333333333333)
    assert cmp_no_d.sim('', 'abc') == pytest.approx(abs=1e-7, expected=0.3333333333333333)
    assert cmp_no_d.sim('abc', 'abc') == pytest.approx(abs=1e-7, expected=0.3333333333333333)
    assert cmp_no_d.sim('abcd', 'efgh') == pytest.approx(abs=1e-7, expected=0.0)

    assert cmp_no_d.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.2222222222)
    assert cmp_no_d.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.2222222222)
    assert cmp_no_d.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.2222222222)
    assert cmp_no_d.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.2222222222)
    assert cmp_no_d.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.2788497568)

def test_dennis_dist():
    """Test abydos.distance.Dennis.dist."""
    # Base cases
    assert cmp.dist('', '') == pytest.approx(abs=1e-7, expected=0.6666666666666667)
    assert cmp.dist('a', '') == pytest.approx(abs=1e-7, expected=0.6666666666666667)
    assert cmp.dist('', 'a') == pytest.approx(abs=1e-7, expected=0.6666666666666667)
    assert cmp.dist('abc', '') == pytest.approx(abs=1e-7, expected=0.6666666666666667)
    assert cmp.dist('', 'abc') == pytest.approx(abs=1e-7, expected=0.6666666666666667)
    assert cmp.dist('abc', 'abc') == pytest.approx(abs=1e-7, expected=0.003401360544217358)
    assert cmp.dist('abcd', 'efgh') == pytest.approx(abs=1e-7, expected=0.6709183673469387)

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.3384353741)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.3384353741)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.3384353741)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.3384353741)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.2306359009)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.dist('', '') == pytest.approx(abs=1e-7, expected=0.6666666666666667)
    assert cmp_no_d.dist('a', '') == pytest.approx(abs=1e-7, expected=0.6666666666666667)
    assert cmp_no_d.dist('', 'a') == pytest.approx(abs=1e-7, expected=0.6666666666666667)
    assert cmp_no_d.dist('abc', '') == pytest.approx(abs=1e-7, expected=0.6666666666666667)
    assert cmp_no_d.dist('', 'abc') == pytest.approx(abs=1e-7, expected=0.6666666666666667)
    assert cmp_no_d.dist('abc', 'abc') == pytest.approx(abs=1e-7, expected=0.6666666666666667)
    assert cmp_no_d.dist('abcd', 'efgh') == pytest.approx(abs=1e-7, expected=1.0)

    assert cmp_no_d.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.7777777778)
    assert cmp_no_d.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.7777777778)
    assert cmp_no_d.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.7777777778)
    assert cmp_no_d.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.7777777778)
    assert cmp_no_d.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.7211502432)

def test_dennis_sim_score():
    """Test abydos.distance.Dennis.sim_score."""
    # Base cases
    assert cmp.sim_score('', '') == 0.0
    assert cmp.sim_score('a', '') == 0.0
    assert cmp.sim_score('', 'a') == 0.0
    assert cmp.sim_score('abc', '') == 0.0
    assert cmp.sim_score('', 'abc') == 0.0
    assert cmp.sim_score('abc', 'abc') == pytest.approx(abs=1e-7, expected=27.85714285714286)
    assert cmp.sim_score('abcd', 'efgh') == pytest.approx(abs=1e-7, expected=-0.17857142857142858)

    assert cmp.sim_score('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=13.7857142857)
    assert cmp.sim_score('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=13.7857142857)
    assert cmp.sim_score('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=13.7857142857)
    assert cmp.sim_score('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=13.7857142857)
    assert cmp.sim_score('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=18.3132921606)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.sim_score('', '') == 0.0
    assert cmp_no_d.sim_score('a', '') == 0.0
    assert cmp_no_d.sim_score('', 'a') == 0.0
    assert cmp_no_d.sim_score('abc', '') == 0.0
    assert cmp_no_d.sim_score('', 'abc') == 0.0
    assert cmp_no_d.sim_score('abc', 'abc') == 0.0
    assert cmp_no_d.sim_score('abcd', 'efgh') == pytest.approx(abs=1e-7, expected=-1.5811388300841895)

    assert cmp_no_d.sim_score('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=-0.5)
    assert cmp_no_d.sim_score('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=-0.5)
    assert cmp_no_d.sim_score('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=-0.5)
    assert cmp_no_d.sim_score('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=-0.5)
    assert cmp_no_d.sim_score('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=-0.3057883149)

def test_dennis_corr():
    """Test abydos.distance.Dennis.corr."""
    # Base cases
    assert cmp.corr('', '') == 0.0
    assert cmp.corr('a', '') == 0.0
    assert cmp.corr('', 'a') == 0.0
    assert cmp.corr('abc', '') == 0.0
    assert cmp.corr('', 'abc') == 0.0
    assert cmp.corr('abc', 'abc') == pytest.approx(abs=1e-7, expected=0.994897959183674)
    assert cmp.corr('abcd', 'efgh') == pytest.approx(abs=1e-7, expected=-0.006377551020408)

    assert cmp.corr('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.4923469388)
    assert cmp.corr('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.4923469388)
    assert cmp.corr('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.4923469388)
    assert cmp.corr('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.4923469388)
    assert cmp.corr('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.6540461486)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.corr('', '') == 0.0
    assert cmp_no_d.corr('a', '') == 0.0
    assert cmp_no_d.corr('', 'a') == 0.0
    assert cmp_no_d.corr('abc', '') == 0.0
    assert cmp_no_d.corr('', 'abc') == 0.0
    assert cmp_no_d.corr('abc', 'abc') == 0.0
    assert cmp_no_d.corr('abcd', 'efgh') == -0.5

    assert cmp_no_d.corr('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=-0.1666666667)
    assert cmp_no_d.corr('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=-0.1666666667)
    assert cmp_no_d.corr('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=-0.1666666667)
    assert cmp_no_d.corr('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=-0.1666666667)
    assert cmp_no_d.corr('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=-0.0817253648)
