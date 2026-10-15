# System design

Product document store. MongoDB holds the documents. Tests use the same rules in memory.

The system is one deployable unit. A request enters through the edge shown in the diagram, passes the rules for this product, and is stored as described in the database note. There is no shared login with the other portfolio repositories.

Stack: Python, MongoDB, Docker.
