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

"""abydos.tests.distance.test_distance_q_gram.

This module contains unit tests for abydos.distance.QGram
"""


import pytest

from abydos.distance import QGram
from abydos.tokenizer import WhitespaceTokenizer


cmp = QGram()

cmp_q1 = QGram(qval=1)

cmp_ws = QGram(tokenizer=WhitespaceTokenizer())


def test_q_gram_dist():
    """Test abydos.distance.QGram.dist."""
    # Base cases
    assert cmp.dist('', '') == 0.0
    assert cmp.dist('a', '') == 0.0
    assert cmp.dist('', 'a') == 0.0
    assert cmp.dist('abc', '') == 1.0
    assert cmp.dist('', 'abc') == 1.0
    assert cmp.dist('abc', 'abc') == 0.0
    assert cmp.dist('abcd', 'efgh') == 1.0

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.8571428571)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.8571428571)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.8571428571)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.8571428571)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.4545454545)

def test_q_gram_sim():
    """Test abydos.distance.QGram.sim."""
    # Base cases
    assert cmp.sim('', '') == 1.0
    assert cmp.sim('a', '') == 1.0
    assert cmp.sim('', 'a') == 1.0
    assert cmp.sim('abc', '') == 0.0
    assert cmp.sim('', 'abc') == 0.0
    assert cmp.sim('abc', 'abc') == 1.0
    assert cmp.sim('abcd', 'efgh') == 0.0

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.1428571429)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.1428571429)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.1428571429)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.1428571429)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.5454545455)

def test_q_gram_dist_abs():
    """Test abydos.distance.QGram.dist_abs."""
    # Base cases
    assert cmp.dist_abs('', '') == 0
    assert cmp.dist_abs('a', '') == 0
    assert cmp.dist_abs('', 'a') == 0
    assert cmp.dist_abs('abc', '') == 2
    assert cmp.dist_abs('', 'abc') == 2
    assert cmp.dist_abs('abc', 'abc') == 0
    assert cmp.dist_abs('abcd', 'efgh') == 6

    assert cmp.dist_abs('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=6)
    assert cmp.dist_abs('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=6)
    assert cmp.dist_abs('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=6)
    assert cmp.dist_abs('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=6)
    assert cmp.dist_abs('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=5)

    # Example from paper
    assert cmp.dist_abs('01000', '001111') == 5

    # Coverage
    assert cmp_q1.dist_abs('01000', '001111') == 5
    assert cmp_ws.dist_abs('a a b b c', 'a b b b c d') == 3
