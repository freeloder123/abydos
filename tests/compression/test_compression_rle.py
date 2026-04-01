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

"""abydos.tests.compression.test_compression_rle.

This module contains unit tests for abydos.compression.RLE
"""


from abydos.compression import BWT, RLE


rle = RLE()

bwt = BWT()

bws = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'


def test_rle_encode():
    """Test abydos.compression.RLE.encode."""
    assert rle.encode('') == ''
    assert rle.encode(bwt.encode('')) == '\x00'
    assert rle.encode('banana') == 'banana'
    assert rle.encode(bwt.encode('banana')) == 'annb\x00aa'
    assert rle.encode(bws) == '12WB12W3B24WB14W'
    assert rle.encode(bwt.encode(bws)) == 'WWBWWB45WB\x003WB10WB'
    assert rle.encode('Schifffahrt') == 'Schi3fahrt'

def test_rle_decode():
    """Test abydos.compression.RLE.decode."""
    assert rle.decode('') == ''
    assert bwt.decode(rle.decode('\x00')) == ''
    assert rle.decode('banana') == 'banana'
    assert bwt.decode(rle.decode('annb\x00aa')) == 'banana'
    assert rle.decode('12WB12W3B24WB14W') == bws
    assert rle.decode('12W1B12W3B24W1B14W') == bws
    assert bwt.decode(rle.decode('WWBWWB45WB\x003WB10WB')) == bws
    assert rle.decode('Schi3fahrt') == 'Schifffahrt'

def test_rle_roundtripping():
    """Test abydos.compression.RLE.encode & .decode roundtripping."""
    assert rle.decode(rle.encode('')) == ''
    assert (
        bwt.decode( rle.decode(rle.encode(bwt.encode(''))) )
        == ''
    )
    assert rle.decode(rle.encode('banana')) == 'banana'
    assert (
        bwt.decode( rle.decode(rle.encode(bwt.encode('banana'))) )
        == 'banana'
    )
    assert rle.decode(rle.encode(bws)) == bws
    assert (
        bwt.decode( rle.decode(rle.encode(bwt.encode(bws))) )
        == bws
    )
    assert rle.decode(rle.encode('Schifffahrt')) == 'Schifffahrt'
    assert (
        bwt.decode( rle.decode( rle.encode(bwt.encode('Schifffahrt')) ) )
        == 'Schifffahrt'
    )
