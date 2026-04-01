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

"""abydos.tests.distance.test_distance_unknown_j.

This module contains unit tests for abydos.distance.UnknownJ
"""


import pytest

from abydos.distance import UnknownJ


cmp = UnknownJ()

cmp_no_d = UnknownJ(alphabet=0)


def test_unknown_j_sim():
    """Test abydos.distance.UnknownJ.sim."""
    # Base cases
    assert cmp.sim('', '') == 0.0
    assert cmp.sim('a', '') == 0.0
    assert cmp.sim('', 'a') == 0.0
    assert cmp.sim('abc', '') == 0.0
    assert cmp.sim('', 'abc') == 0.0
    assert cmp.sim('abc', 'abc') == 1.0
    assert cmp.sim('abcd', 'efgh') == 0.0

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.5)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.5)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.5)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.5)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.6363636364)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.sim('', '') == 0.0
    assert cmp_no_d.sim('a', '') == 0.0
    assert cmp_no_d.sim('', 'a') == 0.0
    assert cmp_no_d.sim('abc', '') == 0.0
    assert cmp_no_d.sim('', 'abc') == 0.0
    assert cmp_no_d.sim('abc', 'abc') == 1.0
    assert cmp_no_d.sim('abcd', 'efgh') == 0.0

    assert cmp_no_d.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.1785714286)
    assert cmp_no_d.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.1785714286)
    assert cmp_no_d.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.1785714286)
    assert cmp_no_d.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.1785714286)
    assert cmp_no_d.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.1988636364)

def test_unknown_j_dist():
    """Test abydos.distance.UnknownJ.dist."""
    # Base cases
    assert cmp.dist('', '') == 1.0
    assert cmp.dist('a', '') == 1.0
    assert cmp.dist('', 'a') == 1.0
    assert cmp.dist('abc', '') == 1.0
    assert cmp.dist('', 'abc') == 1.0
    assert cmp.dist('abc', 'abc') == 0.0
    assert cmp.dist('abcd', 'efgh') == 1.0

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.5)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.5)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.5)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.5)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.3636363636)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.dist('', '') == 1.0
    assert cmp_no_d.dist('a', '') == 1.0
    assert cmp_no_d.dist('', 'a') == 1.0
    assert cmp_no_d.dist('abc', '') == 1.0
    assert cmp_no_d.dist('', 'abc') == 1.0
    assert cmp_no_d.dist('abc', 'abc') == 0.0
    assert cmp_no_d.dist('abcd', 'efgh') == 1.0

    assert cmp_no_d.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.8214285714)
    assert cmp_no_d.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.8214285714)
    assert cmp_no_d.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.8214285714)
    assert cmp_no_d.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.8214285714)
    assert cmp_no_d.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.8011363636)

def test_unknown_j_sim_score():
    """Test abydos.distance.UnknownJ.sim_score."""
    # Base cases
    assert cmp.sim_score('', '') == 0.0
    assert cmp.sim_score('a', '') == 0.0
    assert cmp.sim_score('', 'a') == 0.0
    assert cmp.sim_score('abc', '') == 0.0
    assert cmp.sim_score('', 'abc') == 0.0
    assert cmp.sim_score('abc', 'abc') == 1.005128205128205
    assert cmp.sim_score('abcd', 'efgh') == 0.0

    assert cmp.sim_score('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.5038560411)
    assert cmp.sim_score('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.5038560411)
    assert cmp.sim_score('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.5038560411)
    assert cmp.sim_score('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.5038560411)
    assert cmp.sim_score('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.6454192638)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.sim_score('', '') == 0.0
    assert cmp_no_d.sim_score('a', '') == 0.0
    assert cmp_no_d.sim_score('', 'a') == 0.0
    assert cmp_no_d.sim_score('abc', '') == 0.0
    assert cmp_no_d.sim_score('', 'abc') == 0.0
    assert cmp_no_d.sim_score('abc', 'abc') == 5.0
    assert cmp_no_d.sim_score('abcd', 'efgh') == 0.0

    assert cmp_no_d.sim_score('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=1.25)
    assert cmp_no_d.sim_score('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=1.25)
    assert cmp_no_d.sim_score('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=1.25)
    assert cmp_no_d.sim_score('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=1.25)
    assert cmp_no_d.sim_score('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=2.3863636364)
