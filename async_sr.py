import argparse
import os
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'myproject1.json'

def transcribe_gcs(gcs_uri,file_name):
    """Asynchronously transcribes the audio file specified by the gcs_uri."""
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    client = speech.SpeechClient()

    audio = types.RecognitionAudio(uri=gcs_uri)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=8000,
        language_code='fr')

    operation = client.long_running_recognize(config, audio)
    print('Waiting for operation to complete...')
    response = operation.result(timeout=1000)

    # Print the first alternative of all the consecutive results.
    for result in response.results:
        transc = result.alternatives[0].transcript.decode('utf-8'))
        conf = result.alternatives[0].confidence
    #     with open('result.txt', 'w') as outfile:
        #     json.dump(result.alternatives[0],outfile,ensure_ascii = False)
        print('Transcript:{}'.format(transc)
        print('Confidence: {}'.format(conf))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('speech_file', help = 'Full path of audio file to be recognized')
    parser.add_argument('file_name', help = 'Name of output text file')
    args = parser.parse_args()
    uri = 'gs://audio_project_database/ongcloud/' + args.speech_file
    fname = args.file_name
    transcribe_gcs(uri,fname)
