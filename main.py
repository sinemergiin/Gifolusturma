import glob
from PIL import Image
def make_gif(frame_folder):
    frames = [Image.open(image) for image in glob.glob(f"{frame_folder}/*")]
    frame_one = frames[0]
    frame_one.save("download.gif", format="GIF", append_images=frames,
               save_all=True, duration=1000, loop=1)
if __name__=="__main__":
    print("inside main")
    make_gif("C:/Users/guest/Desktop/pic")