class MinHeap:
    def __init__(self, capacity: int = 100):
        self.heap_array = [None] * capacity  # fixed capacity
        self.element_counter = 0

    # ---- index relations ----
    def left_child(self, parent: int) -> int:
        return 2 * parent + 1

    def right_child(self, parent: int) -> int:
        return 2 * (parent + 1)

    def parent(self, child: int) -> int:
        return (child - 1) // 2

    def swap(self, i: int, j: int) -> None:
        """In-place swap of two array elements."""
        if i != j:
            temp = self.heap_array[i]
            self.heap_array[i] = self.heap_array[j]
            self.heap_array[j] = temp

    # ---- heap core operations ----
    def add(self, value: str) -> None:
        """Add a new element and restore min-heap property (bubble up)."""
        if self.element_counter >= len(self.heap_array):
            raise IndexError("Heap capacity exceeded")

        # Place new element at next free spot
        self.heap_array[self.element_counter] = value
        self.element_counter += 1

        # Restore heap property (bubble up)
        self._bubble_up(self.element_counter - 1)

    def remove(self) -> str | None:
        """Remove and return the smallest element (root)."""
        if self.element_counter == 0:
            return None

        removed = self.heap_array[0]
        # Move last element to the root
        self.heap_array[0] = self.heap_array[self.element_counter - 1]
        self.heap_array[self.element_counter - 1] = None
        self.element_counter -= 1

        # Restore heap property (bubble down)
        if self.element_counter > 0:
            self._bubble_down(0)

        return removed

    def peek(self) -> str | None:
        """Return (without removing) the smallest element."""
        if self.element_counter == 0:
            return None
        return self.heap_array[0]

    def size(self) -> int:
        """Return number of elements currently stored."""
        return self.element_counter

    # ---- helpers to restore heap ----
    def _bubble_up(self, index: int) -> None:
        """Restore heap upward after insertion."""
        while index > 0:
            p = self.parent(index)
            if self.heap_array[index] < self.heap_array[p]:
                self.swap(index, p)
                index = p
            else:
                break

    def _bubble_down(self, index: int) -> None:
        """Restore heap downward after removal."""
        while True:
            left = self.left_child(index)
            right = self.right_child(index)
            smallest = index

            if left < self.element_counter and self.heap_array[left] < self.heap_array[smallest]:
                smallest = left
            if right < self.element_counter and self.heap_array[right] < self.heap_array[smallest]:
                smallest = right

            if smallest != index:
                self.swap(index, smallest)
                index = smallest
            else:
                break


# ---- Example usage ----
if __name__ == "__main__":
    h = MinHeap(10)
    h.add("pear")
    h.add("apple")
    h.add("banana")
    h.add("cherry")

    print("Heap size:", h.size())        # 4
    print("Peek smallest:", h.peek())    # apple

    print("Removed:", h.remove())        # apple
    print("Peek now:", h.peek())         # banana
    print("Heap size:", h.size())        # 3
