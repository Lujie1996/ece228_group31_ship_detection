#### Final Project: Detecting Ship Location and Heading in Satellite Images ####

Group members: Jie Lu, Junchao Lin, Ge Lu, Haocheng Zhu

Group number: 31

#### About this repo: ####

 - Traditional_ml.ipynb shows how the traditional ML models works in classifying ship/non-ship images.
 
 - TransferLearning.ipynb shows how transfer learning works in classifying ship/non-ship images based on VGG-16 and ResNet.

 - BasicCNN.ipynb shows how we designed the basic CNN model using keras. It has has test code to run the detection.

 - Final.ipynb is based on BasicCNN.ipynb and added ship heading detection. 

#### Running guidance: ####
Note that Traditional_ml.ipynb, BasicCNN.ipynb and Final.ipynb relie on 'shipsnet.json' as dataset to train the model. BasicCNN.ipynb and Final.ipynb relie on basicCNN_test.png and test.pbg repectively to show the demo. The dataset should be in the same directory as the code files. To run TransferLearning.ipynb is more complicated. First manually split the 'shipsnet' directory into two directories: train and val. Second, run the create_csv.py to create two csv files for these two directories. After this process, now we have train and val directories and their csv files. Make sure they are in the same root directory. Now we can run the TransferLearning.ipynb.

The dataset can be downloaded at [kaggle](https://www.kaggle.com/rhammell/ships-in-satellite-imagery).
