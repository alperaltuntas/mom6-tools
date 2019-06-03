import xarray as xr

class MOM6grid(object,):
    """ Encapsulates MOM6 grid data """

    def __init__(self, file_path):
        self.f = xr.open_dataset(file_path, decode_times=False)

