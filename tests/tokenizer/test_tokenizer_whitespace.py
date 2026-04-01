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


from abydos.tokenizer import WhitespaceTokenizer


def test_whitespace_tokenizer():
    """Test abydos.tokenizer.WhitespaceTokenizer."""
    assert sorted(WhitespaceTokenizer().tokenize('').get_list()) == []
    assert sorted(WhitespaceTokenizer().tokenize('a').get_list()) == ['a']

    assert (
        sorted(WhitespaceTokenizer().tokenize('NELSON').get_list())
        == sorted(['NELSON'])
    )
    assert (
        sorted(WhitespaceTokenizer().tokenize('NEILSEN').get_list())
        == sorted(['NEILSEN'])
    )

    tweet = 'Good to be home for a night. Even better to see the\
    @chicagobulls start the season off right! #SeeRed'
    assert (
        sorted(WhitespaceTokenizer().tokenize(tweet).get_list())
        == sorted( [ 'Good', 'to', 'be', 'home', 'for', 'a', 'night.', 'Even', 'better', 'to', 'see', 'the', '@chicagobulls', 'start', 'the', 'season', 'off', 'right!', '#SeeRed', ] )
    )
