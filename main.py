import argparse
from p_acquisition.m_acquisition import acquisition

def argument_parser():
    """
    parse arguments to a script
    """
    parser = argparse.ArgumentParser(description=' ')
    parser.add_argument('-p', '--path', help='specify comp list file', type=str)
    parser.add_argument('-k', '--key', help='Open Skill API', type=str)
    args = parser.parse_args()
    return args

def main(arguments):
    print('starting process')
    path = arguments.path
    api_key = arguments.key
    acquisition(path=path, api_key=api_key) #aquí solo devuelve la db que tiene path pero no API, pero coge como api_key la url de la API definida en setup
    print(arguments.path)

    print('finish process')

if __name__ == '__main__':
    main(argument_parser())