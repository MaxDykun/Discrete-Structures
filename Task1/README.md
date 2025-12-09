# Deque (Double-Ended Queue) — Full Interactive Implementation

**Educational project** | Data Structures & Algorithms

### Features
- All classic deque operations:
  - `push_front()` / `push_back()`
  - `pop_front()` / `pop_back()`
  - `peek_front()` / `peek_back()`
- Additional useful methods:
  - `swap_first_last()` — swap first and last elements
  - `reverse()` — reverse the entire deque
  - `contains(value)` — check if element exists
  - `clear()` — remove all elements
  - `size()` and `is_empty()`
- Fully interactive English menu
- Beautiful real-time visualization of current deque state (front/back arrows)
- Clean, readable and well-commented code

 Implementation Details
- Based on Python's built-in `list`
- `push_front()` and `pop_front()` use `insert(0, ...)` and `pop(0)` → O(n)
- All other operations are O(1)
- No external dependencies
