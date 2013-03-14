thunderdome-logging
===================

Library for logging errors and associating them with vertices in a graph via thunderdome

## Update thunderdome spec for logger

Add the following to your thunderdome spec file to allow the logger to work:

```js
{"type": "property", "name": "message", "data_type": "String"},
{"type": "property", "name": "created_at", "data_type": "Double"},
{"type": "property", "name": "created_at_rev", "data_type": "Double"},
{"type": "edge", "label": "errors", "primary_key": "created_at_rev"}
```

## Registering the log handler

To use the graph handler for logging add it as an additional log handler on logger you will be using:

```python
import logging
from thunderdome_logging import GraphHandler
# ...
graph_handler = GraphHandler()
graph_handler.setLevel(...)
# ...
logger.addHandler(graph_handler)
```

## Logging errors using the graph handler

Now that you have the graph handler attached to your logger you can place errors related to certain objects in the graph simply by passing the related vertex objects as additional arguments to logging command, for example:

```python
try:
  # Important stuff
except Exception as ex:
  logger.exception(ex, self.user, self.group) 
```

This will create an error vertex in the graph with the given exception and its stack trace and then attach that error message vertex to the user and group objects passed in.

## Querying the graph for errors

```python
from thunderdome_logging import get_errors

# Get the 5 most recent errors for the object with the given vid
errors = get_errors(vid)
```