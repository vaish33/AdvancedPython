### Python Buffer Protocol :

    The Python buffer protocol, also known in the community as PEP 3118, is a framework in which Python objects can expose raw byte arrays to other Python objects. This can be extremely useful for scientific computing, where we often use packages such as NumPy to efficiently store and manipulate large arrays of data. Using the buffer protocol, we can let multiple objects efficiently manipulate views of the same data buffers, without having to make copies of the often large datasets.

    For ex., we'll use Python's built-in array object to create an array:

        ```
            import array
            A = array.array('i', range(10))
            print A  

        Output :
            array('i', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

        ```

        Both Python's array and NumPy's ndarray objects implement the buffer protocol, it's possible to seamlessly pass data between them using views – that is, without the need to copy the raw data:    

        ``` import numpy as np
            np_A = np.asarray(A)
            np_A 
        
        Output :
            array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=int32)

        The buffer protocol is extremely useful for what scientists do with Python: build intuitive interfaces to compiled legacy code.