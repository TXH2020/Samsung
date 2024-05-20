# Surface Detection:

References TXH2020/deeplab2, TXH2020/models, TXH2020/fast-labeling-workflow

Use Deep Learning for understanding surfaces in order to overcome the computational burden placed by the Google ARCore App during surface understanding which causes device heating. Below is the content section for this repository.
## Image Downloader
For initial classification approach, the automatic_image_downloader.py file was used for automatically downloading various images pertaining to a horizontal surface. 
## Edge Detection

- edge_detection.py

  input: real-time image
  
  outputs:- 
  
            1. using canny filter
  
            2. using laplacian filter
            
            3. using sobel filter

## Classification(initial approach deprecated in favour of segmentation)

- samsung_tflite.py, classification.apk, m.tflite are for classification. 

  classification.apk is the classification mobile app.


- samsungdeeplearning.ipynb is for the Mask RCNN.

## Segmentation(current approach)
- deeplab2.ipynb, deeplabv3_mnv2_custom_257.tflite, deeplabv3mn_coco.ipynb, pascal_voc_deeplab.ipynb, segmentation.apk are for segmentation:-

    1. segmentation.apk is the final segmentation mobile app.
    2. deeplabv3mn_coco.ipynb: Used to train deeplab model on the surface dataset, perform inference and convert model into tflite.
    3. deeplabv3_mnv2_custom_257.tflite: Converted model.
    4. segmentation.apk: Android app which uses converted model to continuously perform segmentation on RGB images along with the display of inference time.
    5. Deeplab2.ipynb contains the modern Deeplab framework implementation while PASCAL_VOC_Deeplab.ipynb contains the code for obtaining a tflite model on the PASCAL-VOC Dataset. This is a precursor to the deeplabv3mn_coco.ipynb.

## Presentation
- Samsung July End PPT contains the presentation that was shown in the last monthly connect meet and contains every detail regarding the last approach i.e. Image Segmentation and a demo video of the Segmentation App.
- Samsung Mid Review PPT contains the presentation that was shown in the Mid Review connect of the project and contains details regarding Surface Detection and a demo video of the Surface Detection App.
- Literature Survey PPT contains the literarture survey done by our team at the beginning of the project.
- End Review PPT contains the presentation needed to be submitted in the format for the end review and contains every detail that is needed.
## Dataset
### Link to Datasets -
  
- #### Classification app -
 
    1) Vertical Surfaces(474 images) - https://drive.google.com/drive/folders/1Fp7YX08GaJPge5N5gTtWbHx_oaX0AT4o
    2) Horizontal Surfaces(463 images) - https://drive.google.com/file/d/1p3fy2fHdYJH79FNeAQ8NQMUNxkE3jU_V/view?usp=share_link
    3) Slant Surfaces(203 images) - https://drive.google.com/drive/folders/1UbPjbeLqXk0J3ylZHGftCd0Wqovmen21?usp=sharing
    
- #### Segmentation app -
 
    1) Training Dataset(118 images) - https://segments.ai/tejash/samsung_sample/
    2) Validation Dataset(5 images) - https://segments.ai/tejash/samsung_validation_set/samples
    3) Test Dataset(30 images) - https://drive.google.com/drive/folders/1Gvk3B4KlLQ9rqTdwo2_tpk-QQV0kU4Qn?usp=sharing
