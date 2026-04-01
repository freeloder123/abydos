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

"""abydos.tests.tokenizer.test_tokenizer_c_or_v_cluster.

This module contains unit tests for abydos.tokenizer.COrVClusterTokenizer
"""


from abydos.tokenizer import COrVClusterTokenizer


def test_c_or_v_cluster_tokenizer():
    """Test abydos.tokenizer.COrVClusterTokenizer."""
    assert sorted(COrVClusterTokenizer().tokenize('').get_list()) == []
    assert sorted(COrVClusterTokenizer().tokenize('a').get_list()) == ['a']

    tok = COrVClusterTokenizer()

    assert (
        sorted(tok.tokenize('nelson').get_list())
        == sorted(['n', 'e', 'ls', 'o', 'n'])
    )
    assert (
        sorted(tok.tokenize('neilson').get_list())
        == sorted(['n', 'ei', 'ls', 'o', 'n'])
    )
    assert (
        sorted(tok.tokenize('peninsular').get_list())
        == sorted(['p', 'e', 'n', 'i', 'ns', 'u', 'l', 'a', 'r'])
    )
    assert (
        sorted(tok.tokenize('spectacular').get_list())
        == sorted(['sp', 'e', 'ct', 'a', 'c', 'u', 'l', 'a', 'r'])
    )
    assert (
        sorted(tok.tokenize('sufficiently').get_list())
        == sorted(['s', 'u', 'ff', 'i', 'c', 'ie', 'ntl', 'y'])
    )
    assert (
        sorted(tok.tokenize('yachting').get_list())
        == sorted(['ya', 'cht', 'i', 'ng'])
    )
    assert (
        sorted(tok.tokenize('caterpillars').get_list())
        == sorted(['c', 'a', 't', 'e', 'rp', 'i', 'll', 'a', 'rs'])
    )
    assert (
        sorted(tok.tokenize('Götterdämmerung').get_list())
        == sorted( ['G', 'ö', 'tt', 'e', 'rd', 'ä', 'mm', 'e', 'r', 'u', 'ng'] )
    )

    tok = COrVClusterTokenizer(consonants='ptkbdgmn', vowels='aeiouwy')
    assert (
        sorted(tok.tokenize('#winning #losing').get_list())
        == sorted(['#', 'wi', 'nn', 'i', 'ng', '#', 'losing'])
    )
