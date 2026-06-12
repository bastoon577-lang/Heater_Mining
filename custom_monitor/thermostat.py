import tinytuya

class ThermostatClient:
    def __init__(self, device_id, device_ip, local_key, device_version):
        """ Initialisation de la Classe.
        
        Args:
            device_id (str) : ID de l'équippement
            device_ip (str) : IP de l'équippementde l'équippement
            local_key (str) : Local key de l'équippement
            device_version (str) : Version Tuya
        """
        self.thermostat = tinytuya.OutletDevice(
            dev_id = device_id,
            address = device_ip,
            local_key = local_key,
            version = device_version
        )
        self.data_store = {}
        
    def update(self):
        """ Reader sur les données du thermostat.
        """
        # Check thermostat status
        status = self.thermostat.status()
        if "Error" in status:
            raise Exception("Thermostat connexion failed")
        
        # Extract thermostat data
        dps_data = status.get("dps", {})
        
        # Store thermostat data
        parsed_data = {}
        for dps_id, value in dps_data.items():
            parsed_data[dps_id] = value
        self.data_store.update(parsed_data)
        return True
        
    def get(self, key, default=None):
        """ Getter sur les données du thermostat.
        
        Args :
            key (str) : La clé ('State', 'Target' ou 'Temperature').
        """
        return self.data_store.get(key, default)