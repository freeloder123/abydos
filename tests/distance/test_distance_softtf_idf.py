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

"""abydos.tests.distance.test_distance_softtf_idf.

This module contains unit tests for abydos.distance.SoftTFIDF
"""

import pytest

import os
import urllib.error

from abydos.corpus import UnigramCorpus
from abydos.distance import Levenshtein, SoftTFIDF
from abydos.tokenizer import QGrams
from abydos.util import download_package, package_path


cmp = SoftTFIDF()

cmp_lev = SoftTFIDF(metric=Levenshtein())


def test_softtf_idf_sim():
    """Test abydos.distance.SoftTFIDF.sim."""
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

    assert cmp_lev.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.304044497)
    assert cmp_lev.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.304044497)
    assert cmp_lev.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.304044497)
    assert cmp_lev.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.304044497)
    assert cmp_lev.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.4676712137)

def test_softtf_idf_dist():
    """Test abydos.distance.SoftTFIDF.dist."""
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

def test_softtf_idf_corpus():
    """Test abydos.distance.SoftTFIDF.sim & .dist with corpus."""
    try:
        download_package('en_qgram', silent=True)
    except urllib.error.URLError as exc:
        pytest.skip('abydos-data index unavailable: {}'.format(exc))

    q3_corpus = UnigramCorpus(word_tokenizer=QGrams(qval=3))
    q3_corpus.load_corpus(
        os.path.join(package_path('en_qgram'), 'q3_en.dat')
    )
    cmp_q3_08 = SoftTFIDF(
        tokenizer=QGrams(qval=3), corpus=q3_corpus, threshold=0.8
    )
    cmp_q3_03 = SoftTFIDF(
        tokenizer=QGrams(qval=3), corpus=q3_corpus, threshold=0.3
    )

    assert cmp_q3_08.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.608842672)
    assert cmp_q3_08.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.608842672)
    assert cmp_q3_08.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.383052250)
    assert cmp_q3_08.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.383052250)

    # These values won't be stable, so we just use Greater/Less
    assert cmp_q3_03.sim('Nigel', 'Niall') > 0.5
    assert cmp_q3_03.sim('Niall', 'Nigel') > 0.5
    assert cmp_q3_03.sim('Colin', 'Coiln') > 0.5
    assert cmp_q3_03.sim('Coiln', 'Colin') > 0.5

    assert cmp_q3_08.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.391157328)
    assert cmp_q3_08.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.391157328)
    assert cmp_q3_08.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.616947750)
    assert cmp_q3_08.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.616947750)

    # These values won't be stable, so we just use Greater/Less
    assert cmp_q3_03.dist('Nigel', 'Niall') < 0.5
    assert cmp_q3_03.dist('Niall', 'Nigel') < 0.5
    assert cmp_q3_03.dist('Colin', 'Coiln') < 0.5
    assert cmp_q3_03.dist('Coiln', 'Colin') < 0.5
