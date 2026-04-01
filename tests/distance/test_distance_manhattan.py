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

"""abydos.tests.distance.test_distance_manhattan.

This module contains unit tests for abydos.distance.Manhattan
"""


import pytest

from abydos.distance import Manhattan
from abydos.tokenizer import QGrams, WhitespaceTokenizer

from .. import NONQ_FROM, NONQ_TO


cmp = Manhattan()

cmp_q2 = Manhattan(tokenizer=QGrams(2))

cmp_ws = Manhattan(tokenizer=WhitespaceTokenizer())


def test_manhattan_dist_abs():
    """Test abydos.distance.Manhattan.dist_abs."""
    assert cmp.dist_abs('', '') == 0
    assert cmp.dist_abs('nelson', '') == 7
    assert cmp.dist_abs('', 'neilsen') == 8
    assert cmp.dist_abs('nelson', 'neilsen') == pytest.approx(abs=1e-7, expected=7)

    assert cmp_q2.dist_abs('', '') == 0
    assert cmp_q2.dist_abs('nelson', '') == 7
    assert cmp_q2.dist_abs('', 'neilsen') == 8
    assert cmp_q2.dist_abs('nelson', 'neilsen') == pytest.approx(abs=1e-7, expected=7)

    # supplied q-gram tests
    assert (
        cmp.dist_abs( QGrams().tokenize('').get_counter(), QGrams().tokenize('').get_counter(), )
        == 0
    )
    assert (
        cmp.dist_abs( QGrams().tokenize('nelson').get_counter(), QGrams().tokenize('').get_counter(), )
        == 7
    )
    assert (
        cmp.dist_abs( QGrams().tokenize('').get_counter(), QGrams().tokenize('neilsen').get_counter(), )
        == 8
    )
    assert cmp.dist_abs(
            QGrams().tokenize('nelson').get_counter(),
            QGrams().tokenize('neilsen').get_counter(),
        ) == pytest.approx(abs=1e-7, expected=7)

    # non-q-gram tests
    assert cmp_ws.dist_abs('', '') == 0
    assert cmp_ws.dist_abs('the quick', '') == 2
    assert cmp_ws.dist_abs('', 'the quick') == 2
    assert cmp_ws.dist_abs(NONQ_FROM, NONQ_TO) == pytest.approx(abs=1e-7, expected=8)
    assert cmp_ws.dist_abs(NONQ_TO, NONQ_FROM) == pytest.approx(abs=1e-7, expected=8)

def test_manhattan_sim():
    """Test abydos.distance.Manhattan.sim."""
    assert cmp.sim('', '') == 1
    assert cmp.sim('nelson', '') == 0
    assert cmp.sim('', 'neilsen') == 0
    assert cmp.sim('nelson', 'neilsen') == pytest.approx(abs=1e-7, expected=8 / 15)

    assert cmp_q2.sim('', '') == 1
    assert cmp_q2.sim('nelson', '') == 0
    assert cmp_q2.sim('', 'neilsen') == 0
    assert cmp_q2.sim('nelson', 'neilsen') == pytest.approx(abs=1e-7, expected=8 / 15)

    # supplied q-gram tests
    assert (
        cmp.sim( QGrams().tokenize('').get_counter(), QGrams().tokenize('').get_counter(), )
        == 1
    )
    assert (
        cmp.sim( QGrams().tokenize('nelson').get_counter(), QGrams().tokenize('').get_counter(), )
        == 0
    )
    assert (
        cmp.sim( QGrams().tokenize('').get_counter(), QGrams().tokenize('neilsen').get_counter(), )
        == 0
    )
    assert cmp.sim(
            QGrams().tokenize('nelson').get_counter(),
            QGrams().tokenize('neilsen').get_counter(),
        ) == pytest.approx(abs=1e-7, expected=8 / 15)

    # non-q-gram tests
    assert cmp_ws.sim('', '') == 1
    assert cmp_ws.sim('the quick', '') == 0
    assert cmp_ws.sim('', 'the quick') == 0
    assert cmp_ws.sim(NONQ_FROM, NONQ_TO) == pytest.approx(abs=1e-7, expected=1 / 2)
    assert cmp_ws.sim(NONQ_TO, NONQ_FROM) == pytest.approx(abs=1e-7, expected=1 / 2)

def test_manhattan_dist():
    """Test abydos.distance.Manhattan.dist."""
    assert cmp.dist('', '') == 0
    assert cmp.dist('nelson', '') == 1
    assert cmp.dist('', 'neilsen') == 1
    assert cmp.dist('nelson', 'neilsen') == pytest.approx(abs=1e-7, expected=7 / 15)

    assert cmp_q2.dist('', '') == 0
    assert cmp_q2.dist('nelson', '') == 1
    assert cmp_q2.dist('', 'neilsen') == 1
    assert cmp_q2.dist('nelson', 'neilsen') == pytest.approx(abs=1e-7, expected=7 / 15)

    # supplied q-gram tests
    assert (
        cmp.dist( QGrams().tokenize('').get_counter(), QGrams().tokenize('').get_counter(), )
        == 0
    )
    assert (
        cmp.dist( QGrams().tokenize('nelson').get_counter(), QGrams().tokenize('').get_counter(), )
        == 1
    )
    assert (
        cmp.dist( QGrams().tokenize('').get_counter(), QGrams().tokenize('neilsen').get_counter(), )
        == 1
    )
    assert cmp.dist(
            QGrams().tokenize('nelson').get_counter(),
            QGrams().tokenize('neilsen').get_counter(),
        ) == pytest.approx(abs=1e-7, expected=7 / 15)

    # non-q-gram tests
    assert cmp_ws.dist('', '') == 0
    assert cmp_ws.dist('the quick', '') == 1
    assert cmp_ws.dist('', 'the quick') == 1
    assert cmp_ws.dist(NONQ_FROM, NONQ_TO) == pytest.approx(abs=1e-7, expected=1 / 2)
    assert cmp_ws.dist(NONQ_TO, NONQ_FROM) == pytest.approx(abs=1e-7, expected=1 / 2)
