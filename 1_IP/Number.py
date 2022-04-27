import random

class threeNumber(object):
    number_list = []
    def ran(self):
        self.number_list = []
        random_number = random.randint(0,9)


        for i in range(3):
            while random_number in self.number_list:
                random_number = random.randint(0,9)
            self.number_list.append(random_number)

        print(self.number_list)

    def cal(self,first,second,third):
        ball_count=[0,0]
        if first==self.number_list[0]:
            ball_count[0]+=1
        else:
            if first == self.number_list[1]:
                ball_count[1] += 1
            elif first == self.number_list[2]:
                ball_count[1] += 1
        if second == self.number_list[1]:
            ball_count[0] += 1
        else:
            if second == self.number_list[0]:
                ball_count[1] += 1
            elif second == self.number_list[2]:
                ball_count[1] += 1
        if third == self.number_list[2]:
            ball_count[0] += 1
        else:
            if third == self.number_list[0]:
                ball_count[1] += 1
            elif third == self.number_list[1]:
                ball_count[1] += 1
        return ball_count





class fourNumber(object):
    number_list = []
    def ran(self):
        self.number_list = []
        random_number = random.randint(0, 9)

        for i in range(4):
            while random_number in self.number_list:
                random_number = random.randint(0, 9)
            self.number_list.append(random_number)

        print(self.number_list)

    def cal(self,first,second,third,fourth):
        ball_count=[0,0]
        if first==self.number_list[0]:
            ball_count[0]+=1
        else:
            if first == self.number_list[1]:
                ball_count[1] += 1
            elif first == self.number_list[2]:
                ball_count[1] += 1
            elif first == self.number_list[3]:
                ball_count[1] += 1
        if second == self.number_list[1]:
            ball_count[0] += 1
        else:
            if second == self.number_list[0]:
                ball_count[1] += 1
            elif second == self.number_list[2]:
                ball_count[1] += 1
            elif second == self.number_list[3]:
                ball_count[1] += 1
        if third == self.number_list[2]:
            ball_count[0] += 1
        else:
            if third == self.number_list[0]:
                ball_count[1] += 1
            elif third == self.number_list[1]:
                ball_count[1] += 1
            elif third == self.number_list[3]:
                ball_count[1] += 1
        if fourth == self.number_list[3]:
            ball_count[0] += 1
        else:
            if fourth == self.number_list[0]:
                ball_count[1] += 1
            elif fourth == self.number_list[1]:
                ball_count[1] += 1
            elif fourth == self.number_list[2]:
                ball_count[1] += 1
        return ball_count