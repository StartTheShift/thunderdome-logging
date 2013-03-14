# Copyright (c) 2012-2013 SHIFT.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from datetime import datetime
import logging

import thunderdome


class ErrorVertex(thunderdome.Vertex):
    """Graph vertex for storing an error message sent to the logs."""
    error_message    = thunderdome.String(required=True)
    created_at = thunderdome.DateTime(default=datetime.now, required=True)
        
    
class Errors(thunderdome.Edge):
    """Edge associating a graph vertex with an ErrorVertex"""

    # The created at timestamp
    created_at = thunderdome.DateTime(required=True)
    # The reverse of the created at timestamp used for vertex centric queries
    created_at_rev = thunderdome.Float(required=False)
    
    def pre_save(self):
        self.created_at = datetime.now()
        self.created_at_rev = -self._columns['created_at'].to_database(self.created_at)
        super(Errors, self).pre_save()


class GraphHandler(logging.Handler):
    """
    Custom log handler which emits errors to a graph and associates the error
    message with any descendants of BaseVertex passed in as arguments. If no
    descendants of thunderdome.Vertex are passed in then this handler has no
    effect.
    """
    
    def emit(self, record):
        """
        Emits the given error message to the graph and associates the error with
        any objects passed as arguments to the logger.

        :param record: The record to be logged
        :type record: logging.LogRecord
        
        """
        vertex_args = [x for x in record.args \
                       if issubclass(x.__class__, thunderdome.Vertex)]

        if vertex_args:
            # Create error vertex in graph
            ev = ErrorVertex.create(error_message=str(record.msg))
            for va in vertex_args:
                # Associate the error vertex with all vertices in arguments
                Errors.create(va, ev)
        
