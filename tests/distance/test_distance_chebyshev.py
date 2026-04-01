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

"""abydos.tests.distance.test_distance_chebyshev.

This module contains unit tests for abydos.distance.Chebyshev
"""


import pytest

from abydos.distance import Chebyshev
from abydos.tokenizer import QGrams, WhitespaceTokenizer

from .. import NONQ_FROM, NONQ_TO


cmp = Chebyshev()

cmp_q2 = Chebyshev(tokenizer=QGrams(2))

cmp_ws = Chebyshev(tokenizer=WhitespaceTokenizer())


def test_chebyshev_dist_abs():
    """Test abydos.distance.Chebyshev.dist_abs."""
    assert cmp.dist_abs('', '') == 0
    assert cmp.dist_abs('nelson', '') == 1
    assert cmp.dist_abs('', 'neilsen') == 1
    assert cmp.dist_abs('nelson', 'neilsen') == 1

    assert cmp_q2.dist_abs('', '') == 0
    assert cmp_q2.dist_abs('nelson', '') == 1
    assert cmp_q2.dist_abs('', 'neilsen') == 1
    assert cmp_q2.dist_abs('nelson', 'neilsen') == pytest.approx(abs=1e-7, expected=1)

    # supplied q-gram tests
    assert (
        cmp.dist_abs( QGrams().tokenize('').get_counter(), QGrams().tokenize('').get_counter(), )
        == 0
    )
    assert (
        cmp.dist_abs( QGrams().tokenize('nelson').get_counter(), QGrams().tokenize('').get_counter(), )
        == 1
    )
    assert (
        cmp.dist_abs( QGrams().tokenize('').get_counter(), QGrams().tokenize('neilsen').get_counter(), )
        == 1
    )
    assert cmp.dist_abs(
            QGrams().tokenize('nelson').get_counter(),
            QGrams().tokenize('neilsen').get_counter(),
        ) == pytest.approx(abs=1e-7, expected=1)

    # non-q-gram tests
    assert cmp_ws.dist_abs('', '') == 0
    assert cmp_ws.dist_abs('the quick', '') == 1
    assert cmp_ws.dist_abs('', 'the quick') == 1
    assert cmp_ws.dist_abs(NONQ_FROM, NONQ_TO) == pytest.approx(abs=1e-7, expected=1)
    assert cmp_ws.dist_abs(NONQ_TO, NONQ_FROM) == pytest.approx(abs=1e-7, expected=1)

def test_chebyshev_dist():
    """Test abydos.distance.Chebyshev.dist."""
    with pytest.raises(NotImplementedError):
        cmp.dist()

def test_chebyshev_sim():
    """Test abydos.distance.Chebyshev.sim."""
    with pytest.raises(NotImplementedError):
        cmp.sim()
