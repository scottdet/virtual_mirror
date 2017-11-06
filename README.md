**First a note on my system:**

For this project I was using Ubuntu 16.04 and python2.7 which made the opencv instillation much easier. I referred to pyimagesearches tutorials pretty heavily and will link to a few of them that were especially helpful in learning facial recognition below.

1. Installing opencv: https://www.pyimagesearch.com/2016/10/24/ubuntu-16-04-how-to-install-opencv/
2. Facial regonition. This one is especially helpful: https://www.pyimagesearch.com/2017/04/17/real-time-facial-landmark-detection-opencv-python-dlib/
3. Creating a local server: https://www.pyimagesearch.com/2015/05/11/creating-a-face-detection-api-with-python-and-opencv-in-just-5-minutes/

**Now some info on how this repository works:**

I wanted to make a basic "snapchat filter" of sorts that would place a hat on my head in real time. To install if you are using Ubuntu you can use `bash requirements.sh` and it will install opencv for you. I took a lot of time to make sure all the steps from the above tutorial on opencv were organized in that file to make things easier. 

`requirements.py` contains all the other libraries necessary to run this code. Just use `pip install requirements.py` for that.

`server.py` and `utils.py` work together. These were a little harder for me to write because they are meant to be deployed to AWS or some such service so that other people could visit the url. I think the way I did this is a bit janky and utilizes constant post and get requests with basehttprequests python library. If you would like more information on how to do this don't hesitate to reach out because it was pretty difficult for me and a great learning experience having to do some backend stuff for the first time. This will require some SSL certificates and also setting up a server on AWS.

The more straightforward usage is `server_local.py` and `utils_local.py`. This should work straight from the start after installing opencv and the necessary libraries but only will display locally, refer to comments in the code for information on how this works. It uses a fairly straightforward flask server to display the codes contents locally.

Here are some examples of how it changed along the way. It is fairly straightfoward to edit the  `getFrame` function in the local versions to draw an outline of your face. follow the second link and mess around with opencvs drawing functions, this is both fun and a helpful learning experience. 

**Recognizing my face in real time**

![Recognizing my face](https://github.com/scottdet/virtual_mirror/blob/master/recognition.gif)

**Placing a hat on my head**

Note: I realize the hat is a bit small here, this isn't the case in my current version but haven't updated the video. I also hardcoded the hat size which isn't ideal, probably better to make something that changes the hat size dynamically in the future.

![Placing a hat] (https://github.com/scottdet/virtual_mirror/blob/master/placed.gif
