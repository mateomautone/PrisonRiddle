import prison_python

def main():
    print("Running 1 Iteration with random number choosing")
    print("Success" if prison_python.main_routine(algorithm='random',verbose=True) else "Fail")
    print("Running 1 Iteration with loop following algorithm")
    print("Success" if prison_python.main_routine(algorithm='tryloop',verbose=True) else "Fail")
    # saliobien = 0
    # saliomal = 0
    # for intento in range(100000):
    #     if prison_python.main_routine(algorithm='tryloop',verbose=False):
    #         saliobien += 1
    #     else:
    #         saliomal += 1
    print("Finished Runs")
    # print("Salieron Bien:", saliobien)
    # print("Salieron Mal:", saliomal)

if __name__ == '__main__':
    main()