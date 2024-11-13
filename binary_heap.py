# Em um heap binário representado como um array:

# O nó na posição i tem:
#   - O pai na posição: (i-1) // 2
#   - O filho esquerdo na posição: 2i + 1
#   - O filho direito na posição: 2i + 2

# Ultimo nó com filhos: len(self.heap) // 2 - 1


class BinaryHeap:
    def __init__(self, array=None):
        self.heap = array if array else []

    def _swap(self, index, parent, heap):
        """Troca as posições"""
        heap[index], heap[parent] = heap[parent], heap[index]

    def _is_bigger(self, i, j, heap):
        """Confere se um valor é maior do que outro dentro do heap"""
        return True if heap[i] > heap[j] else False

    def display_heap(self):
        """Exibe o estado atual do heap."""
        print("Heap:", self.heap)

    def insert(self, new_value):
        """Insere um valor no heap e reorganiza a estrutura."""
        self.heap.append(new_value)
        # self._heapify_up(len(self.heap) - 1) # order
        self.display_heap()

    def _heapify_up(self, index):
        """Reorganiza o heap subindo o valor inserido para a posição correta."""
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[parent_index] < self.heap[index]:
                self._swap(parent_index, index, self.heap)
                index = parent_index
            else:
                break

    def remove(self):
        """Remove o elemento de alta prioridade e reorganiza o heap"""
        if len(self.heap) == 0:
            print("Heap vazio.")
            return None

        removed = self.heap[0]
        # Mover o último elemento para a raiz
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0, self.heap)
        self.display_heap()
        return removed

    def _heapify_down(self, index, heap):
        """Reorganiza o heap descendo o valor para a posição correta."""
        n = len(heap)
        while True:
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            largest = index  # índice do maior valor entre o nó atual e seus filhos.

            if left_child < n and self._is_bigger(left_child, largest, heap):
                largest = left_child
            if right_child < n and self._is_bigger(right_child, largest, heap):
                largest = right_child
            if largest != index:
                self._swap(index, largest, self.heap)
                index = largest
            else:
                # if the oldest is the father
                break

    def arrange(self, heap):
        """Reorganiza a lista para garantir a propriedade do heap."""
        for i in range(len(heap) // 2 - 1, -1, -1):
            self._heapify_down(i, heap)

    def heapsort(self):
        """Realiza a ordenação do heap e exibe o estado após cada remoção."""
        copy_heap = self.heap[:]  # [:] reference
        n = len(copy_heap)

        self.arrange(copy_heap)

        for i in range(n - 1, -1, -1):
            self._swap(0, i, copy_heap)

            self._heapify_down(0, copy_heap)

        print("Heap ordenado: ", copy_heap)

    def get_high_priority(self):
        """Retorna o elemento de alta prioridade (raiz do heap)."""
        if len(self.heap) > 0:
            print("Elemento de alta prioridade:", self.heap[0])
        else:
            print("Heap vazio.")

    def change_priority(self, index, new_priority):
        """Altera a prioridade de um elemento no heap e ajusta sua posição para manter a propriedade do heap."""
        self.heap[index] = new_priority

        self.arrange(self.heap)
        self.display_heap()
