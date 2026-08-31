

import sys

# Fast I/O technique
_input_data = sys.stdin.read().split()
_NUM = int(_input_data[0])
_QUERY_COUNT = int(_input_data[1])

_MAX_RANGE = 1442
_time_array = [0] * _MAX_RANGE

# Process stores
_current_pos = 2
for _ in range(_NUM):
    _start = int(_input_data[_current_pos])
    _end = int(_input_data[_current_pos + 1])
    _time_array[_start] += 1
    if _end + 1 < _MAX_RANGE:
        _time_array[_end + 1] -= 1
    _current_pos += 2

# Prefix Sum Sweep
for i in range(1, _MAX_RANGE):
    _time_array[i] += _time_array[i-1]

# Fast Join Output
_QUERIES = _input_data[_current_pos:]
print(*( _time_array[int(t)] for t in _QUERIES ))