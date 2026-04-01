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

"""abydos.tests.compression.test_compression_bwt.

This module contains unit tests for abydos.compression.BWT
"""


import pytest

from abydos.compression import BWT


coder = BWT()

coder_pipe = BWT('|')

coder_dollar = BWT('$')


def test_bwt_encode():
    """Test abydos.compression.BWT.encode."""
    # Examples from Wikipedia entry on BWT
    assert coder.encode('') == '\x00'
    assert coder_pipe.encode('^BANANA') == 'BNN^AA|A'
    assert (
        coder_pipe.encode( 'SIX.MIXED.PIXIES.SIFT.SIXTY.PIXIE.DUST.BOXES' )
        == 'TEXYDST.E.IXIXIXXSSMPPS.B..E.|.UESFXDIIOIIITS'
    )

    assert coder_dollar.encode('aardvark') == 'k$avrraad'

    with pytest.raises(ValueError):
        coder_dollar.encode('ABC$')
    with pytest.raises(ValueError):
        coder.encode('ABC\0')

def test_bwt_decode():
    """Test abydos.compression.BWT.decode."""
    assert coder.decode('') == ''
    assert coder.decode('\x00') == ''
    assert coder_pipe.decode('BNN^AA|A') == '^BANANA'
    assert (
        coder_pipe.decode( 'TEXYDST.E.IXIXIXXSSMPPS.B..E.|.UESFXDIIOIIITS' )
        == 'SIX.MIXED.PIXIES.SIFT.SIXTY.PIXIE.DUST.BOXES'
    )

    assert coder_dollar.decode('k$avrraad') == 'aardvark'

    with pytest.raises(ValueError):
        coder_dollar.decode('ABC')
    with pytest.raises(ValueError):
        coder.decode('ABC')

def test_bwt_roundtripping():
    """Test abydos.compression.BWT.encode & .decode roundtripping."""
    for w in (
        '',
        'Banana',
        'The quick brown fox, etc.',
        'it is better a chylde unborne than untaught',
        'manners maketh man',
        'בְּרֵאשִׁית, בָּרָא אֱלֹהִים',
        'Ein Rückblick bietet sich folglich an.',
    ):
        assert coder.decode(coder.encode(w)) == w
        assert coder_dollar.decode(coder_dollar.encode(w)) == w
