import os
import scipy.io as sio

data_dir = './eeg_data'

def get_files(dir_path):
    try:
        return os.listdir(dir_path)
    except ValueError:
        print('{0} does not exist'.format(dir_path))

def read_file(file_path):
    try:
        data = sio.loadmat(file_path)
        print('data', data['data'])
        sampling_rate = data['data'][0][0][0][0][3][0][0]
        print('sampling_rate', sampling_rate)

    except ValueError:
        print('could not read data file {0}'.format(file_path))


if __name__ == '__main__':
    files = get_files(data_dir)
    file_path = '{0}/{1}'.format(data_dir, files[0])
    read_file(file_path)
