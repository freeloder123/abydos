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

"""abydos.tests.distance.test_distance_stuart_tau.

This module contains unit tests for abydos.distance.StuartTau
"""


import pytest

from abydos.distance import StuartTau


cmp = StuartTau()

cmp_no_d = StuartTau(alphabet=0)


def test_stuart_tau_sim():
    """Test abydos.distance.StuartTau.sim."""
    # Base cases
    assert cmp.sim('', '') == 0.5025510204081632
    assert cmp.sim('a', '') == 0.5025380049979176
    assert cmp.sim('', 'a') == 0.5025380049979176
    assert cmp.sim('abc', '') == 0.5025249895876718
    assert cmp.sim('', 'abc') == 0.5025249895876718
    assert cmp.sim('abc', 'abc') == 0.5025510204081632
    assert cmp.sim('abcd', 'efgh') == 0.5024859433569346

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.5025119742)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.5025119742)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.5025119742)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.5025119742)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.5025054665)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.sim('', '') == 1.0
    assert cmp_no_d.sim('a', '') == 0.0
    assert cmp_no_d.sim('', 'a') == 0.0
    assert cmp_no_d.sim('abc', '') == 0.0
    assert cmp_no_d.sim('', 'abc') == 0.0
    assert cmp_no_d.sim('abc', 'abc') == 1.0
    assert cmp_no_d.sim('abcd', 'efgh') == 0.3

    assert cmp_no_d.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.4259259259)
    assert cmp_no_d.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.4259259259)
    assert cmp_no_d.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.4259259259)
    assert cmp_no_d.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.4259259259)
    assert cmp_no_d.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.5)

def test_stuart_tau_dist():
    """Test abydos.distance.StuartTau.dist."""
    # Base cases
    assert cmp.dist('', '') == 0.49744897959183676
    assert cmp.dist('a', '') == 0.49746199500208244
    assert cmp.dist('', 'a') == 0.49746199500208244
    assert cmp.dist('abc', '') == 0.4974750104123282
    assert cmp.dist('', 'abc') == 0.4974750104123282
    assert cmp.dist('abc', 'abc') == 0.49744897959183676
    assert cmp.dist('abcd', 'efgh') == 0.49751405664306536

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.4974880258)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.4974880258)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.4974880258)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.4974880258)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.4974945335)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.dist('', '') == 0.0
    assert cmp_no_d.dist('a', '') == 1.0
    assert cmp_no_d.dist('', 'a') == 1.0
    assert cmp_no_d.dist('abc', '') == 1.0
    assert cmp_no_d.dist('', 'abc') == 1.0
    assert cmp_no_d.dist('abc', 'abc') == 0.0
    assert cmp_no_d.dist('abcd', 'efgh') == 0.7

    assert cmp_no_d.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.5740740741)
    assert cmp_no_d.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.5740740741)
    assert cmp_no_d.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.5740740741)
    assert cmp_no_d.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.5740740741)
    assert cmp_no_d.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.5)

def test_stuart_tau_corr():
    """Test abydos.distance.StuartTau.corr."""
    # Base cases
    assert cmp.corr('', '') == 0.00510204081632653
    assert cmp.corr('a', '') == 0.005076009995835068
    assert cmp.corr('', 'a') == 0.005076009995835068
    assert cmp.corr('abc', '') == 0.005049979175343606
    assert cmp.corr('', 'abc') == 0.005049979175343606
    assert cmp.corr('abc', 'abc') == 0.00510204081632653
    assert cmp.corr('abcd', 'efgh') == 0.0049718867138692216

    assert cmp.corr('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.0050239484)
    assert cmp.corr('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.0050239484)
    assert cmp.corr('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.0050239484)
    assert cmp.corr('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.0050239484)
    assert cmp.corr('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.0050109329)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.corr('', '') == 1.0
    assert cmp_no_d.corr('a', '') == -1.0
    assert cmp_no_d.corr('', 'a') == -1.0
    assert cmp_no_d.corr('abc', '') == -1.0
    assert cmp_no_d.corr('', 'abc') == -1.0
    assert cmp_no_d.corr('abc', 'abc') == 1.0
    assert cmp_no_d.corr('abcd', 'efgh') == -0.4

    assert cmp_no_d.corr('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=-0.1481481481)
    assert cmp_no_d.corr('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=-0.1481481481)
    assert cmp_no_d.corr('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=-0.1481481481)
    assert cmp_no_d.corr('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=-0.1481481481)
    assert cmp_no_d.corr('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.0)
