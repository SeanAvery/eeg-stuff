import os
import scipy.io as sio

class EEGSimulation():
    def __init__(self):
        self.data_dir = './eeg_data'
        self.x = []
        self.y = []
        self.y_dim = 2
        self.x_dim = (15, 2560)

    def get_files(self, dir_path):
        try:
            return os.listdir(dir_path)
        except ValueError:
            print('{0} does not exist'.format(dir_path))

    def read_file(self, file_path):
        try:
            self.data = sio.loadmat(file_path)
            self.sampling_rate = self.data['data'][0][0][0][0][3][0][0]
            self.trial_length = 5 * self.sampling_rate
            print('self.trial_length', self.trial_length)

        except ValueError:
             print('could not read data file {0}'.format(file_path))

    def start(self):
        files = self.get_files(self.data_dir)
        file_path = '{0}/{1}'.format(self.data_dir, files[0])
        self.read_file(file_path)
        self.run_simulation()

    def run_simulation(self):
        for run in range(len(self.data['data'][0])):
            print('run', run)
            self.y.append(self.data['data'][0][run][0][0][2][0])
            timestamps = self.data['data'][0][run][0][0][1][0]
            raw_data = self.data['data'][0][run][0][0][0].transpose()

            for start in timestamps:
                end = start + self.trial_length
                self.x.append(raw_data[:, start:end])

        # print('self.y', self.y, len(self.y), self.y[0].shape)
        # print('self.x', self.x, len(self.x))
        print('sample', type(self.x[0]), self.x[0].shape)


if __name__ == '__main__':
    simulation = EEGSimulation()
    simulation.start()
