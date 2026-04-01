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


from abydos.tokenizer import SonoriPyTokenizer


def test_sonoripy_tokenizer():
    """Test abydos.tokenizer.SonoriPyTokenizer."""
    try:
        from syllabipy.sonoripy import SonoriPy  # noqa: F401
    except ImportError:  # pragma: no cover
        return

    assert sorted(SonoriPyTokenizer().tokenize('').get_list()) == ['']
    assert sorted(SonoriPyTokenizer().tokenize('a').get_list()) == ['a']

    tok = SonoriPyTokenizer()

    assert sorted(tok.tokenize('nelson').get_list()) == sorted(['nel', 'son'])
    assert (
        sorted(tok.tokenize('neilson').get_list())
        == sorted(['neil', 'son'])
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
        == sorted(['suf', 'fi', 'cien', 'tly'])
    )
    assert (
        sorted(tok.tokenize('yachting').get_list())
        == sorted(['yach', 'ting'])
    )
    assert (
        sorted(tok.tokenize('caterpillars').get_list())
        == sorted(['ca', 'ter', 'pil', 'lars'])
    )
