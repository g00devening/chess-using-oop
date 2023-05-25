class BigBell:
    bell_count = 0

    def sound(self):
        if self.bell_count % 2 == 0:
            print('Ding!')
            self.bell_count += 1
        else:
            print('Dong!')
            self.bell_count += 1


bell = BigBell()
bell.sound()
bell.sound()
bell.sound()
bell.sound()
bell.sound()