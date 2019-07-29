import subprocess


def get_codecs():
    cmd = "ffmpeg -codecs"
    x = subprocess.check_output(cmd, shell=True)
    x = x.split(b'\n')
    for e in x:
        print(e)


def get_formats():
    cmd = "ffmpeg -formats"
    x = subprocess.check_output(cmd, shell=True)
    x = x.split(b'\n')
    for e in x:
        print(e)


def convert_seq_to_mov():
    input = r"C:\Users\HP\Desktop\FFMPEG\smoke\dense_smoke_p001.%03d.png"
    output = r"C:\Users\HP\Desktop\FFMPEG\out.mp4"
    frame_rate = 24
    cmd = f'ffmpeg -framerate {frame_rate} -i "{input}" "{output}"'
    print(cmd)
    subprocess.check_output(cmd, shell=True)


def convert_mov_to_seq():
    input = r"C:\Users\HP\Desktop\FFMPEG\playblast.mov"
    output = r"C:\Users\HP\Desktop\FFMPEG\v001\car_scene_v001.%03d.png"

    cmd = f'ffmpeg  -i "{input}" "{output}"'
    print(cmd)
    subprocess.check_output(cmd, shell=True)


def get_thumbnail():
    input = r"C:\Users\HP\Desktop\FFMPEG\comp.mov"
    output = r"C:\Users\HP\Desktop\FFMPEG\thumb.png"
    cmd = f'ffmpeg -i "{input}" -ss 00:00:01.000 -vframes 1  -s 640x360  "{output}"'
    print(cmd)
    subprocess.check_output(cmd, shell=True)
