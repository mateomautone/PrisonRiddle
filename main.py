import prison_python

def main():
    #print("Running 1 Iteration with random number choosing")
    #print("Success" if prison_python.main_routine(algorithm='random',verbose=True) else "Fail")
    #print("Running 1 Iteration with loop following algorithm")
    print("Success" if prison_python.main_routine(algorithm='tryloop',verbose=True) else "Fail")
    print("Finished Runs")

if __name__ == '__main__':
    main()