from thermostat import ThermostatClient
from bosminer import Bosminer
from log import setup_logger
import time
import sys
import os

# --- PATH DEFINES ---
LOGGER_PATH = "/var/log/monitor/monitor.log"
BOSMINER_PATH = "/etc/init.d/bosminer"

# --- EXTRACT VARIABLES FROM ENV ---

# --- DEVICE CONFIGURATION ---
device_version = os.getenv('DEVICE_VERSION')
periodicity = os.getenv('PERIODICITY','5')
device_id = os.getenv('DEVICE_ID')
device_ip = os.getenv('DEVICE_IP')
local_key = os.getenv('LOCAL_KEY')

# --- DPS MAPPING ---
hysteresis_id = os.getenv('HYSTERESIS_ID','101')
temperature_id = os.getenv('TEMPERATURE_ID','3')
target_id = os.getenv('TARGET_ID','2')
state_id = os.getenv('STATE_ID','1')

# --- LOGGER INITIALISATION ---
LOGGER = setup_logger(LOGGER_PATH,"custom_monitor")

# --- ENTRY POINT ---
if __name__ == "__main__":
    # ============================================================
    # CHECK INPUTS
    # ============================================================
    if not device_id or len(device_id) != 22:
        LOGGER.error("DEVICE_ID is not defined or different to 22 bytes")
        sys.exit(1)
    
    if not device_ip:
        LOGGER.error("DEVICE_IP is not defined or bad address")
        sys.exit(1)
    
    if not local_key or len(local_key) != 16:
        LOGGER.error("LOCAL_KEY is not defined or different to 16 bytes")
        sys.exit(1)
        
    if not device_version:
        device_version = 3.5
    
    # ============================================================
    # constructors
    # ============================================================
    thermostat = ThermostatClient(device_id,device_ip,local_key,device_version)
    bosminer = Bosminer(BOSMINER_PATH)
    
    LOGGER.info("monitor is starting with :")
    LOGGER.info(f"--- DEVICE CONFIGURATIONS ---")
    LOGGER.info(f"DEVICE_ID       : '{device_id}'")
    LOGGER.info(f"DEVICE_IP       : '{device_ip}'")
    LOGGER.info(f"LOCAL_KEY       : '{local_key}'")
    LOGGER.info(f"DEVICE_VERSION  : '{device_version}'")
    LOGGER.info(f"--- TUYA DPS MAPPING ---")
    LOGGER.info(f"TEMPERATURE_ID  : '{temperature_id}'")
    LOGGER.info(f"HYSTERESIS_ID   : '{hysteresis_id}'")
    LOGGER.info(f"TARGET_ID       : '{target_id}'")
    LOGGER.info(f"STATE_ID        : '{state_id}'")
    LOGGER.info(f"--- SCRIPT CONFIGURATION ---")
    LOGGER.info(f"PERIODICITY     : '{periodicity}'")
    
    # ============================================================
    # MAIN LOOP
    # ============================================================
    while True:
        try:
            if thermostat.update() == True:
                # Thermostat is ON State
                if thermostat.get(state_id):
                    # Read parameters
                    hysteresis_temperature = thermostat.get(hysteresis_id)/10
                    target_temperature = thermostat.get(target_id)/10
                    # Compute thresholds high and low
                    high_threshold = target_temperature + hysteresis_temperature
                    low_threshold = target_temperature - hysteresis_temperature
                    # Read current temperature
                    current_temperature = thermostat.get(temperature_id)/10 
                    # Temperature is less than target (with hysteresis)
                    if current_temperature < low_threshold and not bosminer.get_state():
                        LOGGER.info(
                            f"Restart mining (Temp:'{current_temperature:.2f}°C' vs Target:'{target_temperature:.2f}°C' +/- '{hysteresis_temperature:.2f}°C')"
                        )
                        bosminer.restart()
                    # Temperature is more than target (with hysteresis)
                    elif current_temperature > high_threshold and bosminer.get_state():
                        LOGGER.info(
                            f"Stop mining (Temp:'{current_temperature:.2f}°C' vs Target:'{target_temperature:.2f}°C' +/- '{hysteresis_temperature:.2f}°C')"
                        )
                        bosminer.stop()
                elif not thermostat.get(state_id) and bosminer.get_state():
                    LOGGER.info("Stop mining cause thermostat state is OFF")
                    bosminer.stop()

        except Exception as e:
            LOGGER.error(f"Main loop : {e}")
            pass

        time.sleep(float(periodicity))