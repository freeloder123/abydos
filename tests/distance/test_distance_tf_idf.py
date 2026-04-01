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

"""abydos.tests.distance.test_distance_tf_idf.

This module contains unit tests for abydos.distance.TFIDF
"""

import pytest

import os
import urllib.error

from abydos.corpus import UnigramCorpus
from abydos.distance import TFIDF
from abydos.tokenizer import QGrams
from abydos.util import download_package, package_path


cmp = TFIDF()


def test_tf_idf_sim():
    """Test abydos.distance.TFIDF.sim."""
    # Base cases
    assert cmp.sim('', '') == 0.0
    assert cmp.sim('a', '') == 0.0
    assert cmp.sim('', 'a') == 0.0
    assert cmp.sim('abc', '') == 0.0
    assert cmp.sim('', 'abc') == 0.0
    assert cmp.sim('abc', 'abc') == 1.0
    assert cmp.sim('abcd', 'efgh') == 0.0

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.304044497)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.304044497)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.304044497)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.304044497)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.4676712137)

def test_tf_idf_dist():
    """Test abydos.distance.TFIDF.dist."""
    # Base cases
    assert cmp.dist('', '') == 1.0
    assert cmp.dist('a', '') == 1.0
    assert cmp.dist('', 'a') == 1.0
    assert cmp.dist('abc', '') == 1.0
    assert cmp.dist('', 'abc') == 1.0
    assert cmp.dist('abc', 'abc') == 0.0
    assert cmp.dist('abcd', 'efgh') == 1.0

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.695955503)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.695955503)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.695955503)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.695955503)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.5323287863)

def test_tf_idf_corpus():
    """Test abydos.distance.TFIDF.sim & .dist with corpus."""
    q3_corpus = UnigramCorpus(word_tokenizer=QGrams(qval=3))
    try:
        download_package('en_qgram', silent=True)
    except urllib.error.URLError as exc:
        pytest.skip('abydos-data index unavailable: {}'.format(exc))
    q3_corpus.load_corpus(
        os.path.join(package_path('en_qgram'), 'q3_en.dat')
    )
    cmp_q3 = TFIDF(tokenizer=QGrams(qval=3), corpus=q3_corpus)

    assert cmp_q3.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.259985047)
    assert cmp_q3.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.259985047)
    assert cmp_q3.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.114867563)
    assert cmp_q3.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.114867563)

    assert cmp_q3.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.740014953)
    assert cmp_q3.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.740014953)
    assert cmp_q3.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.885132437)
    assert cmp_q3.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.885132437)
