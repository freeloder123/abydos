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

"""abydos.tests.distance.test_distance_jaccard_nm.

This module contains unit tests for abydos.distance.JaccardNM
"""


import pytest

from abydos.distance import JaccardNM


cmp = JaccardNM()

cmp_no_d = JaccardNM(alphabet=0)


def test_jaccard_nm_sim():
    """Test abydos.distance.JaccardNM.sim."""
    # Base cases
    assert cmp.sim('', '') == 0.0
    assert cmp.sim('a', '') == 0.0
    assert cmp.sim('', 'a') == 0.0
    assert cmp.sim('abc', '') == 0.0
    assert cmp.sim('', 'abc') == 0.0
    assert cmp.sim('abc', 'abc') == 0.01015228426395939
    assert cmp.sim('abcd', 'efgh') == 0.0

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.0075662043)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.0075662043)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.0075662043)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.0075662043)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.0175438596)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.sim('', '') == 0.0
    assert cmp_no_d.sim('a', '') == 0.0
    assert cmp_no_d.sim('', 'a') == 0.0
    assert cmp_no_d.sim('abc', '') == 0.0
    assert cmp_no_d.sim('', 'abc') == 0.0
    assert cmp_no_d.sim('abc', 'abc') == 1.0
    assert cmp_no_d.sim('abcd', 'efgh') == 0.0

    assert cmp_no_d.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.3333333333)
    assert cmp_no_d.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.3333333333)
    assert cmp_no_d.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.3333333333)
    assert cmp_no_d.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.3333333333)
    assert cmp_no_d.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.5)

def test_jaccard_nm_dist():
    """Test abydos.distance.JaccardNM.dist."""
    # Base cases
    assert cmp.dist('', '') == 1.0
    assert cmp.dist('a', '') == 1.0
    assert cmp.dist('', 'a') == 1.0
    assert cmp.dist('abc', '') == 1.0
    assert cmp.dist('', 'abc') == 1.0
    assert cmp.dist('abc', 'abc') == 0.9898477157360406
    assert cmp.dist('abcd', 'efgh') == 1.0

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.9924337957)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.9924337957)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.9924337957)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.9924337957)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.9824561404)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.dist('', '') == 1.0
    assert cmp_no_d.dist('a', '') == 1.0
    assert cmp_no_d.dist('', 'a') == 1.0
    assert cmp_no_d.dist('abc', '') == 1.0
    assert cmp_no_d.dist('', 'abc') == 1.0
    assert cmp_no_d.dist('abc', 'abc') == 0.0
    assert cmp_no_d.dist('abcd', 'efgh') == 1.0

    assert cmp_no_d.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.6666666667)
    assert cmp_no_d.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.6666666667)
    assert cmp_no_d.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.6666666667)
    assert cmp_no_d.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.6666666667)
    assert cmp_no_d.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.5)

def test_jaccard_nm_sim_score():
    """Test abydos.distance.JaccardNM.sim_score."""
    # Base cases
    assert cmp.sim_score('', '') == 0.0
    assert cmp.sim_score('a', '') == 0.0
    assert cmp.sim_score('', 'a') == 0.0
    assert cmp.sim_score('abc', '') == 0.0
    assert cmp.sim_score('', 'abc') == 0.0
    assert cmp.sim_score('abc', 'abc') == 0.005076142131979695
    assert cmp.sim_score('abcd', 'efgh') == 0.0

    assert cmp.sim_score('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.0037831021)
    assert cmp.sim_score('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.0037831021)
    assert cmp.sim_score('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.0037831021)
    assert cmp.sim_score('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.0037831021)
    assert cmp.sim_score('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.0087719298)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.sim_score('', '') == 0.0
    assert cmp_no_d.sim_score('a', '') == 0.0
    assert cmp_no_d.sim_score('', 'a') == 0.0
    assert cmp_no_d.sim_score('abc', '') == 0.0
    assert cmp_no_d.sim_score('', 'abc') == 0.0
    assert cmp_no_d.sim_score('abc', 'abc') == 0.5
    assert cmp_no_d.sim_score('abcd', 'efgh') == 0.0

    assert cmp_no_d.sim_score('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.1666666667)
    assert cmp_no_d.sim_score('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.1666666667)
    assert cmp_no_d.sim_score('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.1666666667)
    assert cmp_no_d.sim_score('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.1666666667)
    assert cmp_no_d.sim_score('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.25)
