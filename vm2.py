import os

# задаем параметры передачи данных
bandwidth = input("Введите пропускную способность (число в мбит/c): ") + "mbit"
loss = input("Введите процент потери пакетов: ") + "%"
delay = input("Введите задержку в мс: ") + "ms"

# получаем IP-адреса второй виртуальной машины
ip_address = input("Введите IP-адрес второй виртуальной машины: ")

# настраиваем эмуляцию параметров передачи
os.system("sudo tc qdisc add dev enp0s3 root netem delay {} loss {} rate {}".format(delay, loss, bandwidth))

# измеряем параметры потери пакетов и задержки
os.system("ping {} -s 1000 -c 10".format(ip_address))

# измеряем параметры пропускной способности
os.system("iperf -c {}".format(ip_address))