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

"""abydos.tests.distance.test_distance_tversky.

This module contains unit tests for abydos.distance.Tversky
"""


import pytest

from abydos.distance import Tversky
from abydos.tokenizer import QGrams, WhitespaceTokenizer

from .. import NONQ_FROM, NONQ_TO


cmp = Tversky()

cmp_q2 = Tversky(tokenizer=QGrams(2))

cmp_ws = Tversky(tokenizer=WhitespaceTokenizer())


def test_tversky_sim():
    """Test abydos.distance.Tversky.sim."""
    assert cmp.sim('', '') == 1
    assert cmp.sim('nelson', '') == 0
    assert cmp.sim('', 'neilsen') == 0
    assert cmp.sim('nelson', 'neilsen') == pytest.approx(abs=1e-7, expected=4 / 11)

    assert cmp_q2.sim('', '') == 1
    assert cmp_q2.sim('nelson', '') == 0
    assert cmp_q2.sim('', 'neilsen') == 0
    assert cmp_q2.sim('nelson', 'neilsen') == pytest.approx(abs=1e-7, expected=4 / 11)

    # test valid alpha & beta
    with pytest.raises(ValueError):
        Tversky(alpha=-1.0, beta=-1.0).sim('abcd', 'dcba')
    with pytest.raises(ValueError):
        Tversky(alpha=-1.0, beta=0.0).sim('abcd', 'dcba')
    with pytest.raises(ValueError):
        Tversky(alpha=0.0, beta=-1.0).sim('abcd', 'dcba')

    # test empty QGrams
    assert Tversky(tokenizer=QGrams(7, start_stop='')).sim(
            'nelson', 'neilsen'
        ) == pytest.approx(abs=1e-7, expected=0.0)

    # test unequal alpha & beta
    assert Tversky(alpha=2.0, beta=1.0, tokenizer=QGrams(2)).sim(
            'niall', 'neal'
        ) == pytest.approx(abs=1e-7, expected=3 / 11)
    assert Tversky(alpha=1.0, beta=2.0, tokenizer=QGrams(2)).sim(
            'niall', 'neal'
        ) == pytest.approx(abs=1e-7, expected=3 / 10)
    assert Tversky(alpha=2.0, beta=2.0, tokenizer=QGrams(2)).sim(
            'niall', 'neal'
        ) == pytest.approx(abs=1e-7, expected=3 / 13)

    # test bias parameter
    assert Tversky(alpha=1.0, beta=1.0, bias=0.5, tokenizer=QGrams(2)).sim(
            'niall', 'neal'
        ) == pytest.approx(abs=1e-7, expected=7 / 11)
    assert Tversky(alpha=2.0, beta=1.0, bias=0.5, tokenizer=QGrams(2)).sim(
            'niall', 'neal'
        ) == pytest.approx(abs=1e-7, expected=7 / 9)
    assert Tversky(alpha=1.0, beta=2.0, bias=0.5, tokenizer=QGrams(2)).sim(
            'niall', 'neal'
        ) == pytest.approx(abs=1e-7, expected=7 / 15)
    assert Tversky(alpha=2.0, beta=2.0, bias=0.5, tokenizer=QGrams(2)).sim(
            'niall', 'neal'
        ) == pytest.approx(abs=1e-7, expected=7 / 11)

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
        ) == pytest.approx(abs=1e-7, expected=4 / 11)

    # non-q-gram tests
    assert cmp_ws.sim('', '') == 1
    assert cmp_ws.sim('the quick', '') == 0
    assert cmp_ws.sim('', 'the quick') == 0
    assert cmp_ws.sim(NONQ_FROM, NONQ_TO) == pytest.approx(abs=1e-7, expected=1 / 3)
    assert cmp_ws.sim(NONQ_TO, NONQ_FROM) == pytest.approx(abs=1e-7, expected=1 / 3)

def test_tversky_dist():
    """Test abydos.distance.Tversky.dist."""
    assert cmp.dist('', '') == 0
    assert cmp.dist('nelson', '') == 1
    assert cmp.dist('', 'neilsen') == 1
    assert cmp.dist('nelson', 'neilsen') == pytest.approx(abs=1e-7, expected=7 / 11)

    assert cmp_q2.dist('', '') == 0
    assert cmp_q2.dist('nelson', '') == 1
    assert cmp_q2.dist('', 'neilsen') == 1
    assert cmp_q2.dist('nelson', 'neilsen') == pytest.approx(abs=1e-7, expected=7 / 11)

    # test valid alpha & beta
    with pytest.raises(ValueError):
        Tversky(alpha=-1.0, beta=-1.0).dist('abcd', 'dcba')
    with pytest.raises(ValueError):
        Tversky(alpha=-1.0, beta=0.0).dist('abcd', 'dcba')
    with pytest.raises(ValueError):
        Tversky(alpha=0.0, beta=-1.0).dist('abcd', 'dcba')

    # test empty QGrams
    assert Tversky(tokenizer=QGrams(7, start_stop='')).dist(
            'nelson', 'neilsen'
        ) == pytest.approx(abs=1e-7, expected=1.0)

    # test unequal alpha & beta
    assert Tversky(alpha=2.0, beta=1.0, tokenizer=QGrams(2)).dist(
            'niall', 'neal'
        ) == pytest.approx(abs=1e-7, expected=8 / 11)
    assert Tversky(alpha=1.0, beta=2.0, tokenizer=QGrams(2)).dist(
            'niall', 'neal'
        ) == pytest.approx(abs=1e-7, expected=7 / 10)
    assert Tversky(alpha=2.0, beta=2.0, tokenizer=QGrams(2)).dist(
            'niall', 'neal'
        ) == pytest.approx(abs=1e-7, expected=10 / 13)

    # test bias parameter
    assert Tversky(alpha=1.0, beta=1.0, bias=0.5, tokenizer=QGrams(2)).dist(
            'niall', 'neal'
        ) == pytest.approx(abs=1e-7, expected=4 / 11)
    assert Tversky(alpha=2.0, beta=1.0, bias=0.5, tokenizer=QGrams(2)).dist(
            'niall', 'neal'
        ) == pytest.approx(abs=1e-7, expected=2 / 9)
    assert Tversky(alpha=1.0, beta=2.0, bias=0.5, tokenizer=QGrams(2)).dist(
            'niall', 'neal'
        ) == pytest.approx(abs=1e-7, expected=8 / 15)
    assert Tversky(alpha=2.0, beta=2.0, bias=0.5, tokenizer=QGrams(2)).dist(
            'niall', 'neal'
        ) == pytest.approx(abs=1e-7, expected=4 / 11)

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
        ) == pytest.approx(abs=1e-7, expected=7 / 11)

    # non-q-gram tests
    assert cmp_ws.dist('', '') == 0
    assert cmp_ws.dist('the quick', '') == 1
    assert cmp_ws.dist('', 'the quick') == 1
    assert cmp_ws.dist(NONQ_FROM, NONQ_TO) == pytest.approx(abs=1e-7, expected=2 / 3)
    assert cmp_ws.dist(NONQ_TO, NONQ_FROM) == pytest.approx(abs=1e-7, expected=2 / 3)
