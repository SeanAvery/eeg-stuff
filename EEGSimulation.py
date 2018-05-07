import os
import scipy.io as sio

class EEGSimulation():
    def __init__(self):
        self.data_dir = './eeg_data'
        self.x = []
        self.y = []

    def get_files(self, dir_path):
        try:
            return os.listdir(dir_path)
        except ValueError:
            print('{0} does not exist'.format(dir_path))

    def read_file(file_path):
        try:
            self.data = sio.loadmat(file_path)
            self.sampling_rate = data['data'][0][0][0][0][3][0][0]
            print('sampling_rate', sampling_rate)

        except ValueError:
             print('could not read data file {0}'.format(file_path))
    
    def start(self):
        files = self.get_files(self.data_dir)
        file_path = '{0}/{1}'.format(data_dir, files[0])
        self.read_file(file_path)
        self.run_simulation()

    def run_simulation(self):
        for run in range(len(self.data['data'][0])):
            y.append(data['data'][0][run][0][0][2][0])
            timestamps = data['data'][0][run][0][0][1][0]
            raw_data = data['data'][0][run][0][0][0].transpose()

            for start in timestamps:
                end = start + self.trial_length 
                self.x.append(raw_data[:, start:end])

        del raw_data
        del data


if __name__ == '__main__':
    files = get_files(data_dir)
    data = read_file(file_path)
    
