# Copyright 2018-2020 by Christopher C. Little.
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

"""abydos.tests.phonetic.test_phonetic_eudex.

This module contains unit tests for abydos.phonetic.Eudex
"""

from abydos.phonetic import Eudex


pa = Eudex()

def test_eudex():
    """Test abydos.phonetic.Eudex."""
    # base cases
    assert pa.encode('') == '18374686479671623680'
    assert pa.encode(' ') == '18374686479671623680'

    # exact & mismatch cases from
    # https://github.com/ticki/eudex/blob/master/src/tests.rs
    assert pa.encode('JAva') == pa.encode('jAva')
    assert pa.encode('co!mputer') == pa.encode('computer'
    )
    assert pa.encode('comp-uter') == pa.encode('computer'
    )
    assert pa.encode('comp@u#te?r') == pa.encode('computer'
    )
    assert pa.encode('lal') == pa.encode('lel')
    assert pa.encode('rindom') == pa.encode('ryndom')
    assert pa.encode('riiiindom') == pa.encode('ryyyyyndom'
    )
    assert pa.encode('riyiyiiindom') == pa.encode('ryyyyyndom'
    )
    assert pa.encode('triggered') == pa.encode('TRIGGERED'
    )
    assert pa.encode('repert') == pa.encode('ropert')

    assert pa.encode('reddit') != pa.encode('eddit')
    assert pa.encode('lol') != pa.encode('lulz')
    assert pa.encode('ijava') != pa.encode('java')
    assert pa.encode('jiva') != pa.encode('java')
    assert pa.encode('jesus') != pa.encode('iesus')
    assert pa.encode('aesus') != pa.encode('iesus')
    assert pa.encode('iesus') != pa.encode('yesus')
    assert pa.encode('rupirt') != pa.encode('ropert')
    assert pa.encode('ripert') != pa.encode('ropyrt')
    assert pa.encode('rrr') != pa.encode('rraaaa')
    assert pa.encode('randomal') != pa.encode('randomai'
    )

    # manually checked against algorithm
    assert pa.encode('guillaume') == '288230383131034112'
    assert pa.encode('niall') == '648518346341351840'
    assert pa.encode('hello') == '144115188075896832'
    assert pa.encode('christopher') == '433648490138894409'
    assert pa.encode('colin') == '432345564238053650'
