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


from abydos.tokenizer import WordpunctTokenizer


def test_wordpunct_tokenizer():
    """Test abydos.tokenizer.WordpunctTokenizer."""
    assert sorted(WordpunctTokenizer().tokenize('').get_list()) == []
    assert sorted(WordpunctTokenizer().tokenize('a').get_list()) == ['a']

    assert (
        sorted(WordpunctTokenizer().tokenize('NELSON').get_list())
        == sorted(['NELSON'])
    )
    assert (
        sorted(WordpunctTokenizer().tokenize('NEILSEN').get_list())
        == sorted(['NEILSEN'])
    )

    tweet = 'I got a chance to catch up with the @Space_Station crew\
    today. Nothing like a call to space on #AstronomyNight!'
    assert (
        sorted(WordpunctTokenizer().tokenize(tweet).get_list())
        == sorted( [ 'I', 'got', 'a', 'chance', 'to', 'catch', 'up', 'with', 'the', '@', 'Space_Station', 'crew', 'today', '.', 'Nothing', 'like', 'a', 'call', 'to', 'space', 'on', '#', 'AstronomyNight', '!', ] )
    )
