from mmdet.apis import init_detector,inference_detector,show_result
import os
import time
import mmcv

def test_inference(config_file,model_file):

    model = init_detector(config_file,model_file,device='cuda:0')

    g_loop_count = 100
    image = 'test.jpg'
    input_image = mmcv.imread(image)

    start_time = time.time()

    for i in range(g_loop_count):
        result = inference_detector(model,input_image)

    end_time = time.time()

    avg_time = (end_time-start_time) / g_loop_count

    return avg_time

if __name__ == '__main__':
    config_file = 'zhuoshi-train/cascade_rcnn_x101_64x4d_fpn_1x.py'
    model_file = 'zhuoshi-train/epoch_4.pth'

    inference_time = test_inference(config_file,model_file)
    print('model inference cost %f',inference_time)
    
