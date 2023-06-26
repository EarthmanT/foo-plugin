import sys

from cloudify import ctx


def foo(*args, **kwargs):
    ctx.logger.info(sys.version)
    try:
        import pydoc
    except ImportError as e:
        ctx.logger.info('Cannot import pydoc: {}'.format(e))
    else:
        ctx.logger.info('Can import pydoc.')
