from imageloaderbase import ImageLoaderBase

class SinglepLoader(ImageLoaderBase):

    def __init__(self,imin,imax):
        super(SinglepLoader,self).__init__()
        self.name = "SinglepLoader"
        self.imin = imin
        self.imax = imax

    def __load_image__(self,img):
        
        assert img.shape[-1] == 3 #better be three channels

        for i in xrange(3):
            img[:,:,i] = img[:,:,i].T
        
        # subtract off the minimum
        img -= self.imin;
        
        # don't allow negativees
        img[ img < 0  ] = 0

        # cut the top off
        img[ img > self.imax ] = self.imax
    
        img = img[::-1,:,2:]
        
        assert img.shape[-1] == 1
        
        return img
        
        
