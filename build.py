import time

def processor_intensive_calculation():
    while True:
        x = 0
        for i in range(1000000000):
            for j in range(1000000000):
                for k in range(1000000000):
                    for l in range(1000000000):
                        for m in range(1000000000):
                            for n in range(1000000000):
                                for o in range(1000000000):
                                    for p in range(1000000000):
                                    x += i * j * k * l * m * n * o * p
        print(x)

if __name__ == "__main__":
    processor_intensive_calculation()
