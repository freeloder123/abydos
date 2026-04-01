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

"""abydos.tests.distance.test_distance_eyraud.

This module contains unit tests for abydos.distance.Eyraud
"""


import pytest

from abydos.distance import Eyraud


cmp = Eyraud()

cmp_no_d = Eyraud(alphabet=0)


def test_eyraud_sim():
    """Test abydos.distance.Eyraud.sim."""
    # Base cases
    assert cmp.sim('', '') == 0.0
    assert cmp.sim('a', '') == 0.0
    assert cmp.sim('', 'a') == 0.0
    assert cmp.sim('abc', '') == 0.0
    assert cmp.sim('', 'abc') == 0.0
    assert cmp.sim('abc', 'abc') == pytest.approx(abs=1e-7, expected=1.2327416173570019e-06)
    assert cmp.sim('abcd', 'efgh') == pytest.approx(abs=1e-7, expected=1.6478781097519779e-06)

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=1.5144e-06)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=1.5144e-06)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=1.5144e-06)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=1.5144e-06)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=1.565e-06)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.sim('', '') == 0.0
    assert cmp_no_d.sim('a', '') == 0.0
    assert cmp_no_d.sim('', 'a') == 0.0
    assert cmp_no_d.sim('abc', '') == 0.0
    assert cmp_no_d.sim('', 'abc') == 0.0
    assert cmp_no_d.sim('abc', 'abc') == 0.75
    assert cmp_no_d.sim('abcd', 'efgh') == 0.04

    assert cmp_no_d.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.1018518519)
    assert cmp_no_d.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.1018518519)
    assert cmp_no_d.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.1018518519)
    assert cmp_no_d.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.1018518519)
    assert cmp_no_d.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.078030303)

def test_eyraud_dist():
    """Test abydos.distance.Eyraud.dist."""
    # Base cases
    assert cmp.dist('', '') == 1.0
    assert cmp.dist('a', '') == 1.0
    assert cmp.dist('', 'a') == 1.0
    assert cmp.dist('abc', '') == 1.0
    assert cmp.dist('', 'abc') == 1.0
    assert cmp.dist('abc', 'abc') == pytest.approx(abs=1e-7, expected=0.9999987672583827)
    assert cmp.dist('abcd', 'efgh') == pytest.approx(abs=1e-7, expected=0.9999983521218903)

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.9999984856)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.9999984856)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.9999984856)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.9999984856)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.999998435)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.dist('', '') == 1.0
    assert cmp_no_d.dist('a', '') == 1.0
    assert cmp_no_d.dist('', 'a') == 1.0
    assert cmp_no_d.dist('abc', '') == 1.0
    assert cmp_no_d.dist('', 'abc') == 1.0
    assert cmp_no_d.dist('abc', 'abc') == 0.25
    assert cmp_no_d.dist('abcd', 'efgh') == 0.96

    assert cmp_no_d.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.8981481481)
    assert cmp_no_d.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.8981481481)
    assert cmp_no_d.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.8981481481)
    assert cmp_no_d.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.8981481481)
    assert cmp_no_d.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.921969697)

def test_eyraud_sim_score():
    """Test abydos.distance.Eyraud.sim_score."""
    # Base cases
    assert cmp.sim_score('', '') == 0.0
    assert cmp.sim_score('a', '') == 0.0
    assert cmp.sim_score('', 'a') == 0.0
    assert cmp.sim_score('abc', '') == 0.0
    assert cmp.sim_score('', 'abc') == 0.0
    assert cmp.sim_score('abc', 'abc') == pytest.approx(abs=1e-7, expected=-1.2327416173570019e-06)
    assert cmp.sim_score('abcd', 'efgh') == pytest.approx(abs=1e-7, expected=-1.6478781097519779e-06)

    assert cmp.sim_score('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=-1.5144e-06)
    assert cmp.sim_score('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=-1.5144e-06)
    assert cmp.sim_score('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=-1.5144e-06)
    assert cmp.sim_score('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=-1.5144e-06)
    assert cmp.sim_score('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=-1.565e-06)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.sim_score('', '') == 0.0
    assert cmp_no_d.sim_score('a', '') == 0.0
    assert cmp_no_d.sim_score('', 'a') == 0.0
    assert cmp_no_d.sim_score('abc', '') == 0.0
    assert cmp_no_d.sim_score('', 'abc') == 0.0
    assert cmp_no_d.sim_score('abc', 'abc') == -0.75
    assert cmp_no_d.sim_score('abcd', 'efgh') == -0.04

    assert cmp_no_d.sim_score('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=-0.1018518519)
    assert cmp_no_d.sim_score('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=-0.1018518519)
    assert cmp_no_d.sim_score('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=-0.1018518519)
    assert cmp_no_d.sim_score('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=-0.1018518519)
    assert cmp_no_d.sim_score('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=-0.078030303)
