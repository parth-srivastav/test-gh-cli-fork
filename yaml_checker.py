import yaml
import sys

def check_yaml(yaml_path, account, application_name):
    with open(yaml_path, 'r') as yaml_file:
        data = yaml.safe_load(yaml_file)

    block_deployment = data.get('blockDeployment', [])

    for item in block_deployment:
        if (
            'application' in item and 'accounts' in item and
            (application_name in item['application'] or '*' in item['application']) and (account in item['accounts'] or '*' in item['accounts'])
        ):
            return True
    
    return False

if __name__ == "__main__":
    yaml_path = sys.argv[1]
    account = sys.argv[2]
    application_name = sys.argv[3]
    if check_yaml(yaml_path, account, application_name):
        print ("Combination Found")
        sys.exit(1)
    else:
        sys.exit(0)