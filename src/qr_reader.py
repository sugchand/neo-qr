from qrtools import QR

class qr_reader():
    '''
    class to match the QR image with
    specific information.
    '''
    def __init__(self):
        pass

    def image_qr_read(self, filename):
        '''
        Read the QR image data from the image.
        '''
        qr_result = ""
        qr_data = QR(filename=filename)
        if qr_data.decode():
            print(qr_data.data)
            print(qr_data.data_type)
            print(qr_data.data_to_string())
            qr_result = qr_data.data_to_string()
        return qr_result

    def webcam_qr_read(self):
        pass

if __name__ == "__main__":
    qr_reader().image_qr_read("/home/sugesh/sree.jpg")