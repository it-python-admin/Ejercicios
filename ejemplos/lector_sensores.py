import time
def lector_sensor_temperatura():
    print("Sensor temperatura")
    return 25
def lector_sensor_humedad():
    print("Sensor humedad")
    return 70
def lector_sensor_volumetrico():
    print("Sensor volumetrico")
    return True

sensores = [lector_sensor_temperatura, lector_sensor_humedad, lector_sensor_volumetrico]

while True:
    for sensor in sensores:
        sensor()
    time.sleep(1)