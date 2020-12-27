from typing import List, Tuple, Set
import numpy as np


class Game:
    def __init__(self, matrix: Set[Tuple[int, int]]) -> object:
        self.matrix = np.array(matrix)
        dx, dy, dz = self.matrix.shape
        if dx != dy and dz != 2:
            raise BaseException("Мтрица не квадратная, как моя голова")

    def play(self) -> List[Tuple[int, int]]:
        """Вохвращает номера адреса ячеек принадлежащих равновесию Неша"""
        # Повышвем скорость
        matrix = self.matrix
        res_one: List[int] = list()
        res_two: List[int] = list()
        res: Set[Tuple[int, int]] = set()
        for item in matrix[:, :, 1]:
            # print(item.max())
            res_one.append(item.argmax())
        # print("_"*10)
        for item in matrix[:, :, 0].T:
            # print(item.max())
            res_two.append(item.argmax())
        # print(res_one)
        # print(res_two)
        it = res_two.__iter__()
        for i in res_one:
            res.add((i, next(it)))
        return res
