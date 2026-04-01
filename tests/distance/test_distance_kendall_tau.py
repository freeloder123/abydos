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

"""abydos.tests.distance.test_distance_kendall_tau.

This module contains unit tests for abydos.distance.KendallTau
"""


import pytest

from abydos.distance import KendallTau


cmp = KendallTau()

cmp_no_d = KendallTau(alphabet=0)


def test_kendall_tau_sim():
    """Test abydos.distance.KendallTau.sim."""
    # Base cases
    assert cmp.sim('', '') == 0.5012771392081737
    assert cmp.sim('a', '') == 0.5012706231918055
    assert cmp.sim('', 'a') == 0.5012706231918055
    assert cmp.sim('abc', '') == 0.5012641071754372
    assert cmp.sim('', 'abc') == 0.5012641071754372
    assert cmp.sim('abc', 'abc') == 0.5012771392081737
    assert cmp.sim('abcd', 'efgh') == 0.5012445591263325

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.5012575912)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.5012575912)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.5012575912)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.5012575912)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.5012543332)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.sim('', '') == 0.5
    assert cmp_no_d.sim('a', '') == 0.0
    assert cmp_no_d.sim('', 'a') == 0.0
    assert cmp_no_d.sim('abc', '') == 0.16666666666666669
    assert cmp_no_d.sim('', 'abc') == 0.16666666666666669
    assert cmp_no_d.sim('abc', 'abc') == 0.8333333333333333
    assert cmp_no_d.sim('abcd', 'efgh') == 0.3888888888888889

    assert cmp_no_d.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.4583333333)
    assert cmp_no_d.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.4583333333)
    assert cmp_no_d.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.4583333333)
    assert cmp_no_d.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.4583333333)
    assert cmp_no_d.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.5)

def test_kendall_tau_dist():
    """Test abydos.distance.KendallTau.dist."""
    # Base cases
    assert cmp.dist('', '') == 0.49872286079182626
    assert cmp.dist('a', '') == 0.4987293768081945
    assert cmp.dist('', 'a') == 0.4987293768081945
    assert cmp.dist('abc', '') == 0.49873589282456277
    assert cmp.dist('', 'abc') == 0.49873589282456277
    assert cmp.dist('abc', 'abc') == 0.49872286079182626
    assert cmp.dist('abcd', 'efgh') == 0.4987554408736675

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.4987424088)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.4987424088)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.4987424088)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.4987424088)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.4987456668)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.dist('', '') == 0.5
    assert cmp_no_d.dist('a', '') == 1.0
    assert cmp_no_d.dist('', 'a') == 1.0
    assert cmp_no_d.dist('abc', '') == 0.8333333333333333
    assert cmp_no_d.dist('', 'abc') == 0.8333333333333333
    assert cmp_no_d.dist('abc', 'abc') == 0.16666666666666674
    assert cmp_no_d.dist('abcd', 'efgh') == 0.6111111111111112

    assert cmp_no_d.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.5416666667)
    assert cmp_no_d.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.5416666667)
    assert cmp_no_d.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.5416666667)
    assert cmp_no_d.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.5416666667)
    assert cmp_no_d.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.5)

def test_kendall_tau_corr():
    """Test abydos.distance.KendallTau.corr."""
    # Base cases
    assert cmp.corr('', '') == 0.002554278416347382
    assert cmp.corr('a', '') == 0.0025412463836109156
    assert cmp.corr('', 'a') == 0.0025412463836109156
    assert cmp.corr('abc', '') == 0.0025282143508744493
    assert cmp.corr('', 'abc') == 0.0025282143508744493
    assert cmp.corr('abc', 'abc') == 0.002554278416347382
    assert cmp.corr('abcd', 'efgh') == 0.0024891182526650506

    assert cmp.corr('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.0025151823)
    assert cmp.corr('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.0025151823)
    assert cmp.corr('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.0025151823)
    assert cmp.corr('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.0025151823)
    assert cmp.corr('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.0025086663)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.corr('', '') == 0.0
    assert cmp_no_d.corr('a', '') == -2.0
    assert cmp_no_d.corr('', 'a') == -2.0
    assert cmp_no_d.corr('abc', '') == -0.6666666666666666
    assert cmp_no_d.corr('', 'abc') == -0.6666666666666666
    assert cmp_no_d.corr('abc', 'abc') == 0.6666666666666666
    assert cmp_no_d.corr('abcd', 'efgh') == -0.2222222222222222

    assert cmp_no_d.corr('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=-0.0833333333)
    assert cmp_no_d.corr('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=-0.0833333333)
    assert cmp_no_d.corr('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=-0.0833333333)
    assert cmp_no_d.corr('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=-0.0833333333)
    assert cmp_no_d.corr('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.0)
