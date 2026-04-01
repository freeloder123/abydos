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

"""abydos.tests.distance.test_distance_fuzzywuzzy_token_set.

This module contains unit tests for abydos.distance.FuzzyWuzzyTokenSet
"""


import pytest

from abydos.distance import FuzzyWuzzyTokenSet
from abydos.tokenizer import QGrams


cmp = FuzzyWuzzyTokenSet()

cmp_q2 = FuzzyWuzzyTokenSet(tokenizer=QGrams(qval=2))


def test_fuzzywuzzy_token_set_sim():
    """Test abydos.distance.FuzzyWuzzyTokenSet.sim."""
    # Base cases
    assert cmp.sim('', '') == 1.0
    assert cmp.sim('a', '') == 1.0
    assert cmp.sim('', 'a') == 1.0
    assert cmp.sim('abc', '') == 1.0
    assert cmp.sim('', 'abc') == 1.0
    assert cmp.sim('abc', 'abc') == 1.0
    assert cmp.sim('abcd', 'efgh') == 0.3333333333333333

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.6666666667)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.6666666667)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.8333333333)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.8333333333)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.6666666667)

    # tests from blog
    assert (
        cmp.sim( 'mariners vs angels', 'los angeles angels of anaheim at seattle mariners', )
        == 0.9411764705882353
    )
    assert cmp.sim('Sirhan, Sirhan', 'Sirhan') == 1.0

    # q2 tokenizer
    assert cmp_q2.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.84)
    assert cmp_q2.sim('YANKEES', 'NEW YORK YANKEES') == pytest.approx(abs=1e-7, expected=0.9545454545454546)
    assert cmp_q2.sim('NEW YORK METS', 'NEW YORK YANKEES') == pytest.approx(abs=1e-7, expected=0.8450704225352113)
    assert cmp_q2.sim(
            'New York Mets vs Atlanta Braves',
            'Atlanta Braves vs New York Mets',
        ) == pytest.approx(abs=1e-7, expected=0.9782608695652174)

def test_fuzzywuzzy_token_set_dist():
    """Test abydos.distance.FuzzyWuzzyTokenSet.dist."""
    # Base cases
    assert cmp.dist('', '') == 0.0
    assert cmp.dist('a', '') == 0.0
    assert cmp.dist('', 'a') == 0.0
    assert cmp.dist('abc', '') == 0.0
    assert cmp.dist('', 'abc') == 0.0
    assert cmp.dist('abc', 'abc') == 0.0
    assert cmp.dist('abcd', 'efgh') == 0.6666666666666667

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.3333333333)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.3333333333)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.1666666667)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.1666666667)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.3333333333)
