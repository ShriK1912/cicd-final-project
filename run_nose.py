import collections
import collections.abc

from nose import main


if not hasattr(collections, "Callable"):
    collections.Callable = collections.abc.Callable

main(argv=["nosetests", "-v"])
