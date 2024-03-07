import yaml

with open("../jupyter_config/config-selfauth-autopilot.yaml", "r") as yaml_file:
    data = yaml.safe_load(yaml_file)

data["hub"]["config"]["DummyAuthenticator"]["password"] = "dummy"

with open("../jupyter_config/config-selfauth-autopilot.yaml", 'w') as yaml_file:
    yaml.dump(data, yaml_file)