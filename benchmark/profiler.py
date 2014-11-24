import cProfile, pstats, StringIO

def print_stats(func, *args, **kwargs):
    pr = cProfile.Profile()
    pr.enable()
    res = func(*args, **kwargs)
    pr.disable()
    s = StringIO.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())
    return r
