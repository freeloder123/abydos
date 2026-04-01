# Copyright 2014-2020 by Christopher C. Little.
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

"""abydos.tests.distance.test_distance_jaccard.

This module contains unit tests for abydos.distance.Jaccard
"""

import pytest
from math import log2

from abydos.distance import Jaccard
from abydos.tokenizer import QGrams, WhitespaceTokenizer

from .. import NONQ_FROM, NONQ_TO


class TestJaccard:
    """Test Jaccard functions.

    abydos.distance.Jaccard
    """

    cmp = Jaccard()
    cmp_q2 = Jaccard(tokenizer=QGrams(2))
    cmp_ws = Jaccard(tokenizer=WhitespaceTokenizer())

    def test_jaccard_sim(self):
        """Test abydos.distance.Jaccard.sim."""
        assert self.cmp.sim('', '') == 1
        assert self.cmp.sim('nelson', '') == 0
        assert self.cmp.sim('', 'neilsen') == 0
        assert self.cmp.sim('nelson', 'neilsen') == pytest.approx(
            abs=1e-7, expected=4 / 11
        )

        assert self.cmp_q2.sim('', '') == 1
        assert self.cmp_q2.sim('nelson', '') == 0
        assert self.cmp_q2.sim('', 'neilsen') == 0
        assert self.cmp_q2.sim('nelson', 'neilsen') == pytest.approx(
            abs=1e-7, expected=4 / 11
        )

        # supplied q-gram tests
        assert self.cmp.sim(
            QGrams().tokenize('').get_counter(),
            QGrams().tokenize('').get_counter(),
        ) == 1
        assert self.cmp.sim(
            QGrams().tokenize('nelson').get_counter(),
            QGrams().tokenize('').get_counter(),
        ) == 0
        assert self.cmp.sim(
            QGrams().tokenize('').get_counter(),
            QGrams().tokenize('neilsen').get_counter(),
        ) == 0
        assert self.cmp.sim(
            QGrams().tokenize('nelson').get_counter(),
            QGrams().tokenize('neilsen').get_counter(),
        ) == pytest.approx(abs=1e-7, expected=4 / 11)

        # non-q-gram tests
        assert self.cmp_ws.sim('', '') == 1
        assert self.cmp_ws.sim('the quick', '') == 0
        assert self.cmp_ws.sim('', 'the quick') == 0
        assert self.cmp_ws.sim(NONQ_FROM, NONQ_TO) == pytest.approx(
            abs=1e-7, expected=1 / 3
        )
        assert self.cmp_ws.sim(NONQ_TO, NONQ_FROM) == pytest.approx(
            abs=1e-7, expected=1 / 3
        )

    def test_jaccard_dist(self):
        """Test abydos.distance.Jaccard.dist."""
        assert self.cmp.dist('', '') == 0
        assert self.cmp.dist('nelson', '') == 1
        assert self.cmp.dist('', 'neilsen') == 1
        assert self.cmp.dist('nelson', 'neilsen') == pytest.approx(
            abs=1e-7, expected=7 / 11
        )

        assert self.cmp_q2.dist('', '') == 0
        assert self.cmp_q2.dist('nelson', '') == 1
        assert self.cmp_q2.dist('', 'neilsen') == 1
        assert self.cmp_q2.dist('nelson', 'neilsen') == pytest.approx(
            abs=1e-7, expected=7 / 11
        )

        # supplied q-gram tests
        assert self.cmp.dist(
            QGrams().tokenize('').get_counter(),
            QGrams().tokenize('').get_counter(),
        ) == 0
        assert self.cmp.dist(
            QGrams().tokenize('nelson').get_counter(),
            QGrams().tokenize('').get_counter(),
        ) == 1
        assert self.cmp.dist(
            QGrams().tokenize('').get_counter(),
            QGrams().tokenize('neilsen').get_counter(),
        ) == 1
        assert self.cmp.dist(
            QGrams().tokenize('nelson').get_counter(),
            QGrams().tokenize('neilsen').get_counter(),
        ) == pytest.approx(abs=1e-7, expected=7 / 11)

        # non-q-gram tests
        assert self.cmp_ws.dist('', '') == 0
        assert self.cmp_ws.dist('the quick', '') == 1
        assert self.cmp_ws.dist('', 'the quick') == 1
        assert self.cmp_ws.dist(NONQ_FROM, NONQ_TO) == pytest.approx(
            abs=1e-7, expected=2 / 3
        )
        assert self.cmp_ws.dist(NONQ_TO, NONQ_FROM) == pytest.approx(
            abs=1e-7, expected=2 / 3
        )


class TestTanimoto:
    """Test Tanimoto functions.

    abydos.distance.Jaccard.tanimoto_coeff
    """

    cmp = Jaccard()
    cmp_q2 = Jaccard(tokenizer=QGrams(2))
    cmp_ws = Jaccard(tokenizer=WhitespaceTokenizer())

    def test_jaccard_tanimoto_coeff(self):
        """Test abydos.distance.Jaccard.tanimoto_coeff."""
        assert self.cmp.tanimoto_coeff('', '') == 0
        assert self.cmp.tanimoto_coeff('nelson', '') == float('-inf')
        assert self.cmp.tanimoto_coeff('', 'neilsen') == float('-inf')
        assert self.cmp.tanimoto_coeff('nelson', 'neilsen') == pytest.approx(
            abs=1e-7, expected=log2(4 / 11)
        )

        assert self.cmp_q2.tanimoto_coeff('', '') == 0
        assert self.cmp_q2.tanimoto_coeff('nelson', '') == float('-inf')
        assert self.cmp_q2.tanimoto_coeff('', 'neilsen') == float('-inf')
        assert self.cmp_q2.tanimoto_coeff(
            'nelson', 'neilsen'
        ) == pytest.approx(abs=1e-7, expected=log2(4 / 11))

        # supplied q-gram tests
        assert self.cmp.tanimoto_coeff(
            QGrams().tokenize('').get_counter(),
            QGrams().tokenize('').get_counter(),
        ) == 0
        assert self.cmp.tanimoto_coeff(
            QGrams().tokenize('nelson').get_counter(),
            QGrams().tokenize('').get_counter(),
        ) == float('-inf')
        assert self.cmp.tanimoto_coeff(
            QGrams().tokenize('').get_counter(),
            QGrams().tokenize('neilsen').get_counter(),
        ) == float('-inf')
        assert self.cmp.tanimoto_coeff(
            QGrams().tokenize('nelson').get_counter(),
            QGrams().tokenize('neilsen').get_counter(),
        ) == pytest.approx(abs=1e-7, expected=log2(4 / 11))

        # non-q-gram tests
        assert self.cmp_ws.tanimoto_coeff('', '') == 0
        assert self.cmp_ws.tanimoto_coeff('the quick', '') == float('-inf')
        assert self.cmp_ws.tanimoto_coeff('', 'the quick') == float('-inf')
        assert self.cmp_ws.tanimoto_coeff(
            NONQ_FROM, NONQ_TO
        ) == pytest.approx(abs=1e-7, expected=log2(1 / 3))
        assert self.cmp_ws.tanimoto_coeff(
            NONQ_TO, NONQ_FROM
        ) == pytest.approx(abs=1e-7, expected=log2(1 / 3))
