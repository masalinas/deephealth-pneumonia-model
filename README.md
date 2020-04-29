# retrain the deeplearning artificial net from Inception V3
python3 retrain.py --image_dir ./Sources/deephealth-covid19/train_classifed --architecture inception_v3 --saved_model_dir ./Sources/deephealth-covid19/model

# model prediction
python3 label_image.py --graph=./trained-model-inception/output_graph.pb --labels=./trained-model-inception/output_labels.txt --input_layer=Mul --output_layer=final_result --image=./server/storage/temp/person87_virus_160.jpeg

# using TensorBoard
tensorboard --logdir trained-model-inception/retrain_logs

# dataset link
https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia
