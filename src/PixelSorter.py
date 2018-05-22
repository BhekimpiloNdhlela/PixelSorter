''' docstring '''

from ComparativeMerge import comparative_merge_sort
from ImageFeatureVector import ImageFeatureVector as IFV

class PixelSorter(object):
    ''' docstring '''
    def __init__(self, image_name, sort_criteria):
        self.image_name = image_name
        self.sort_criteria = sort_criteria
        self.__validate_args__()

    def __validate_args__(self):
        ''' docstring '''
        if not (self.sort_criteria == 'C' or self.sort_criteria == 'L'):
            raise IOError

    def sort_pixels(self):
        ''' docstring '''
        ifv           = IFV(self.image_name, self.sort_criteria)
        pixel_data    = ifv.get_pixel_data()
        criteria_data = ifv.get_criteria_data()
        print (criteria_data[0])

        comparative_merge_sort(criteria_data, pixel_data)

if __name__ == '__main__':
    window = PixelSorter('../tests/test_cases/colorful.jpg', 'C')
    window.sort_pixels()
