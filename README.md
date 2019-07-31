# rosbag-to-video
Just put it in a folder where you have your rosbags. It will search for all the subfolders and if there is a rosbag, it will generate videos from the images in the camera topics. 

# Usage

python rosbag2video_compressed.py --topics your_image_topic_1 --outnames little_additional
or more than 1 argument is allowed in case of stereo camera, or maybe hyperspectral camera if there is idk.
python rosbag2video_compressed.py --topics your_image_topic_1 --outnames little_additional_for_topic_1 --topics your_image_topic_2 ---outnames little_additional_for_topic_2
