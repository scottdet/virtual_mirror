**First a note on my system:**

For this project I was using Ubuntu 16.04 and python2.7 which made the opencv instillation much easier. I referred to pyimagesearches tutorials pretty heavily and will link to a few of them that were especially helpful in learning facial recognition below.

installing opencv: https://www.pyimagesearch.com/2016/10/24/ubuntu-16-04-how-to-install-opencv/
facial regonition. This one is especially helpful: https://www.pyimagesearch.com/2017/04/17/real-time-facial-landmark-detection-opencv-python-dlib/
creating a local server: https://www.pyimagesearch.com/2015/05/11/creating-a-face-detection-api-with-python-and-opencv-in-just-5-minutes/

**Now some info on how this repository works:**

I wanted to make a basic "snapchat filter" of sorts that would place a hat on my head in real time. To install if you are using Ubuntu you can use requirements.sh and it will install opencv for you. I took a lot of time to make sure all the steps from the above tutorial on opencv were organized in that file to make things easier. 

Requirements.py contains all the other libraries necessary to run this code. Just use pip for that.

server.py and utils.py work together. These were a little harder for me to write because they are meant to be deployed to AWS or some such service so that other people could visit the url. I think the way I did this is a bit janky and utilizes constant post and get requests with basehttp python library. If you would like more information on how to do this don't hesitate to reach out because it was pretty difficult for me and a great learning experience having to do some backend stuff for the first time. This will require some SSL certificates and also setting up a server on AWS.

The more straightforward usage is server_local.py and utils_local.py. This should work straight from the start after installing opencv and the necessary libraries but only will display locally, refer to comments in the code for information on how this works.

Here are some examples of how it changed along the way. It is fairly straightfoward to edit the  `getFrame` function in the local versions to draw an outline of your face. follow the second link and mess around with opencvs drawing functions, this is both fun and a helpful learning experience. 



