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

"""abydos.tests.distance.test_distance_kuhns_iii.

This module contains unit tests for abydos.distance.KuhnsIII
"""


import pytest

from abydos.distance import KuhnsIII


cmp = KuhnsIII()

cmp_no_d = KuhnsIII(alphabet=0)


def test_kuhns_iii_sim():
    """Test abydos.distance.KuhnsIII.sim."""
    # Base cases
    assert cmp.sim('', '') == 0.25
    assert cmp.sim('a', '') == 0.25
    assert cmp.sim('', 'a') == 0.25
    assert cmp.sim('abc', '') == 0.25
    assert cmp.sim('', 'abc') == 0.25
    assert cmp.sim('abc', 'abc') == 0.9980818414322251
    assert cmp.sim('abcd', 'efgh') == 0.24760076775431863

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.4971190781)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.4971190781)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.4971190781)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.4971190781)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.6199553626)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.sim('', '') == 0.25
    assert cmp_no_d.sim('a', '') == 0.25
    assert cmp_no_d.sim('', 'a') == 0.25
    assert cmp_no_d.sim('abc', '') == 0.25
    assert cmp_no_d.sim('', 'abc') == 0.25
    assert cmp_no_d.sim('abc', 'abc') == 0.25
    assert cmp_no_d.sim('abcd', 'efgh') == 0.0

    assert cmp_no_d.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.125)
    assert cmp_no_d.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.125)
    assert cmp_no_d.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.125)
    assert cmp_no_d.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.125)
    assert cmp_no_d.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.1766304348)

def test_kuhns_iii_dist():
    """Test abydos.distance.KuhnsIII.dist."""
    # Base cases
    assert cmp.dist('', '') == 0.75
    assert cmp.dist('a', '') == 0.75
    assert cmp.dist('', 'a') == 0.75
    assert cmp.dist('abc', '') == 0.75
    assert cmp.dist('', 'abc') == 0.75
    assert cmp.dist('abc', 'abc') == 0.0019181585677748858
    assert cmp.dist('abcd', 'efgh') == 0.7523992322456814

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.5028809219)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.5028809219)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.5028809219)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.5028809219)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.3800446374)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.dist('', '') == 0.75
    assert cmp_no_d.dist('a', '') == 0.75
    assert cmp_no_d.dist('', 'a') == 0.75
    assert cmp_no_d.dist('abc', '') == 0.75
    assert cmp_no_d.dist('', 'abc') == 0.75
    assert cmp_no_d.dist('abc', 'abc') == 0.75
    assert cmp_no_d.dist('abcd', 'efgh') == 1.0

    assert cmp_no_d.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.875)
    assert cmp_no_d.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.875)
    assert cmp_no_d.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.875)
    assert cmp_no_d.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.875)
    assert cmp_no_d.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.8233695652)

def test_kuhns_iii_corr():
    """Test abydos.distance.KuhnsIII.corr."""
    # Base cases
    assert cmp.corr('', '') == 0.0
    assert cmp.corr('a', '') == 0.0
    assert cmp.corr('', 'a') == 0.0
    assert cmp.corr('abc', '') == 0.0
    assert cmp.corr('', 'abc') == 0.0
    assert cmp.corr('abc', 'abc') == 0.9974424552429668
    assert cmp.corr('abcd', 'efgh') == -0.003198976327575176

    assert cmp.corr('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.3294921041)
    assert cmp.corr('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.3294921041)
    assert cmp.corr('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.3294921041)
    assert cmp.corr('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.3294921041)
    assert cmp.corr('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.4932738168)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.corr('', '') == 0.0
    assert cmp_no_d.corr('a', '') == 0.0
    assert cmp_no_d.corr('', 'a') == 0.0
    assert cmp_no_d.corr('abc', '') == 0.0
    assert cmp_no_d.corr('', 'abc') == 0.0
    assert cmp_no_d.corr('abc', 'abc') == 0.0
    assert cmp_no_d.corr('abcd', 'efgh') == -0.3333333333333333

    assert cmp_no_d.corr('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=-0.1666666667)
    assert cmp_no_d.corr('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=-0.1666666667)
    assert cmp_no_d.corr('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=-0.1666666667)
    assert cmp_no_d.corr('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=-0.1666666667)
    assert cmp_no_d.corr('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=-0.097826087)
