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

"""abydos.tests.fingerprint.test_fingerprint_synoname_toolcode.

This module contains unit tests for abydos.fingerprint.SynonameToolcode
"""


from abydos.fingerprint import SynonameToolcode


fp = SynonameToolcode()


def test_synoname_toolcode():
    """Test abydos.fingerprint.SynonameToolcode."""
    # Base case
    assert fp.fingerprint('') == ',,0000000000$$'

    # from Synoname demo
    assert (
        fp.fingerprint('angelico', 'fra')
        == 'angelico,fra,0000000308$044a$af'
    )
    assert (
        fp.fingerprint('Aelst', 'Willem van', '')
        == 'aelst,willem van,0000001005$143a$awv'
    )
    assert fp.fingerprint('Afro') == 'afro,,0000000004$$a'
    assert (
        fp.fingerprint('Afro', 'Basaldella')
        == 'afro,basaldella,0000001004$$ab'
    )
    assert fp.fingerprint('Albright', 'Ivan') == 'albright,ivan,0000000408$$ai'
    assert (
        fp.fingerprint('Antonello da Messina')
        == 'antonello da messina,,0000000020$022b$adm'
    )
    assert (
        fp.fingerprint('Albright', 'Ivan Le Lorraine')
        == 'albright,ivan le lorraine,0000001608$067b$ail'
    )
    assert (
        fp.fingerprint('Bazille', 'Frederic', 'Attributed to')
        == 'bazille,frederic,1000000807$$bf'
    )
    assert (
        fp.fingerprint('Bazille', 'Frederick', 'Attributed to')
        == 'bazille,frederick,1000000907$$bf'
    )
    assert (
        fp.fingerprint('Beerstraaten', 'Jan Abrahamsz.')
        == 'beerstraaten,jan abrahamsz.,0200001412$$bja'
    )
    assert (
        fp.fingerprint('Bonifacio di Pitati')
        == 'bonifacio di pitati,,0000000019$035b$bdp'
    )
    assert (
        fp.fingerprint('Breughel the Younger', 'Jan')
        == 'breughel the younger,jan,0020000320$134b$btyj'
    )
    assert fp.fingerprint('Brown', 'W. W.') == 'brown,w. w.,0200000505$$bw'
    assert (
        fp.fingerprint('Brueghel II (the Younger)', 'Jan')
        == 'brueghel ii (the younger),jan,0120490325$049b134b$bityj'
    )
    assert (
        fp.fingerprint( 'Brueghel II (the Younger)', 'Pieter', 'Workshop of' )
        == 'brueghel ii (the younger),pieter,3120490625$049b134b$bityp'
    )
    assert (
        fp.fingerprint('Bugiardini', 'Guiliano di Piero di Simone')
        == 'bugiardini,guiliano di piero di simone,0000002710$035b035b$bgdps'
    )
    assert (
        fp.fingerprint('Caravaggio', '', 'Follower of')
        == 'caravaggio,,3000000010$$c'
    )
    assert (
        fp.fingerprint( 'Caravaggio', 'Michelangelo Merisi da', 'Follower of' )
        == 'caravaggio,michelangelo merisi da,3000002210$022a$cmd'
    )
    assert (
        fp.fingerprint('Oost the Younger', 'Jacob van')
        == 'oost the younger,jacob van,0020000916$134b143a$otyjv'
    )

    # additional tests for coverage
    assert (
        fp.fingerprint('Cato the Elder', '', 'Copy of')
        == 'cato the elder,,2010000014$133b$cte'
    )
    assert (
        fp.fingerprint('Cato, the Elder', normalize=2)
        == 'cato the elder,,0110000014$133b$cte'
    )
    assert (
        fp.fingerprint('Cato the Elder', normalize=2)
        == 'cato the elder,,0010000014$133b$cte'
    )
    assert (
        fp.fingerprint( 'Lorem ipsum dolor sit amet, ' + 'consectetur adipiscing elit, ' + 'sed do eiusmod tempor ' + 'incididunt ut labore et dolore ' + 'magna aliqua. Nulla aliquet ' + 'porttitor lacus luctus accumsan ' + 'tortor posuere. Egestas purus ' + 'viverra accumsan in. Ultrices ' + 'mi tempus imperdiet nulla ' + 'malesuada pellentesque elit ' + 'eget gravida. Proin libero nunc ' + 'consequat interdum varius sit ' + 'amet mattis vulputate. Mauris ' + 'ultrices eros in cursus turpis ' + 'massa tincidunt dui. Faucibus ' + 'in ornare quam viverra orci ' + 'sagittis eu volutpat odio. Enim ' + 'blandit volutpat maecenas ' + 'volutpat blandit aliquam etiam. ' + 'Vel quam elementum pulvinar ' + 'etiam. Duis ut diam quam nulla ' + 'porttitor massa id.', normalize=1, ).split(',')[-1]
        == '02000060626$068d$lidsacetumnpvgflo'
    )
    assert (
        fp.fingerprint('Sainte-Vincent')
        == 'sainte-vincent,,0100000014$110c$sv'
    )
    assert (
        fp.fingerprint('Lorem', 'Sainte-Vincent')
        == 'lorem,sainte-vincent,0100001405$068d110b$lsvlo'
    )
    assert (
        fp.fingerprint('Louis II', 'Jean')
        == 'louis ii,jean,0000490408$049b068d$lijlo'
    )
    assert (
        fp.fingerprint('Louis', 'Jean II', normalize=2)
        == 'louis ii,jean,0000490705$049a068d$ljilo'
    )
    assert (
        fp.fingerprint('Louis', 'Jean II ', normalize=2)
        == 'louis ii,jean,0000490805$049b068d$ljilo'
    )
    assert (
        fp.fingerprint('Louis', 'Jean II-', normalize=2)
        == 'louis,jean ii-,0100490805$049b068d$ljilo'
    )
    assert (
        fp.fingerprint('Louis V.', 'Jean', normalize=2)
        == 'louis v.,jean,0200000408$068d$lvjlo'
    )
    assert (
        fp.fingerprint('Louis V.', 'Ste.-Jean Ste.', normalize=2)
        == 'louis v.,ste.-jean ste.,0200001408$068d127b127X$lvsjlo ste'
    )
    assert (
        fp.fingerprint('Louis IX', 'Jean III II', normalize=2)
        == 'louis ix iii ii,jean,0000481108$048b049a056b068d$lijlo'
    )
    assert (
        fp.fingerprint('Louis IX', 'Jean II III', normalize=2)
        == 'louis ix iii ii,jean,0000481108$048a049a056b068d$lijlo'
    )
    assert (
        fp.fingerprint('Louis IX', 'Jean II III', normalize=1)
        == 'louis ix,jean ii iii,0000481108$048a049a056b068d$lijlo'
    )
    assert (
        fp.fingerprint('Lorem', 'Sainte-Sainte-Vincent')
        == 'lorem,sainte-sainte-vincent,0100002105$068d110b$lsvlo'
    )
    assert (
        fp.fingerprint('Brueghel II', 'I. Jan', normalize=2)
        == 'brueghel ii,i. jan,0200000611$$bij'
    )
    assert (
        fp.fingerprint('Brueghel', 'I. Jan II', normalize=2)
        == 'brueghel,i. jan ii,0200000908$$bij'
    )
    assert (
        fp.fingerprint('Lorem', 'Laurent Ormond')
        == 'lorem,laurent ormond,0000001405$068d$lo'
    )
