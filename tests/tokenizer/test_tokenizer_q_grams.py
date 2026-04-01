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

"""abydos.tests.tokenizer.test_tokenizer_q_grams.

This module contains unit tests for abydos.tokenizer.QGrams
"""

import pytest

import sys
from collections import Counter
from math import log1p

from abydos.tokenizer import QGrams


def test_qgrams():
    """Test abydos.tokenizer.QGrams."""
    assert sorted(QGrams().tokenize('').get_list()) == []
    assert sorted(QGrams(2).tokenize('a').get_list()) == ['$a', 'a#']
    assert sorted(QGrams(-1).tokenize('NELSON').get_list()) == []

    assert (
        sorted(QGrams(3).tokenize('NELSON').get_list())
        == sorted(['$$N', '$NE', 'NEL', 'ELS', 'LSO', 'SON', 'ON#', 'N##'])
    )
    assert (
        sorted(QGrams(7).tokenize('NELSON').get_list())
        == sorted( [ '$$$$$$N', '$$$$$NE', '$$$$NEL', '$$$NELS', '$$NELSO', '$NELSON', 'ELSON##', 'LSON###', 'N######', 'NELSON#', 'ON#####', 'SON####', ] )
    )

    # http://www.sound-ex.com/alternative_qgram.htm
    assert (
        sorted(QGrams().tokenize('NELSON').get_list())
        == sorted(['$N', 'NE', 'EL', 'LS', 'SO', 'ON', 'N#'])
    )
    assert (
        sorted(QGrams().tokenize('NEILSEN').get_list())
        == sorted(['$N', 'NE', 'EI', 'IL', 'LS', 'SE', 'EN', 'N#'])
    )
    assert (
        sorted(QGrams(start_stop='').tokenize('NELSON').get_list())
        == sorted(['NE', 'EL', 'LS', 'SO', 'ON'])
    )
    assert (
        sorted(QGrams(start_stop='').tokenize('NEILSEN').get_list())
        == sorted(['NE', 'EI', 'IL', 'LS', 'SE', 'EN'])
    )

    # qval=(1,2)
    assert (
        sorted(QGrams(qval=(1, 2)).tokenize('NELSON').get_list())
        == sorted( [ '$N', 'E', 'EL', 'L', 'LS', 'N', 'N', 'N#', 'NE', 'O', 'ON', 'S', 'SO', ] )
    )
    assert (
        sorted(QGrams(qval=(2, 1)).tokenize('NELSON').get_list())
        == sorted( [ '$N', 'E', 'EL', 'L', 'LS', 'N', 'N', 'N#', 'NE', 'O', 'ON', 'S', 'SO', ] )
    )
    assert (
        sorted(QGrams(qval=range(3)).tokenize('NELSON').get_list())
        == sorted( [ '$N', 'E', 'EL', 'L', 'LS', 'N', 'N', 'N#', 'NE', 'O', 'ON', 'S', 'SO', ] )
    )
    assert QGrams(qval=(1, 2)).tokenize('NELSON').count() == 13

    # skip=(1,2)
    assert (
        sorted(QGrams(skip=(2, 1, 0)).tokenize('NELSON').get_list())
        == sorted( [ '$E', '$L', '$N', 'EL', 'EO', 'ES', 'LN', 'LO', 'LS', 'N', 'N', 'N#', 'NE', 'NL', 'NS', 'O', 'O#', 'ON', 'S#', 'SN', 'SO', ] )
    )
    assert (
        sorted(QGrams(skip=(2, 1, 0)).tokenize('NELSON').get_list())
        == sorted( [ '$E', '$L', '$N', 'EL', 'EO', 'ES', 'LN', 'LO', 'LS', 'N', 'N', 'N#', 'NE', 'NL', 'NS', 'O', 'O#', 'ON', 'S#', 'SN', 'SO', ] )
    )
    assert (
        sorted(QGrams(skip=range(3)).tokenize('NELSON').get_list())
        == sorted( [ '$E', '$L', '$N', 'EL', 'EO', 'ES', 'LN', 'LO', 'LS', 'N', 'N', 'N#', 'NE', 'NL', 'NS', 'O', 'O#', 'ON', 'S#', 'SN', 'SO', ] )
    )
    assert QGrams(skip=(0, 1, 2)).tokenize('NELSON').count() == 21
    assert (
        QGrams(qval=1).tokenize('COLIN').get_counter()
        == Counter({'C': 1, 'O': 1, 'L': 1, 'I': 1, 'N': 1})
    )
    assert (
        QGrams(qval=10, start_stop='').tokenize('COLIN').get_counter()
        == Counter({})
    )
    if sys.version_info >= (3, 6):
        assert (
            repr(QGrams(qval=1).tokenize('COLIN'))
            == "QGrams({'C': 1, 'O': 1, 'L': 1, 'I': 1, 'N': 1})"
        )
    assert (
        QGrams(qval=1).tokenize('COLIN').get_set()
        == {'C', 'O', 'L', 'I', 'N'}
    )

    # Test exception
    with pytest.raises(ValueError):
        QGrams(0)

