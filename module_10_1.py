from time import sleep
from datetime import datetime
from threading import Thread

time_st1 = datetime.now()

def wite_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i} \n')
            sleep(0.1)
        print(f'Завершилась запись в файл {file.name}')


wite_words(10, "example1.txt")
wite_words(30, "example2.txt")
wite_words(200, "example3.txt")
wite_words(100, "example4.txt")

time_end1 = datetime.now()
time_result = time_end1 - time_st1
print(f'Работа потоков {time_result}')

time_st2 = datetime.now()

flux_1 = Thread(target=wite_words, args=(10, "example5.txt"))
flux_2 = Thread(target=wite_words, args=(30, "example6.txt"))
flux_3 = Thread(target=wite_words, args=(200, "example7.txt"))
flux_4 = Thread(target=wite_words, args=(100, "example8.txt"))

flux_1.start()
flux_2.start()
flux_3.start()
flux_4.start()

flux_1.join()
flux_2.join()
flux_3.join()
flux_4.join()

time_end2 = datetime.now()
time_result2 = time_end2 - time_st2
print(f'Работа потоков {time_result2}')
