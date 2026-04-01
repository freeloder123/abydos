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

"""abydos.tests.tokenizer.test_tokenizer_qgrams.

This module contains unit tests for abydos.tokenizer.QGrams
"""


from abydos.tokenizer import LegaliPyTokenizer

from .. import _corpus_file


def test_legalipy_tokenizer():
    """Test abydos.tokenizer.LegaliPyTokenizer."""
    try:
        from syllabipy.legalipy import LegaliPy  # noqa: F401
    except ImportError:  # pragma: no cover
        return

    assert sorted(LegaliPyTokenizer().tokenize('').get_list()) == ['']
    assert sorted(LegaliPyTokenizer().tokenize('a').get_list()) == ['a']

    assert (
        sorted(LegaliPyTokenizer().tokenize('nelson').get_list())
        == sorted(['n', 'els', 'on'])
    )
    assert (
        sorted(LegaliPyTokenizer().tokenize('neilson').get_list())
        == sorted(['n', 'eils', 'on'])
    )

    tok = LegaliPyTokenizer()
    with open(_corpus_file('wikipediaCommonMisspellings.csv')) as corpus:
        text = ' '.join([_.split(',')[1] for _ in corpus.readlines()])
    tok.train_onsets(text)

    with open(_corpus_file('misspellings.csv')) as corpus:
        text = ' '.join([_.split(',')[1] for _ in corpus.readlines()])
    tok.train_onsets(text, append=True)

    assert sorted(tok.tokenize('nelson').get_list()) == sorted(['nel', 'son'])
    assert (
        sorted(tok.tokenize('neilson').get_list())
        == sorted(['ne', 'il', 'son'])
    )
    assert (
        sorted(tok.tokenize('peninsular').get_list())
        == sorted(['pe', 'nin', 'su', 'lar'])
    )
    assert (
        sorted(tok.tokenize('spectacular').get_list())
        == sorted(['spec', 'ta', 'cu', 'lar'])
    )
    assert (
        sorted(tok.tokenize('sufficiently').get_list())
        == sorted(['suf', 'fi', 'ci', 'ent', 'ly'])
    )
    assert (
        sorted(tok.tokenize('yachting').get_list())
        == sorted(['y', 'ach', 'ting'])
    )
    assert (
        sorted(tok.tokenize('caterpillars').get_list())
        == sorted(['ca', 'ter', 'pil', 'lars'])
    )
