# -*-coding:utf-8-*-
#
#    Simple stemmer for Croatian v0.1
#    Copyright 2012 Nikola Ljubešić and Ivan Pandžić
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import re
import sys

pravila = [re.compile(r'^(' + osnova + ')(' + nastavak + r')$') for osnova, nastavak in
           [e.strip().split(' ') for e in open('rules.txt')]]
transformacije = [e.strip().split('\t') for e in open('transformations.txt')]
#stop = [e.strip().split('\t') for e in open('stop.txt')]


def istakniSlogotvornoR(niz):
    return re.sub(r'(^|[^aeiou])r($|[^aeiou])', r'\1R\2', niz)


def imaSamoglasnik(niz):
    if re.search(r'[aeiouR]', istakniSlogotvornoR(niz)) is None:
        return False
    else:
        return True


def transformiraj(pojavnica):
    for trazi, zamijeni in transformacije:
        if pojavnica.endswith(trazi):
            return pojavnica[:-len(trazi)] + zamijeni
    return pojavnica


def korjenuj(pojavnica):
    for pravilo in pravila:
        dioba = pravilo.match(pojavnica)
        if dioba is not None:
            if imaSamoglasnik(dioba.group(1)) and len(dioba.group(1)) > 1:
                return dioba.group(1)
    return pojavnica


def stem(input):
    stop = [e.strip() for e in open('stop.txt')]
    if input.lower() not in stop:
        return korjenuj(transformiraj(input.lower()))
    else:
        return ""
