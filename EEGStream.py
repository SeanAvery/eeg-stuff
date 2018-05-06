import os

data_dir = './BCICIV_1calib_1000Hz_asc/'

def get_files(path):
    try:
        return os.listdir(path)
    except ValueError:
        print('{0} does not exist'.format(path))

if __name__ == '__main__':
    files = get_files(data_dir)
    print('files', files)
