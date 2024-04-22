class star_printing:
    def right_angle_tringle(self, n):
        for i in range(n):
            for j in range(n+1):
                print("*",end=" ")


if __name__ == '__main__':
    obj = star_printing()
    obj.right_angle_tringle(4)