def test_qgrams_intersections():
    """Test abydos.tokenizer.QGrams intersections."""
    assert sorted(QGrams().tokenize('NELSON') & QGrams().tokenize('')) == []
    assert sorted(QGrams().tokenize('') & QGrams().tokenize('NEILSEN')) == []
    assert (
        sorted(QGrams().tokenize('NELSON') & QGrams().tokenize('NEILSEN'))
        == sorted(['$N', 'NE', 'LS', 'N#'])
    )
    assert (
        sorted(QGrams().tokenize('NELSON') & QGrams().tokenize('NOSLEN'))
        == sorted(['$N', 'N#'])
    )
    assert sorted(QGrams().tokenize('NAIL') & QGrams().tokenize('LIAN')) == []

    assert (
        sorted( QGrams(start_stop='').tokenize('NELSON') & QGrams(start_stop='').tokenize('NEILSEN') )
        == sorted(['NE', 'LS'])
    )
    assert (
        sorted( QGrams(start_stop='').tokenize('NELSON') & QGrams(start_stop='').tokenize('NOSLEN') )
        == []
    )
    assert (
        sorted( QGrams(start_stop='').tokenize('NAIL') & QGrams(start_stop='').tokenize('LIAN') )
        == []
    )

def test_qgrams_counts():
    """Test abydos.tokenizer.QGrams counts."""
    assert QGrams().tokenize('').count() == 0
    assert len(QGrams().tokenize('').get_list()) == 0

    assert QGrams().tokenize('NEILSEN').count() == 8
    assert QGrams().tokenize('NELSON').count() == 7
    assert QGrams(start_stop='').tokenize('NEILSEN').count() == 6
    assert QGrams(start_stop='').tokenize('NELSON').count() == 5

    assert len(QGrams().tokenize('NEILSEN').get_list()) == 8
    assert len(QGrams().tokenize('NELSON').get_list()) == 7
    assert len(QGrams(start_stop='').tokenize('NEILSEN').get_list()) == 6
    assert len(QGrams(start_stop='').tokenize('NELSON').get_list()) == 5

    assert (
        QGrams(scaler='set').tokenize('ACAACACCTAG').get_counter()
        == Counter( { '$A': 1, 'AC': 1, 'CA': 1, 'AA': 1, 'CC': 1, 'CT': 1, 'TA': 1, 'AG': 1, 'G#': 1, } )
    )

    gold_standard = Counter(
        {
            '$A': 0.6931471805599453,
            'AC': 1.3862943611198906,
            'CA': 1.0986122886681096,
            'AA': 0.6931471805599453,
            'CC': 0.6931471805599453,
            'CT': 0.6931471805599453,
            'TA': 0.6931471805599453,
            'AG': 0.6931471805599453,
            'G#': 0.6931471805599453,
        }
    )
    test_counter = (
        QGrams(scaler=log1p).tokenize('ACAACACCTAG').get_counter()
    )
    for key in test_counter:
        assert test_counter[key] == pytest.approx(abs=1e-7, expected=gold_standard[key])

    assert QGrams(scaler=log1p).tokenize('ACAACACCTAG').count_unique() == 9

    tokens1 = QGrams().tokenize('ACAACACCTAG')
    tokens2 = QGrams().tokenize('GAAGATAC')
    assert (
        tokens1 - tokens2
        == Counter({'$A': 1, 'AC': 2, 'CA': 2, 'CC': 1, 'CT': 1, 'G#': 1})
    )
    assert (
        tokens1 + tokens2
        == Counter( { '$A': 1, 'AC': 4, 'CA': 2, 'AA': 2, 'CC': 1, 'CT': 1, 'TA': 2, 'AG': 2, 'G#': 1, '$G': 1, 'GA': 2, 'AT': 1, 'C#': 1, } )
    )
