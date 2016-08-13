import qr_mplayer
import qr_reader

if __name__ == "__main__":
    qr_read_obj = qr_reader.qr_reader()
    qr_mplayer_obj = qr_mplayer.qr_mplayer()
    qr_id = qr_read_obj.webcam_qr_read()
    if qr_id:
        video_src = qr_mplayer_obj.get_video_src_from_qr(qr_id)
        qr_mplayer_obj.video_play(video_src)