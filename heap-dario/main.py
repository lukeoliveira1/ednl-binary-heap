from ternary_heap import TernaryHeap

def test():
    data = [13, 26, 19, 17, 24, 31, 22]

    heap = TernaryHeap()

    print("--------Construção do Heap:--------")

    # 1. Construção do Heap
    for value in data:
        print(f"Inserindo: {value}")
        heap.insert(value)

    ("\n--------Remoções:--------")
    # 3. Remoções - Remover três vezes consecutivas
    # print("Removendo o elemento de alta prioridade:")
    # heap.remove()
    # heap.remove()
    # heap.remove()
    
    heap.display_heap_graph()

if __name__ == "__main__":
    test()