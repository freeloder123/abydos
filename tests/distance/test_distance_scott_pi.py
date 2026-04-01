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

"""abydos.tests.distance.test_distance_scott_pi.

This module contains unit tests for abydos.distance.ScottPi
"""


import pytest

from abydos.distance import ScottPi


cmp = ScottPi()

cmp_no_d = ScottPi(alphabet=0)


def test_scott_pi_sim():
    """Test abydos.distance.ScottPi.sim."""
    # Base cases
    assert cmp.sim('', '') == 1.0
    assert cmp.sim('a', '') == 0.4993614303959431
    assert cmp.sim('', 'a') == 0.4993614303959431
    assert cmp.sim('abc', '') == 0.49872122762147786
    assert cmp.sim('', 'abc') == 0.49872122762147786
    assert cmp.sim('abc', 'abc') == 1.0
    assert cmp.sim('abcd', 'efgh') == 0.49679075738125517

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.7480719794)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.7480719794)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.7480719794)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.7480719794)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.8310708899)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.sim('', '') == 1.0
    assert cmp_no_d.sim('a', '') == 0.0
    assert cmp_no_d.sim('', 'a') == 0.0
    assert cmp_no_d.sim('abc', '') == 0.0
    assert cmp_no_d.sim('', 'abc') == 0.0
    assert cmp_no_d.sim('abc', 'abc') == 1.0
    assert cmp_no_d.sim('abcd', 'efgh') == 0.0

    assert cmp_no_d.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.25)
    assert cmp_no_d.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.25)
    assert cmp_no_d.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.25)
    assert cmp_no_d.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.25)
    assert cmp_no_d.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.3333333333)

def test_scott_pi_dist():
    """Test abydos.distance.ScottPi.dist."""
    # Base cases
    assert cmp.dist('', '') == 0.0
    assert cmp.dist('a', '') == 0.500638569604057
    assert cmp.dist('', 'a') == 0.500638569604057
    assert cmp.dist('abc', '') == 0.5012787723785221
    assert cmp.dist('', 'abc') == 0.5012787723785221
    assert cmp.dist('abc', 'abc') == 0.0
    assert cmp.dist('abcd', 'efgh') == 0.5032092426187449

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.2519280206)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.2519280206)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.2519280206)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.2519280206)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.1689291101)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.dist('', '') == 0.0
    assert cmp_no_d.dist('a', '') == 1.0
    assert cmp_no_d.dist('', 'a') == 1.0
    assert cmp_no_d.dist('abc', '') == 1.0
    assert cmp_no_d.dist('', 'abc') == 1.0
    assert cmp_no_d.dist('abc', 'abc') == 0.0
    assert cmp_no_d.dist('abcd', 'efgh') == 1.0

    assert cmp_no_d.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.75)
    assert cmp_no_d.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.75)
    assert cmp_no_d.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.75)
    assert cmp_no_d.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.75)
    assert cmp_no_d.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.6666666667)

def test_scott_pi_corr():
    """Test abydos.distance.ScottPi.corr."""
    # Base cases
    assert cmp.corr('', '') == 1.0
    assert cmp.corr('a', '') == -0.0012771392081137526
    assert cmp.corr('', 'a') == -0.0012771392081137526
    assert cmp.corr('abc', '') == -0.0025575447570442954
    assert cmp.corr('', 'abc') == -0.0025575447570442954
    assert cmp.corr('abc', 'abc') == 1.0
    assert cmp.corr('abcd', 'efgh') == -0.006418485237489689

    assert cmp.corr('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.4961439589)
    assert cmp.corr('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.4961439589)
    assert cmp.corr('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.4961439589)
    assert cmp.corr('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.4961439589)
    assert cmp.corr('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.6621417798)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.corr('', '') == 1.0
    assert cmp_no_d.corr('a', '') == -1.0
    assert cmp_no_d.corr('', 'a') == -1.0
    assert cmp_no_d.corr('abc', '') == -1.0
    assert cmp_no_d.corr('', 'abc') == -1.0
    assert cmp_no_d.corr('abc', 'abc') == 1.0
    assert cmp_no_d.corr('abcd', 'efgh') == -1.0

    assert cmp_no_d.corr('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=-0.5)
    assert cmp_no_d.corr('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=-0.5)
    assert cmp_no_d.corr('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=-0.5)
    assert cmp_no_d.corr('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=-0.5)
    assert cmp_no_d.corr('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=-0.3333333333)
