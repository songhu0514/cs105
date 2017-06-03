from schedule import Schedule

def test_add():
    s = Schedule('s1', 'work schedule')
    s.add_task('write', 'write gibberish design doc', '1')
    assert 'write' in s.tasks

def test_remove():
    s = Schedule('s1', 'work schedule')
    s.add_task('study', 'study python', '1000')
    s.remove_task('study')
    assert s.tasks == {}
