import time
class BatteryInfo:
    battery_percentage: int = -1
    battery_present: bool = False
    battery_voltage: float = 0
    battery_mos_state: int = 0
    battery_current: float = 0
    battery_location: str = "unknown"
    battery_header_frame_id: str = "unknown"
    battery_stamp: time = time.time()


if __name__ == '__main__':
    batteryList=[]
    
    battery_tmp= BatteryInfo()
    battery_tmp.battery_percentage = 20
    battery_tmp.battery_present=True
    batteryList.append(battery_tmp)

    battery_tmp2= BatteryInfo()
    battery_tmp2.battery_percentage = 30
    battery_tmp2.battery_present=False
    batteryList.append(battery_tmp2)

    for tmp in batteryList:
        print(tmp.battery_percentage)
        print(tmp.battery_present)
    
    id = 2
    print(batteryList[id-1].battery_percentage)