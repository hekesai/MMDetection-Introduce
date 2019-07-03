from mmdet.apis import init_detector, inference_detector, show_result


def detect_image(config_file,checkpoint_file,img_path):
    # build the model from a config file and a checkpoint file
    model = init_detector(config_file, checkpoint_file, device='cuda:0')

    result = inference_detector(model, img_path)
    show_result(img, result, model.CLASSES)

def detect_images(config_file,checkpoint_file,imgs_path):
    #imgs_path 包含image 路径的txt文件
    f = open(img_path)
    imgs_list = f.readlines(imgs_path)
    f.close()
    # test a list of images and write the results to image files
    for i, result in enumerate(inference_detector(model, imgs_list)):
        show_result(imgs[i], result, model.CLASSES, out_file='result_{}.jpg'.format(i))


if __name__ == '__main__':
   #file you should support
   config_file = 'configs/faster_rcnn_r50_fpn_1x.py'
   checkpoint_file = 'checkpoints/faster_rcnn_r50_fpn_1x_20181010-3d1b3351.pth'
   img_path = 'images/test01.jpg'
   
   # test a single image and show the results
   detect_image(config_file,checkpoint_file,img_path)

   #test images
   #detect_image(config_file,checkpoint_file,img_path)






