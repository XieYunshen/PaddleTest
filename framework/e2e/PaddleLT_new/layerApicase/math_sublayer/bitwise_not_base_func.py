import numpy as np
import paddle


class LayerCase(paddle.nn.Layer):
    """
    case名称: bitwise_not_base
    api简介: 逐元素的对 X 和 Y 进行按位取反运算
    """

    def __init__(self):
        super(LayerCase, self).__init__()

    def forward(self, x, ):
        """
        forward
        """

        paddle.seed(33)
        np.random.seed(33)
        out = paddle.bitwise_not(x,  )
        return out


def create_tensor_inputs():
    """
    paddle tensor
    """
    inputs = (paddle.to_tensor(np.random.randint(-1, 1, [2, 3, 4, 4]).astype('int32'), dtype='int32', stop_gradient=False), )
    return inputs


def create_numpy_inputs():
    """
    numpy array
    """
    inputs = (np.random.randint(-1, 1, [2, 3, 4, 4]).astype('int32'), )
    return inputs

