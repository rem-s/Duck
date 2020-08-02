from control.sensor.mic import Recorder

if __name__ == "__main__":

    recorder = Recorder()
    file_dst = './control/ai/dataset/speech_samples/text_dependent/robot_manip/banri/'
    out = recorder.record_voice(wfile_list=['forward{}.wav'.format(w) for w in range(5)], dst=file_dst, overwrite=True)
    print(out)