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

"""abydos.tests.distance.test_distance_kuhns_viii.

This module contains unit tests for abydos.distance.KuhnsVIII
"""


import pytest

from abydos.distance import KuhnsVIII


cmp = KuhnsVIII()

cmp_no_d = KuhnsVIII(alphabet=0)


def test_kuhns_viii_sim():
    """Test abydos.distance.KuhnsVIII.sim."""
    # Base cases
    assert cmp.sim('', '') == 0.3333333333333333
    assert cmp.sim('a', '') == 0.3333333333333333
    assert cmp.sim('', 'a') == 0.3333333333333333
    assert cmp.sim('abc', '') == 0.3333333333333333
    assert cmp.sim('', 'abc') == 0.3333333333333333
    assert cmp.sim('abc', 'abc') == 0.9965986394557823
    assert cmp.sim('abcd', 'efgh') == 0.32908163265306123

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.6615646259)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.6615646259)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.6615646259)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.6615646259)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.7688694525)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.sim('', '') == 0.3333333333333333
    assert cmp_no_d.sim('a', '') == 0.3333333333333333
    assert cmp_no_d.sim('', 'a') == 0.3333333333333333
    assert cmp_no_d.sim('abc', '') == 0.3333333333333333
    assert cmp_no_d.sim('', 'abc') == 0.3333333333333333
    assert cmp_no_d.sim('abc', 'abc') == 0.3333333333333333
    assert cmp_no_d.sim('abcd', 'efgh') == 0.0

    assert cmp_no_d.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.2222222222)
    assert cmp_no_d.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.2222222222)
    assert cmp_no_d.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.2222222222)
    assert cmp_no_d.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.2222222222)
    assert cmp_no_d.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.2789115646)

def test_kuhns_viii_dist():
    """Test abydos.distance.KuhnsVIII.dist."""
    # Base cases
    assert cmp.dist('', '') == 0.6666666666666667
    assert cmp.dist('a', '') == 0.6666666666666667
    assert cmp.dist('', 'a') == 0.6666666666666667
    assert cmp.dist('abc', '') == 0.6666666666666667
    assert cmp.dist('', 'abc') == 0.6666666666666667
    assert cmp.dist('abc', 'abc') == 0.003401360544217691
    assert cmp.dist('abcd', 'efgh') == 0.6709183673469388

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.3384353741)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.3384353741)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.3384353741)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.3384353741)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.2311305475)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.dist('', '') == 0.6666666666666667
    assert cmp_no_d.dist('a', '') == 0.6666666666666667
    assert cmp_no_d.dist('', 'a') == 0.6666666666666667
    assert cmp_no_d.dist('abc', '') == 0.6666666666666667
    assert cmp_no_d.dist('', 'abc') == 0.6666666666666667
    assert cmp_no_d.dist('abc', 'abc') == 0.6666666666666667
    assert cmp_no_d.dist('abcd', 'efgh') == 1.0

    assert cmp_no_d.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.7777777778)
    assert cmp_no_d.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.7777777778)
    assert cmp_no_d.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.7777777778)
    assert cmp_no_d.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.7777777778)
    assert cmp_no_d.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.7210884354)

def test_kuhns_viii_corr():
    """Test abydos.distance.KuhnsVIII.corr."""
    # Base cases
    assert cmp.corr('', '') == 0.0
    assert cmp.corr('a', '') == 0.0
    assert cmp.corr('', 'a') == 0.0
    assert cmp.corr('abc', '') == 0.0
    assert cmp.corr('', 'abc') == 0.0
    assert cmp.corr('abc', 'abc') == 0.9948979591836735
    assert cmp.corr('abcd', 'efgh') == -0.006377551020408163

    assert cmp.corr('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.4923469388)
    assert cmp.corr('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.4923469388)
    assert cmp.corr('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.4923469388)
    assert cmp.corr('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.4923469388)
    assert cmp.corr('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.6533041788)

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
    assert cmp_no_d.corr('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=-0.0816326531)
