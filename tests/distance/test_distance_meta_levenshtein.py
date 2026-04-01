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

"""abydos.tests.distance.test_distance_meta_levenshtein.

This module contains unit tests for abydos.distance.MetaLevenshtein
"""

import pytest

import os
import urllib.error

from abydos.corpus import UnigramCorpus
from abydos.distance import Jaccard, MetaLevenshtein
from abydos.tokenizer import QGrams
from abydos.util import download_package, package_path


cmp = MetaLevenshtein()

cmp_jac1 = MetaLevenshtein(metric=Jaccard(qval=1))


def test_meta_levenshtein_dist():
    """Test abydos.distance.MetaLevenshtein.dist."""
    # Base cases
    assert cmp.dist('', '') == 0.0
    assert cmp.dist('a', '') == 1.0
    assert cmp.dist('', 'a') == 1.0
    assert cmp.dist('abc', '') == 1.0
    assert cmp.dist('', 'abc') == 1.0
    assert cmp.dist('abc', 'abc') == 0.0
    assert cmp.dist('abcd', 'efgh') == 0.8463953614713058

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.3077801314)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.3077801314)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.3077801314)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.3077801314)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.2931752664)

def test_meta_levenshtein_sim():
    """Test abydos.distance.MetaLevenshtein.sim."""
    # Base cases
    assert cmp.sim('', '') == 1.0
    assert cmp.sim('a', '') == 0.0
    assert cmp.sim('', 'a') == 0.0
    assert cmp.sim('abc', '') == 0.0
    assert cmp.sim('', 'abc') == 0.0
    assert cmp.sim('abc', 'abc') == 1.0
    assert cmp.sim('abcd', 'efgh') == 0.15360463852869422

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.6922198686)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.6922198686)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.6922198686)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.6922198686)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.7068247336)

    assert cmp_jac1.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.569107816)
    assert cmp_jac1.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.569107816)
    assert cmp_jac1.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.753775895)
    assert cmp_jac1.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.753775895)
    assert cmp_jac1.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.5746789477)

def test_meta_levenshtein_dist_abs():
    """Test abydos.distance.MetaLevenshtein.dist_abs."""
    # Base cases
    assert cmp.dist_abs('', '') == 0.0
    assert cmp.dist_abs('a', '') == 1.0
    assert cmp.dist_abs('', 'a') == 1.0
    assert cmp.dist_abs('abc', '') == 3.0
    assert cmp.dist_abs('', 'abc') == 3.0
    assert cmp.dist_abs('abc', 'abc') == 0.0
    assert cmp.dist_abs('abcd', 'efgh') == 3.385581445885223

    assert cmp.dist_abs('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=1.5389006572)
    assert cmp.dist_abs('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=1.5389006572)
    assert cmp.dist_abs('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=1.5389006572)
    assert cmp.dist_abs('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=1.5389006572)
    assert cmp.dist_abs('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=2.9317526638)

def test_meta_levenshtein_corpus():
    """Test abydos.distance.MetaLevenshtein with corpus."""
    q3_corpus = UnigramCorpus(word_tokenizer=QGrams(qval=3))
    try:
        download_package('en_qgram', silent=True)
    except urllib.error.URLError as exc:
        pytest.skip('abydos-data index unavailable: {}'.format(exc))
    q3_corpus.load_corpus(
        os.path.join(package_path('en_qgram'), 'q3_en.dat')
    )
    cmp_q3 = MetaLevenshtein(tokenizer=QGrams(qval=3), corpus=q3_corpus)

    assert cmp_q3.dist_abs('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=7.378939370)
    assert cmp_q3.dist_abs('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=7.378939370)
    assert cmp_q3.dist_abs('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=8.0)
    assert cmp_q3.dist_abs('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=8.0)

    assert cmp_q3.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.527067098)
    assert cmp_q3.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.527067098)
    assert cmp_q3.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.571428571)
    assert cmp_q3.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.571428571)

    assert cmp_q3.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.472932902)
    assert cmp_q3.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.472932902)
    assert cmp_q3.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.428571429)
    assert cmp_q3.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.428571429)
