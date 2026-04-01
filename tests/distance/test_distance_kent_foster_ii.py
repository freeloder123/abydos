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

"""abydos.tests.distance.test_distance_kent_foster_ii.

This module contains unit tests for abydos.distance.KentFosterII
"""


import pytest

from abydos.distance import KentFosterII


cmp = KentFosterII()

cmp_no_d = KentFosterII(alphabet=0)


def test_kent_foster_ii_sim():
    """Test abydos.distance.KentFosterII.sim."""
    # Base cases
    assert cmp.sim('', '') == 1.0
    assert cmp.sim('a', '') == 1.0
    assert cmp.sim('', 'a') == 1.0
    assert cmp.sim('abc', '') == 1.0
    assert cmp.sim('', 'abc') == 1.0
    assert cmp.sim('abc', 'abc') == 1.0
    assert cmp.sim('abcd', 'efgh') == 0.9968010236724241

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.9980756895)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.9980756895)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.9980756895)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.9980756895)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.9977888336)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.sim('', '') == 1.0
    assert cmp_no_d.sim('a', '') == 1.0
    assert cmp_no_d.sim('', 'a') == 1.0
    assert cmp_no_d.sim('abc', '') == 1.0
    assert cmp_no_d.sim('', 'abc') == 1.0
    assert cmp_no_d.sim('abc', 'abc') == 1.0
    assert cmp_no_d.sim('abcd', 'efgh') == 0.6666666666666667

    assert cmp_no_d.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.6666666667)
    assert cmp_no_d.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.6666666667)
    assert cmp_no_d.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.6666666667)
    assert cmp_no_d.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.6666666667)
    assert cmp_no_d.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.6756756757)

def test_kent_foster_ii_dist():
    """Test abydos.distance.KentFosterII.dist."""
    # Base cases
    assert cmp.dist('', '') == 0.0
    assert cmp.dist('a', '') == 0.0
    assert cmp.dist('', 'a') == 0.0
    assert cmp.dist('abc', '') == 0.0
    assert cmp.dist('', 'abc') == 0.0
    assert cmp.dist('abc', 'abc') == 0.0
    assert cmp.dist('abcd', 'efgh') == 0.003198976327575931

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.0019243105)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.0019243105)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.0019243105)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.0019243105)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.0022111664)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.dist('', '') == 0.0
    assert cmp_no_d.dist('a', '') == 0.0
    assert cmp_no_d.dist('', 'a') == 0.0
    assert cmp_no_d.dist('abc', '') == 0.0
    assert cmp_no_d.dist('', 'abc') == 0.0
    assert cmp_no_d.dist('abc', 'abc') == 0.0
    assert cmp_no_d.dist('abcd', 'efgh') == 0.33333333333333326

    assert cmp_no_d.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.3333333333)
    assert cmp_no_d.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.3333333333)
    assert cmp_no_d.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.3333333333)
    assert cmp_no_d.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.3333333333)
    assert cmp_no_d.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.3243243243)

def test_kent_foster_ii_sim_score():
    """Test abydos.distance.KentFosterII.sim_score."""
    # Base cases
    assert cmp.sim_score('', '') == 0.0
    assert cmp.sim_score('a', '') == 0.0
    assert cmp.sim_score('', 'a') == 0.0
    assert cmp.sim_score('abc', '') == 0.0
    assert cmp.sim_score('', 'abc') == 0.0
    assert cmp.sim_score('abc', 'abc') == 0.0
    assert cmp.sim_score('abcd', 'efgh') == -0.0031989763275758767

    assert cmp.sim_score('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=-0.0019243105)
    assert cmp.sim_score('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=-0.0019243105)
    assert cmp.sim_score('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=-0.0019243105)
    assert cmp.sim_score('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=-0.0019243105)
    assert cmp.sim_score('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=-0.0022111664)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.sim_score('', '') == 0.0
    assert cmp_no_d.sim_score('a', '') == 0.0
    assert cmp_no_d.sim_score('', 'a') == 0.0
    assert cmp_no_d.sim_score('abc', '') == 0.0
    assert cmp_no_d.sim_score('', 'abc') == 0.0
    assert cmp_no_d.sim_score('abc', 'abc') == 0.0
    assert cmp_no_d.sim_score('abcd', 'efgh') == -0.3333333333333333

    assert cmp_no_d.sim_score('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=-0.3333333333)
    assert cmp_no_d.sim_score('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=-0.3333333333)
    assert cmp_no_d.sim_score('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=-0.3333333333)
    assert cmp_no_d.sim_score('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=-0.3333333333)
    assert cmp_no_d.sim_score('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=-0.3243243243)
