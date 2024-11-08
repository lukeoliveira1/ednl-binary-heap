from binary_heap import BinaryHeap


def test_one():
    data = [10, 5, 20, 1, 15, 30, 25]

    heap = BinaryHeap()

    print("--------Construção do Heap:--------")

    # 1. Construção do Heap
    for value in data:
        print(f"Inserindo: {value}")
        heap.insert(value)

    print("\n---------Alteração de Prioridade--------")
    # 2. Alteração de Prioridade
    print("Alterando prioridade do índice 3 para 50")
    heap.change_priority(3, 50)
    print("Alterando prioridade do índice 1 para 8")
    heap.change_priority(1, 8)

    print("\n--------Remoções:--------")
    # 3. Remoções - Remover três vezes consecutivas
    print("Removendo 4x o elemento de alta prioridade:")
    heap.remove()
    heap.remove()
    heap.remove()
    heap.remove()

    # 4. Remover e ordenar todos os elementos
    print("\n--------Heapsort:--------")
    heap.heapsort()

    # 5. Exibir o elemento de maior prioridade
    print("\n--------Get High Priority:--------")
    heap.get_high_priority()

    heap.display_heap_graph()


def test_two():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    heap = BinaryHeap()

    print("--------Construção do Heap:--------")

    # 1. Construção do Heap
    for value in data:
        print(f"Inserindo: {value}")
        heap.insert(value)

    print("\n---------Alteração de Prioridade--------")
    # 2. Alteração de Prioridade
    print("Alterando prioridade do índice 4 para 15")
    heap.change_priority(4, 15)
    print("Alterando prioridade do índice 8 para 3")
    heap.change_priority(8, 3)

    print("\n--------Remoções:--------")
    # 3. Remoções - Remover três vezes consecutivas
    print("Removendo 5x o elemento de alta prioridade:")
    heap.remove()
    heap.remove()
    heap.remove()
    heap.remove()
    heap.remove()

    # 4. Remover e ordenar todos os elementos
    print("\n--------Heapsort:--------")
    heap.heapsort()

    # 5. Exibir o elemento de maior prioridade
    print("\n--------Get High Priority:--------")
    heap.get_high_priority()

    heap.display_heap_graph()


def test_three():
    data = [50, 40, 30, 20, 10, 5, 3]

    heap = BinaryHeap()

    print("--------Construção do Heap:--------")

    # 1. Construção do Heap
    for value in data:
        print(f"Inserindo: {value}")
        heap.insert(value)

    print("\n---------Alteração de Prioridade--------")
    # 2. Alteração de Prioridade
    print("Alterando prioridade do índice 2 para 60")
    heap.change_priority(2, 60)
    print("Alterando prioridade do índice 5 para 1")
    heap.change_priority(5, 1)

    print("\n--------Remoções:--------")
    # 3. Remoções - Remover três vezes consecutivas
    print("Removendo 3x o elemento de alta prioridade:")
    heap.remove()
    heap.remove()
    heap.remove()

    # 4. Remover e ordenar todos os elementos
    print("\n--------Heapsort:--------")
    heap.heapsort()

    # 5. Exibir o elemento de maior prioridade
    print("\n--------Get High Priority:--------")
    heap.get_high_priority()

    heap.display_heap_graph()


def test_four():
    data = [13, 26, 19, 17, 24, 31, 22, 11, 8, 20, 5, 27, 18]

    heap = BinaryHeap()

    print("--------Construção do Heap:--------")

    # 1. Construção do Heap
    for value in data:
        print(f"Inserindo: {value}")
        heap.insert(value)

    print("\n---------Alteração de Prioridade--------")
    # 2. Alteração de Prioridade
    print("Alterando prioridade do índice 7 para 35")
    heap.change_priority(7, 35)
    print("Alterando prioridade do índice 10 para 12")
    heap.change_priority(10, 12)  

    print("\n--------Remoções:--------")
    # 3. Remoções - Remover três vezes consecutivas
    print("Removendo o elemento de alta prioridade:")
    heap.remove()
    heap.remove()
    heap.remove()

    # 4. Remover e ordenar todos os elementos
    print("\n--------Heapsort:--------")
    heap.heapsort()

    # 5. Exibir o elemento de maior prioridade
    print("\n--------Get High Priority:--------")
    heap.get_high_priority()

    heap.display_heap_graph()
