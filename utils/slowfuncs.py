#    Copyright (C) 2009 Jeremy S. Sanders
#    Email: Jeremy Sanders <jeremy@jeremysanders.net>
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
##############################################################################

# $Id$

"""
These are slow versions of routines also implemented in C++
"""

from itertools import izip
import veusz.qtall as qt4

def addNumpyToPolygonF(poly, *args):
    """Add a set of numpy arrays to a QPolygonF."""

    for row in xrange(len(args[0])):
        for col in xrange(0, len(args), 2):
            x = args[col][row]
            y = args[col+1][row]
            poly.append( qt4.QPointF(x, y) )

def plotPathsToPainter(painter, path, x, y):
    """Plot array of x, y points."""

    for xp, yp in izip(x, y):
        painter.translate(xp, yp)
        painter.drawPath(path)
        painter.translate(-xp, -yp)

def plotLinesToPainter(painter, x1, y1, x2, y2):
    """Plot lines given in numpy arrays to painter."""
    lines = []
    for p in izip(x1, y1, x2, y2):
        lines.append( qt4.QLineF(*p) )
    painter.drawLines(lines)