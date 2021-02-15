import cv2 as cv
import hashlib
import sys, os
from dupecheck import dupecheck_any, dupecheck_find

### resize the output video
def resizeFrame(frame, scale):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

vid_to_check = sys.argv[1]      # user input for the video file path

if sys.getsizeof(vid_to_check) is None:   # is this even a video, bro?
    print("Video file does not exist.")
    exit(0)

capture = cv.VideoCapture(vid_to_check)
md5s = []       # list to store MD5 values for each frame
sha1s = []      # list to store SHA1 values for each frame
crops = []

# play the video until it's over or someone hits the 'D' key
while True:
    isTrue, frame = capture.read()
    cropped = frame[40:400, 40:400]     # experimental...
                                        # sample only a portion of the video frame to check for "green screening"
                                        # --- need to figure out sensitivity settings / how often the same hash comes up

    #cv.imshow('video', frame)
    try:
        rescaled = resizeFrame(frame, .5)       # rescale the video to 50% size
        cv.imshow('video', rescaled)

        ### experimental stuff -- trying to crop out a section of the frame to check for GREEN SCREENING
        cv.imshow('cropped', cropped)
        test = cv.imwrite('temp.jpg', cropped)
        img = cv.imread('temp.jpg')

    except:
        pass
    # get the MD5 hash value for the current frame
    if frame is None:
        break
    else:
        md5hash = hashlib.md5(frame)        # change to _img_ for cropped value
        md5hashed = md5hash.hexdigest()
        md5s.append(md5hashed)      # add to the MD5 list so we can later look for duplicates
        print("MD5:  " + str(md5hashed))

        # get the SHA1 hash value for the current frame
        sha1Hash = hashlib.sha1(frame)      # change to _img_ for cropped value
        sha1Hashed = sha1Hash.hexdigest()
        sha1s.append(sha1Hashed)    # add to the SHA1 list so we can later look for duplicates
        #print("SHA1: " + str(sha1Hashed))

    if cv.waitKey(20) & 0xFF==ord('d'):     # stop the video if it has ended or someone pressed 'D' key
        break

capture.release()           # no longer need to use the video, so close it up
cv.destroyAllWindows()      # close the video display window

print("Frame hashing complete.")
print("Running hash-compare...")

print("MD5s:")
print(dupecheck_any(md5s))      # check for duplicate frames -- if any exist, that is evidence of "doctored" video
print("")
print("SHA1s:")
print(dupecheck_any(sha1s))     # check for duplicate frames -- if any exist, that is evidence of "doctored" video
print("")
