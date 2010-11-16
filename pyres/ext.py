import pkgutil
import pyresext

def simple_extensions():
    extension_modules = [name for _, name, _ in pkgutil.iter_modules([pyresext.__name__])]
    def _load_before_job(mod):
        func = getattr(mod,'before_job', None)
        if func:
            return func
    def _load_after_job(mod):
        func = getattr(mod,'after_job', None)
        if func:
            return func

    def _load_before_fork(mod):
        func = getattr(mod,'before_fork', None)
        if func:
            return func

    def _load_after_fork(mod):
        func = getattr(mod,'after_fork', None)
        if func:
            return func
    

def _load_extensions(package_name='pyresext'):
    """Loads modules from the pyresext."""
    import pkgutil
    package = __import__(package_name,globals(), locals())
    _modules = []
    for importer, modname, ispkg in pkgutil.walk_packages(path=package.__path__, onerror=lambda x: None):
        _module = getattr(package, modname)
        _modules.append(_module)
    
    def _load_before_job(mod):
        func = getattr(mod,'before_job', None)
        if func:
            return func
    def _load_after_job(mod):
        func = getattr(mod,'after_job', None)
        if func:
            return func

    def _load_before_fork(mod):
        func = getattr(mod,'before_fork', None)
        if func:
            return func

    def _load_after_fork(mod):
        func = getattr(mod,'after_fork', None)
        if func:
            return func
    _before_jobs = map(_load_before_job, _modules)
    _after_jobs = map(_load_after_job, _modules)
    _before_forks = map(_load_before_fork, _modules)
    _after_forks = map(_load_after_fork, _modules)
    return _before_jobs, _after_jobs, _before_forks, _after_forks

_before_jobs, _after_jobs, _before_forks, _after_forks = _load_extensions()
