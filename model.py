import time
import os
import datetime
import random

test_combiner = [[0, 5000, 50000000], [1, 7500, None]]

epoch = 0
max_epoch = 1000000000
max_value = []
min_value = []


def pre_reg(result_arr):
    global max_value
    global min_value

    if (len(max_value) == 0) or (result_arr[0] > max_value[0]):
        max_value = result_arr

    if (len(min_value) == 0) or (result_arr[0] < min_value[0]):
        min_value = result_arr


class Simulation(object):
    def __init__(self, data_for_start, data_of_registry):

        # не обращайте внимания на столетия до потопа, программа их не учитывает

        self.matrix_dl_bible = {
            '1': [1, 3, 4, 3], '2': [1, 3, 4, 3], '3': [1, 3, 4, 3],
            '4': [1, 3, 4, 3], '5': [1, 3, 4, 3], '6': [1, 3, 4, 3],
            '7': [1, 3, 4, 3], '8': [1, 3, 4, 3], '9': [1, 3, 4, 4],
            '10': [1, 3, 4, 3], '11': [1, 3, 4, 3], '12': [1, 3, 4, 3],
            '13': [1, 3, 4, 3], '14': [1, 3, 4, 3], '15': [1, 3, 4, 3],
            '16': [1, 3, 4, 3], '17': [1, 3, 4, 4], '18': [1, 3, 4, 4],
            '19': [1, 3, 4, 6], '20': [1, 2, 4, 8], '21': [1, 1, 4, 5],
            '22': [1, 3, 4, 6], '23': [1, 4, 4, 6], '24': [1, 4, 4, 4],
            '25': [1, 4, 4, 4], '26': [1, 4, 4, 4], '27': [1, 4, 4, 4],
            '28': [1, 4, 4, 4], '29': [1, 4, 4, 4], '30': [1, 4, 4, 4],
            '31': [1, 4, 4, 4], '32': [1, 4, 4, 4], '33': [1, 4, 4, 4],
            '34': [2, 4, 6, 4], '35': [0, 4, 4, 4], '36': [0, 4, 4, 4],
            '37': [0, 4, 4, 4], '38': [0, 4, 4, 4], '39': [0, 4, 4, 4],
            '40': [0, 4, 4, 4], '41': [0, 4, 4, 4], '42': [0, 4, 4, 4],
            '43': [0, 4, 4, 4], '44': [0, 4, 4, 4], '45': [0, 4, 4, 4],
            '46': [0, 4, 4, 4], '47': [0, 4, 4, 4], '48': [0, 4, 4, 4],
            '49': [0, 4, 4, 4], '50': [0, 4, 4, 4], '51': [0, 4, 4, 4],
            '52': [0, 4, 4, 4], '53': [0, 4, 4, 4], '54': [0, 4, 4, 4]
        }

        self.matrix_dl = {
            '1': [3, 3, 6, 3], '2': [3, 3, 4, 3], '3': [3, 3, 4, 3],
            '4': [3, 3, 4, 3], '5': [3, 3, 4, 3], '6': [3, 3, 4, 3],
            '7': [3, 3, 4, 3], '8': [3, 3, 4, 3], '9': [4, 3, 4, 4],
            '10': [4, 3, 4, 3], '11': [4, 3, 4, 3], '12': [4, 3, 4, 3],
            '13': [4, 3, 4, 3], '14': [4, 3, 4, 3], '15': [4, 3, 4, 3],
            '16': [4, 3, 4, 3], '17': [4, 3, 4, 4], '18': [4, 3, 4, 4],
            '19': [4, 3, 4, 6], '20': [4, 2, 4, 8], '21': [4, 1, 4, 5],
            '22': [4, 3, 4, 4], '23': [4, 4, 4, 4], '24': [4, 4, 4, 4],
            '25': [4, 4, 4, 4], '26': [4, 4, 4, 4], '27': [4, 4, 4, 4],
            '28': [4, 4, 4, 4], '29': [4, 4, 4, 4], '30': [4, 4, 4, 4],
            '31': [4, 4, 4, 4], '32': [4, 4, 4, 4], '33': [4, 4, 4, 4],
            '34': [4, 4, 4, 4], '35': [4, 4, 4, 4], '36': [4, 4, 4, 4],
            '37': [4, 4, 4, 4], '38': [4, 4, 4, 4], '39': [4, 4, 4, 4],
            '40': [4, 4, 4, 4], '41': [4, 4, 4, 4], '42': [4, 4, 4, 4],
            '43': [4, 4, 4, 4], '44': [4, 4, 4, 4], '45': [4, 4, 4, 4],
            '46': [4, 4, 4, 4], '47': [4, 4, 4, 4], '48': [4, 4, 4, 4],
            '49': [4, 4, 4, 4], '50': [4, 4, 4, 4], '51': [4, 4, 4, 4],
            '52': [4, 4, 4, 4], '53': [4, 4, 4, 4], '54': [4, 4, 4, 4]
        }

        self.max_value = []
        self.min_value = []

        self.stat = {
            'test_code': data_for_start[0],
            'years': data_for_start[1],
        }
        self.__db_matrix = []
        self.__stat_result = {}
        self.levels = self.__gen_arr_items()
        self.centuries = self.__s_time(self.stat['years'])
        self.data_of_registry = data_of_registry

        if self.stat['test_code'] == 0:
            self.stat['count_of_start'] = data_for_start[2]
            self.stat['flood'] = 0
        elif self.stat['test_code'] == 1:
            self.stat['count_of_start'] = 13
            self.stat['flood'] = 1
        self.__ex_history()

    # получаем рандомные проценты для уровней смертности и рождаемости
    def __gen_arr_items(self):

        return [[i for i in range(1, 3)], # 0
                [i for i in range(1, 7)], # 1
                [i for i in range(8, 21)], # 2
                [i for i in range(22, 34)], # 3
                [i for i in range(43, 45)], # 4
                [i for i in range(100, 105)], # 5
                [i for i in range(120, 125)], # 6
                [i for i in range(190, 205)], # 7
                [i for i in range(280, 285)], # 8
        ]

    def __s_time(self, years):
        data_result = []
        for century in range(1, (years // 100) + 1):
            if century > 21:
                data_result.append((century * (-1)) + 21)
            else:
                data_result.append(century)
        data_result.sort()
        return data_result

    # получаем индекс из матрицы оганичений.
    # 0 элемент — это уровень смертности в век до нашей эры
    # 1 элемент — это уровень смерности в нашей эры
    # 2 элемент — это уровень рождаемости до нашей эры
    # 3 элемент — это уровень рождаемости в нашей эре
    def __mdl_index(self, num_oc, dl_param):
        if num_oc < 0 and dl_param == 'd':
            return 0
        elif num_oc > 0 and dl_param == 'd':
            return 1
        elif num_oc < 0 and dl_param == 'b':
            return 2
        elif num_oc > 0 and dl_param == 'b':
            return 3
        else:
            pass

    def __pdl(self, level_od):
        return self.levels[level_od]

    def __gen_stat(self, century):
        def gen_bd(type_of_matrix):
            global b
            global d

            if type_of_matrix == 0:
                b = random.choice(
                    self.levels[self.matrix_dl[str(int((century ** 2) ** 0.5))][self.__mdl_index(century, 'b')]])
                d = random.choice(
                    self.levels[self.matrix_dl[str(int((century ** 2) ** 0.5))][self.__mdl_index(century, 'd')]])
            elif type_of_matrix == 1:
                b = random.choice(
                    self.levels[self.matrix_dl_bible[str(int((century ** 2) ** 0.5))][self.__mdl_index(century, 'b')]])
                d = random.choice(
                    self.levels[self.matrix_dl_bible[str(int((century ** 2) ** 0.5))][self.__mdl_index(century, 'd')]])

        if self.stat['test_code'] == 0:
            gen_bd(self.stat['test_code'])
        elif self.stat['test_code'] == 1:
            gen_bd(self.stat['test_code'])
        if century > 0:
            # должен быть прирост, то есть b (born) > d (death)
            while b == d or d > b:
                if self.stat['test_code'] == 0:
                    gen_bd(self.stat['test_code'])
                elif self.stat['test_code'] == 1:
                    gen_bd(self.stat['test_code'])
        else:
            # если популяция сильно мала (8 человек), она может пропасть вовсе.
            # поэтому должен быть прирост
            while b == d:
                if self.stat['test_code'] == 0:
                    gen_bd(self.stat['test_code'])
                elif self.stat['test_code'] == 1:
                    gen_bd(self.stat['test_code'])
        self.__db_matrix.append([b, d])

    def __ex_history(self):
        for cent in self.centuries:
            if cent == -34 and self.stat['flood'] == 1:
                # после потопа осталось 8 человек
                self.__stat_result['-35'][0] = 8
            self.__gen_stat(cent)

            if len(self.__stat_result.keys()) < 1:
                data_for_ep = self.stat['count_of_start']
            else:
                if cent == 1:
                    data_for_ep = self.__stat_result[str(cent - 2)][0]
                else:
                    keys_of_stat_result = [i for i in self.__stat_result.keys()]
                    if str(cent - 1) == '0':
                        continue
                    else:
                        data_for_ep = self.__stat_result[str(cent - 1)][0]
                pass

            if self.data_of_registry[0] == 1:
                self.s_reg.r_registry(sum([b, d]))

            if self.data_of_registry[0] == 1 and self.data_of_registry[1] == 1:
                pass
            else:
                borned = int((data_for_ep * (b / 100)))
                death = int((data_for_ep * (d / 100)))
                pre_result = data_for_ep - death + borned
            self.__stat_result[str(cent)] = [pre_result, '{0}%'.format(b), '{0}%'.format(d), borned]
        pre_reg([pre_result, self.__db_matrix])


if __name__ == '__main__':
    for test_c in test_combiner:
        start_time = time.time()
        while epoch < max_epoch:
            epoch += 1
            test = Simulation(test_c, [0, 0])

        print(str(max_value[0]) + ', ' + str(min_value[0]) + ' - ' + str(time.time() - start_time))
        epoch = 0
        max_value.clear()
        min_value.clear()
