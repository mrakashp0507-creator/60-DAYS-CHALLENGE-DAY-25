# Day 25 - Cycle Detection
# Detect cycles using Fast and Slow Pointers


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class MazePath:
    def __init__(self):
        self.head = None
        self.nodes = []

    def add_path(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            self.nodes[-1].next = new_node

        self.nodes.append(new_node)

    def create_cycle(self, position):
        """
        Connect the last node to the node at the given position.

        position = 0 means cycle connects to the first node.
        position = -1 means no cycle.
        """

        if position < 0:
            return

        if position >= len(self.nodes):
            print("Invalid cycle position.")
            return

        self.nodes[-1].next = self.nodes[position]

    def display(self, limit=15):
        """
        Display the maze path safely.
        A limit prevents infinite printing when a cycle exists.
        """

        current = self.head
        count = 0

        while current is not None and count < limit:
            print(current.value, end=" -> ")
            current = current.next
            count += 1

        if current is not None:
            print("... cycle continues")
        else:
            print("None")


def detect_cycle(head):
    """
    Floyd's Cycle Detection Algorithm.

    Slow pointer moves one node at a time.
    Fast pointer moves two nodes at a time.
    """

    slow = head
    fast = head

    while fast is not None and fast.next is not None:

        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


def test_maze(name, values, cycle_position):
    print("\n======================================")
    print(name)
    print("======================================")

    maze = MazePath()

    for value in values:
        maze.add_path(value)

    maze.create_cycle(cycle_position)

    print("\nMaze Path:")
    maze.display()

    if detect_cycle(maze.head):
        print("\nResult: CYCLE DETECTED!")
        print("Players may be trapped in an infinite loop.")
    else:
        print("\nResult: NO CYCLE")
        print("Players can reach the end safely.")


# ============================================================
# TEST CASE 1 - No Cycle
# ============================================================

test_maze(
    "Maze 1 - Safe Path",
    ["Start", "Room-A", "Room-B", "Exit"],
    -1
)


# ============================================================
# TEST CASE 2 - Cycle to Start
# ============================================================

test_maze(
    "Maze 2 - Loop to Start",
    ["Start", "Room-A", "Room-B", "Room-C"],
    0
)


# ============================================================
# TEST CASE 3 - Cycle in Middle
# ============================================================

test_maze(
    "Maze 3 - Hidden Loop",
    ["Start", "Room-A", "Room-B", "Room-C", "Room-D"],
    2
)


# ============================================================
# TEST CASE 4 - Single Node Cycle
# ============================================================

test_maze(
    "Maze 4 - Single Room Loop",
    ["Start"],
    0
)