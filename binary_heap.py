# Em um heap binário representado como um array:

# O nó na posição i tem:
#   - O pai na posição: (i-1) // 2
#   - O filho esquerdo na posição: 2i + 1
#   - O filho direito na posição: 2i + 2

# Ultimo nó com filhos: len(self.heap) // 2 - 1 

class BinaryHeap:
    def __init__(self, array=None):
        self.heap = array if array else []

    def _swap(self, index, parent):
        """Troca as posições"""
        self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]

    def _is_bigger(self, i, j):
        """Confere se um valor é maior do que outro dentro do heap"""
        return True if self.heap[i] > self.heap[j] else False

    def display_heap(self):
        """Exibe o estado atual do heap."""
        print("Heap:", self.heap)

    def insert(self, new_value):
        """Insere um valor no heap e reorganiza a estrutura."""
        self.heap.append(new_value)
        self._heapify_up(len(self.heap) - 1)
        self.display_heap()

    def _heapify_up(self, index):
        """Reorganiza o heap subindo o valor inserido para a posição correta."""
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[parent_index] < self.heap[index]:
                self._swap(parent_index, index)
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
        self._heapify_down(0)
        self.display_heap()
        return removed

    def _heapify_down(self, index):
        """Reorganiza o heap descendo o valor para a posição correta."""
        n = len(self.heap)
        while True:
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            largest = index  # índice do maior valor entre o nó atual e seus filhos.

            if left_child < n and self._is_bigger(left_child, largest):
                largest = left_child
            if right_child < n and self._is_bigger(right_child, largest):
                largest = right_child
            if largest != index:
                self._swap(index, largest)
                index = largest
            else:
                # se o maior for o pai
                break

    def heapsort(self):
        """Realiza a ordenação do heap e exibe o estado após cada remoção."""
        # construindo o max-heap
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)
        
        # removendo e ordenando
        sorted_list = []
        while len(self.heap) > 0:
            sorted_list.append(self.remove())

        self.heap = sorted_list
        print("Heap ordenado: ", self.heap)

    def get_high_priority(self):
        """Retorna o elemento de alta prioridade (raiz do heap)."""
        if len(self.heap) > 0:
            print("Elemento de alta prioridade:", self.heap[0])
        else:
            print("Heap vazio.")

    def change_priority(self, index, new_priority):
        self.heap[index] = new_priority
        parent = (index - 1) // 2

        if index > 0 and self.heap[index] > self.heap[parent]:
            self._heapify_up(index)
        else:
            self._heapify_down(index)
        self.display_heap()

    def display_heap_graph(self):
        print("NADA POR ENQUANTO")
