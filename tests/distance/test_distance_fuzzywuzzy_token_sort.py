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

"""abydos.tests.distance.test_distance_fuzzywuzzy_token_sort.

This module contains unit tests for abydos.distance.FuzzyWuzzyTokenSort
"""


import pytest

from abydos.distance import FuzzyWuzzyTokenSort
from abydos.tokenizer import QGrams


cmp = FuzzyWuzzyTokenSort()

cmp_q2 = FuzzyWuzzyTokenSort(tokenizer=QGrams(qval=2))


def test_fuzzywuzzy_token_sort_sim():
    """Test abydos.distance.FuzzyWuzzyTokenSort.sim."""
    # Base cases
    assert cmp.sim('', '') == 1.0
    assert cmp.sim('a', '') == 0.0
    assert cmp.sim('', 'a') == 0.0
    assert cmp.sim('abc', '') == 0.0
    assert cmp.sim('', 'abc') == 0.0
    assert cmp.sim('abc', 'abc') == 1.0
    assert cmp.sim('abcd', 'efgh') == 0.0

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.6)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.6)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.8)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.8)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.6315789474)

    # tests from blog
    assert (
        cmp.sim( 'New York Mets vs Atlanta Braves', 'Atlanta Braves vs New York Mets', )
        == 1.0
    )

    # q2 tokenizer
    assert cmp_q2.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.8524590163934426)
    assert cmp_q2.sim('YANKEES', 'NEW YORK YANKEES') == pytest.approx(abs=1e-7, expected=0.6027397260273972)
    assert cmp_q2.sim('NEW YORK METS', 'NEW YORK YANKEES') == pytest.approx(abs=1e-7, expected=0.7692307692307693)
    assert cmp_q2.sim(
            'New York Mets vs Atlanta Braves',
            'Atlanta Braves vs New York Mets',
        ) == pytest.approx(abs=1e-7, expected=0.9578947368421052)

def test_fuzzywuzzy_token_sort_dist():
    """Test abydos.distance.FuzzyWuzzyTokenSort.dist."""
    # Base cases
    assert cmp.dist('', '') == 0.0
    assert cmp.dist('a', '') == 1.0
    assert cmp.dist('', 'a') == 1.0
    assert cmp.dist('abc', '') == 1.0
    assert cmp.dist('', 'abc') == 1.0
    assert cmp.dist('abc', 'abc') == 0.0
    assert cmp.dist('abcd', 'efgh') == 1.0

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.4)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.4)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.2)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.2)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.3684210526)
