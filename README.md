# Day 25 - Cycle Detection

## Maze Cycle Detection System

A game developer created a maze where some paths may accidentally form
infinite loops.

This project represents maze paths using a linked list and detects cycles
using Floyd's Fast and Slow Pointer Algorithm.

---

## Problem

A cycle occurs when a node eventually points back to an earlier node.

Example:

    Start -> A -> B -> C
                 ^       |
                 |_______|

If a player enters this path, they may never reach the exit.

---

## Floyd's Cycle Detection Algorithm

The algorithm uses two pointers:

### Slow Pointer

Moves one node at a time.

    slow = slow.next

### Fast Pointer

Moves two nodes at a time.

    fast = fast.next.next

If the two pointers meet:

    slow == fast

then a cycle exists.

---

## Example

Consider:

    Start -> A -> B -> C -> D
                 ^           |
                 |___________|

The slow and fast pointers eventually meet inside the cycle.

Therefore:

    Cycle Detected

---

## No Cycle

For a normal linked list:

    Start -> A -> B -> Exit -> None

The fast pointer eventually reaches None.

Therefore:

    No Cycle

---

## Test Cases

The program tests:

1. Normal path with no cycle.
2. Cycle connected to the first node.
3. Cycle connected to a middle node.
4. Single-node cycle.

---

## Safe Visualization

A cyclic linked list cannot be printed normally because the traversal
would continue forever.

Therefore, the display function limits the number of nodes shown.

This prevents the visualization itself from becoming an infinite loop.

---

## Complexity

Time Complexity:

    O(n)

Space Complexity:

    O(1)

Floyd's algorithm only requires two pointers.

---

## Real-World Applications

Cycle detection is useful in:

- Operating systems
- Dependency graphs
- Distributed systems
- Linked-list processing
- Game path systems
- Workflow systems
- Network routing

---

## How to Run

Open the VS Code terminal:

    python day25_cycle_detection.py

---

## Learning Outcomes

- Built linked-list maze paths.
- Created cyclic linked lists.
- Learned Floyd's cycle detection algorithm.
- Used fast and slow pointers.
- Tested multiple cycle configurations.
- Prevented infinite traversal during visualization.
- Understood O(n) time and O(1) space cycle detection.
