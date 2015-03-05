import contextlib
import yaml

@contextlib.contextmanager
def yaml_load(yml_stream):
    try:
        f = yaml.safe_load(yml_stream)
        yield f
    except AttributeError, e:
        print "Error %s" %(e)
    finally:
        del f